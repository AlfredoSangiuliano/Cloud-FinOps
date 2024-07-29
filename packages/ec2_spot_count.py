import boto3
from datetime import datetime, timedelta

def list_cost_generating_services():
    # Create a Cost Explorer client
    client = boto3.client('ce')

    # Define the time period (last 30 days)
    end = datetime.today().date()
    start = end - timedelta(days=30)

    try:
        # Call get_cost_and_usage to get cost data
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': str(start),
                'End': str(end)
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost'],
            GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
        )

        # Print information about each service
        print("AWS Services Generating Costs:")
        for result in response['ResultsByTime'][0]['Groups']:
            service = result['Keys'][0]
            cost = result['Metrics']['UnblendedCost']['Amount']
            print(f"Service: {service}, Cost: ${cost}")
    except boto3.exceptions.Boto3Error as e:
        print(f"Error retrieving cost data: {e}")

if __name__ == "__main__":
    list_cost_generating_services()
