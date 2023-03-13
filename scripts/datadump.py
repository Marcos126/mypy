import os
import subprocess

# Set MySQL database credentials
CT_HOST = 'mysql'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'lomas'

#Set path to save dump.sql file
DUMP_PATH = 'lomas.sql'

# Create a mysqldump of the database
mysqldump_cmd = f"mysqldump -h {CT_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {DUMP_PATH}"
subprocess.call(mysqldump_cmd, shell=True)

# Copy dump.sql file to the host machine
docker_cp_cmd = f"docker cp {CT_HOST}:{DUMP_PATH} {os.getcwd()}"
subprocess.call(docker_cp_cmd, shell=True)