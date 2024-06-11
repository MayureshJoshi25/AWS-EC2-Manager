import boto.ec2
import boto.logs
import boto3
import sys
from datetime import datetime, timedelta
import time

# AWS credentials, replace with your actual credentials
auth = {"aws_access_key_id": "your_access_key_id_here", "aws_secret_access_key": "your_secret_access_key_here"}

# Create a CloudWatch Logs client
client = boto3.client('logs')

# Specify the CloudWatch Logs log group to query
log_group = "your_log_group_here"


def main():
    # Check if the script is called with the correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: python aws.py {start|stop}\n")
        sys.exit(0)
    else:
        # Get the action (start or stop) from the command-line arguments
        action = sys.argv[1]

    # Perform the appropriate action based on the command-line argument
    if action == "start":
        startInstance()
    elif action == "stop":
        stopInstance()
    else:
        print("Usage: python aws.py {start|stop}\n")


def startInstance():
    print("Starting the instance...")

    try:
        # Connect to the specified AWS region
        ec2 = boto.ec2.connect_to_region("your_region_here", **auth)
        time.sleep(2)  # Pause for 2 seconds

    except Exception as e1:
        # Handle connection errors
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    try:
        # Start the specified EC2 instance
        ec2.start_instances(instance_ids="your_instance_id_here")

    except Exception as e2:
        # Handle errors when starting instances
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)


def stopInstance():
    print("Stopping the instance...")

    try:
        # Connect to the specified AWS region
        ec2 = boto.ec2.connect_to_region("your_region_here", **auth)

    except Exception as e1:
        # Handle connection errors
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    try:
        # Stop the specified EC2 instance
        ec2.stop_instances(instance_ids="your_instance_id_here")

    except Exception as e2:
        # Handle errors when stopping instances
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)


def getLogs():
    # Start a CloudWatch Logs query
    response = client.start_query(
        logGroupName=log_group,
        logGroupNames=[log_group],
        logGroupIdentifiers=[
            'arn:aws:logs:your_region_here:your_aws_account_id_here:log-group:your_log_group_here:*',
        ],
        startTime=int((datetime.today() - timedelta(hours=5)).timestamp()),  # Query logs from the past 5 hours
        endTime=int(datetime.now().timestamp()),  # Up to the current time
        queryString='fields @timestamp, @message',  # Specify the query
        limit=123  # Limit the number of log events returned
    )
    print(response)


if __name__ == '__main__':
    main()
    time.sleep(3)  # Wait for 3 seconds before fetching logs
    getLogs()
