
# Created By : Shawkath Khan
# Created On : October 19 2015
# Purpose    : To start the AWS instances using instance ID

from cm_api.api_client import ApiResource
import socket
import time
import boto.ec2
import time
import logging

logging.basicConfig()

AKID='AKIABVFGTUYTMDZEHVFHYW'
ASAK='cyZ710UEsdfsdfGasgerhersoHctzLMPKdf'
REGION='us-west-1'

# Create connection object and map region and access key id & secret access key for authentication
conn = boto.ec2.connect_to_region(REGION, aws_access_key_id=AKID, aws_secret_access_key=ASAK)
 

# Start Instance 1  by passing its instance id 
conn.start_instances(instance_ids=['i-66f73bo4'])
print "Instance 1 started"


# Start Instance 2 by passing its instance id 
conn.start_instances(instance_ids=['i-69du9bo4'])
print "Instance 2 started"
