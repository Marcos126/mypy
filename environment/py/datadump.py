import os
import subprocess

# Set MySQL database credentials
DB_HOST = 'mysql'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'lomas'

# Set path to save dump.sql file
DUMP_PATH = './app/lomas.sql'

# Create a mysqldump of the database
mysqldump_cmd = f"mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {DUMP_PATH}"
subprocess.call(mysqldump_cmd, shell=True)

# Copy dump.sql file to the host machine
docker_cp_cmd = f"docker cp {DB_HOST}:{DUMP_PATH} {os.getcwd()}/dump.sql"
subprocess.call(docker_cp_cmd, shell=True)