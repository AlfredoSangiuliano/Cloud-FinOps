import boto3
from datetime import datetime, timedelta

def list_ec2_costs():
    # Create a Cost Explorer client
    client = boto3.client('ce')
    
    # Define the time period (last 30 days)
    end = datetime.today().date()
    start = end - timedelta(days=30)
    
    try:
        # Call get_cost_and_usage to get cost data for EC2
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': str(start),
                'End': str(end)
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost'],
            Filter={
                'Dimensions': {
                    'Key': 'SERVICE',
                    'Values': ['Amazon Elastic Compute Cloud - Compute']
                }
            },
            GroupBy=[
                {'Type': 'DIMENSION', 'Key': 'USAGE_TYPE'}
            ]
        )
        
        # Initialize cost variables
        total_cost = 0.0
        spot_cost = 0.0
        on_demand_cost = 0.0
        
        # Print information about each usage type
        print("EC2 Costs for the Last 30 Days:")
        for result in response['ResultsByTime'][0]['Groups']:
            usage_type = result['Keys'][0]
            cost = float(result['Metrics']['UnblendedCost']['Amount'])
            total_cost += cost
            if 'Spot' in usage_type:
                spot_cost += cost
            else:
                on_demand_cost += cost
            print(f"Usage Type: {usage_type}, Cost: ${cost:.2f}")
        
        # Print summary
        print("\nSummary:")
        print(f"Total EC2 Cost: ${total_cost:.2f}")
        print(f"Spot Instances Cost: ${spot_cost:.2f}")
        print(f"On-Demand Instances Cost: ${on_demand_cost:.2f}")
        
    except boto3.exceptions.Boto3Error as e:
        print(f"Error retrieving cost data: {e}")