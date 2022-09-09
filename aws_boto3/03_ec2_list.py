import boto3
from tabulate import tabulate

# Create Session and client if profile other than default require to use
'''aws_mgmt_con = boto3.session.Session(profile_name='default')
ec2_con = aws_mgmt_con.client('ec2')'''

# if default profile can be used then create client as below
ec2_con = boto3.client('ec2')
response = ec2_con.describe_instances()

table = [
    [item['ImageId'], item['InstanceId'], item['LaunchTime'].strftime("%Y-%m-%d"), item['InstanceType'],
     item['PublicDnsName'], item['State']['Name'], item['Placement']['AvailabilityZone']]
    for each_item in response['Reservations']
    for item in each_item['Instances']
]
headers = ['ImageId', 'InstanceId', 'LaunchTime' , 'InstanceType', 'PublicDnsName', 'State','AvailabilityZone']
print(tabulate(table, headers, tablefmt="pretty"))


