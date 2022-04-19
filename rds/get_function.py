import sys
import logging
import rds_config
import pymysql

# rds settings
rds_host  = "myDatabase.ghfghghgf.us-east-1.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

# logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# connect using creds from rds_config.py
try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")

# array to store values to be returned
records = []

# executes upon API event
def handler(event, context):
   with conn.cursor() as cur:
   cur.execute("select * from employees")
   conn.commit()
   for row in cur:
            record = {
                    'employee_id': row[1],
                    'employee_info': {
                        'firstname': row[2],
                        'lastname': row[3],
                        'email': row[4],
                    }
                }
            records.append(record)
    return records
