
# Created By : Shawkath Khan
# Created On : October 19 2015
# Purpose      : To stop the AWS instances using instance ID
# Updated By :   Shawkath Khan
# Updated On : Nov 2 2015

import boto.ec2

AKID='AKIAFOASD6AW4RE2F23WQ'
ASAK='tT1i1opb90SD034NNANQLFEvDhx'
REGION='us-west-1'

# Create connection object and map region and access key id & secret access key for authentication
conn = boto.ec2.connect_to_region(REGION, aws_access_key_id=AKID, aws_secret_access_key=ASAK)

# Stop instance 1  by passing its instance id 
conn.stop_instances(instance_ids=['i-66sy7Cd4'])

# Stop Instance 2  by passing its instance id 
conn.stop_instances(instance_ids=['i-66sd5h5s'])
