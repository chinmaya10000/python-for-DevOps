import requests
import smtplib
import os
import paramiko  # SSH to remote server
import boto3
import time
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_REGION = 'us-east-1'  # Set your AWS region
INSTANCE_ID = 'i-xxxxxxxxxxxxxx'  # Replace with your EC2 instance ID
NGINX_SERVER_IP = 'YOUR_NGINX_SERVER_PUBLIC_IP'  # IP of the server running Nginx
PRIVATE_KEY_PATH = '/path/to/your/private/key.pem'  # Path to your private key file


def restart_server_and_container():
    # Reboot AWS EC2 instance
    print('Rebooting the server...')
    ec2 = boto3.client('ec2', region_name=AWS_REGION,
                       aws_access_key_id=AWS_ACCESS_KEY,
                       aws_secret_access_key=AWS_SECRET_KEY)
    ec2.reboot_instances(InstanceIds=[INSTANCE_ID])

    # Wait until the instance is running
    ec2_resource = boto3.resource('ec2', region_name=AWS_REGION,
                                  aws_access_key_id=AWS_ACCESS_KEY,
                                  aws_secret_access_key=AWS_SECRET_KEY)
    instance = ec2_resource.Instance(INSTANCE_ID)
    instance.wait_until_running()

    # Restart the container once the instance is running
    time.sleep(5)
    restart_container()


def send_notification(email_msg):
    print('Sending an email...')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


def restart_container():
    print('Restarting the application on the Nginx server...')
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=NGINX_SERVER_IP, username='ec2-user', key_filename=PRIVATE_KEY_PATH)
        stdin, stdout, stderr = ssh.exec_command('docker start YOUR_CONTAINER_ID')  # Replace with your container ID
        print('Docker output:', stdout.read().decode())
        error = stderr.read().decode()
        if error:
            print('Error restarting container:', error)
        else:
            print('Application restarted successfully!')
    except Exception as e:
        print(f'Failed to connect or execute command: {e}')
    finally:
        ssh.close()


def monitor_application():
    try:
        response = requests.get(f'http://{NGINX_SERVER_IP}:8080/')
        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application Down. Fix it!')
            msg = f'Application returned {response.status_code}'
            send_notification(msg)
            restart_container()
    except Exception as ex:
        print(f'Connection error happened: {ex}')
        msg = 'Application not accessible at all'
        send_notification(msg)
        restart_server_and_container()


# Monitor every 5 minutes
schedule.every(5).minutes.do(monitor_application)

while True:
    schedule.run_pending()
    time.sleep(1)
