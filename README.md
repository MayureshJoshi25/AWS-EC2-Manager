# aws-ec2-manager
A Python script for managing EC2 instances and querying CloudWatch Logs.

## Usage

Make sure you have Python installed on your system.

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/aws-ec2-logs-manager.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd aws-ec2-logs-manager
    ```

3. Replace the placeholder values in the script with your actual AWS credentials, region, instance ID, and log group name.

4. Run the script using Python:

    ```bash
    python aws.py {start|stop}
    ```

    Replace `{start|stop}` with the action you want to perform on your EC2 instance.

## Requirements

- Python 3.x
- boto3 library (install using `pip install boto3`)
- AWS account with appropriate permissions for EC2 and CloudWatch Logs
