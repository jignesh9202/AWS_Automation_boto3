import boto3
aws_mgmt_con = boto3.session.Session(profile_name="default")
sts_con = aws_mgmt_con.client('sts')
resposne = sts_con.get_caller_identity()
print(resposne)
