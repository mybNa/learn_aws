import sys
import logging
import rds_config
import pymysql
import json

# rds settings
rds_host  = "myDatabase.ghfghghgf.us-east-1.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

# logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")

def handler(event, context):
    data = {
        json.dumps({
        'key': event['id'],
        'email': event['email'],
        'firstname': event['firstname'],
        'lastname': event['lastname'],
    }
    with conn.cursor() as cur:
        sql = "INSERT INTO `workers` (`key`, `email`, `firstname`, `lastname`) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (data['key'], data['email'], data['firstname'], data['lastname']))
        conn.commit()

    return {
        'statusCode': 200,
        'body': data,
        })
    }
