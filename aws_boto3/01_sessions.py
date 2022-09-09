## Create Session and then create resouce or client
import boto3
aws_mgmt_con = boto3.session.Session(profile_name="default")

s3_con = aws_mgmt_con.resource('s3')

## Using Resource --> Returns Object
print("========= Buckets ===========")
for each_bucket in s3_con.buckets.all():
    print(each_bucket.name)
print("========= Users ===========")
iam_con = aws_mgmt_con.resource('iam')
for each_user in iam_con.users.all():
    print(each_user.name)
print("==================================================")

## Using Client --> Returns Dictionary -- Low level api
s3_con = aws_mgmt_con.client('s3')
for each_bucket in s3_con.list_buckets()['Buckets']:
    print(each_bucket['Name'])
##############################################################
#without creating Session
print("===== Without Session =======")
buckets = boto3.resource('s3')
for each_bucket in buckets.buckets.all():
    print(each_bucket.name)
