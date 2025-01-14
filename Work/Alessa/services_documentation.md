# Services Documentation

This document provides comprehensive information about all deployed services, including access details, credentials, and usage examples.

## Table of Contents
1. [PostgreSQL Databases](#postgresql-databases)
2. [MinIO Object Storage](#minio-object-storage)
3. [File Browser](#file-browser)

## PostgreSQL Databases

### 1. Syria Database
#### Connection Details
- Host: syriaslost.db.noulez.app
- Port: 5432
- Database: syriaslost
- Username: syria_admin
- Password: syriaslost345@db_34

#### Usage Examples

```bash
# Command line connection
PGPASSWORD='syriaslost345@db_34' psql -h syriaslost.db.noulez.app -p 5432 -U syria_admin -d syriaslost
```

```python
# Python with psycopg2
import psycopg2

conn = psycopg2.connect(
    dbname="syriaslost",
    user="syria_admin",
    password="syriaslost345@db_34",
    host="syriaslost.db.noulez.app",
    port="5432"
)
```

### 2. Contact Database
#### Connection Details
- Host: contact.db.noulez.app
- Port: 5433
- Database: postgres
- Username: postgres
- Password: contact123@noulez.app

#### Usage Examples

```bash
# Command line connection
PGPASSWORD='contact123@noulez.app' psql -h contact.db.noulez.app -p 5433 -U postgres -d postgres
```

```python
# Python with psycopg2
import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="contact123@noulez.app",
    host="contact.db.noulez.app",
    port="5433"
)
```

## MinIO Object Storage

### Access Details
- API Endpoint: https://syriaslost.file.noulez.app
- Console URL: https://syriaslost.file.noulez.app/console/
- Access Key: 483f166836971280
- Secret Key: 9dqxipSuR0FOhZRofnqEjRAAopxDo3yNzXCGnKT6wjQ=

### Usage Examples

#### 1. Using MinIO Client (mc)
```bash
# Configure MinIO Client
mc alias set minio https://syriaslost.file.noulez.app 483f166836971280 9dqxipSuR0FOhZRofnqEjRAAopxDo3yNzXCGnKT6wjQ=

# List buckets
mc ls minio

# Upload file
mc cp myfile.txt minio/mybucket/

# Download file
mc cp minio/mybucket/myfile.txt ./
```

#### 2. Python with boto3
```python
import boto3

# Configure S3 client
s3_client = boto3.client('s3',
    endpoint_url='https://syriaslost.file.noulez.app',
    aws_access_key_id='483f166836971280',
    aws_secret_access_key='9dqxipSuR0FOhZRofnqEjRAAopxDo3yNzXCGnKT6wjQ=',
    verify=True  # Set to False if using self-signed certificates
)

# List buckets
buckets = s3_client.list_buckets()

# Upload file
s3_client.upload_file('local_file.txt', 'bucket_name', 'remote_file.txt')

# Download file
s3_client.download_file('bucket_name', 'remote_file.txt', 'downloaded_file.txt')
```

#### 3. Using curl
```bash
# List buckets
curl -X GET https://syriaslost.file.noulez.app \
    -H "Authorization: AWS4-HMAC-SHA256 Credential=483f166836971280/$(date -u +%Y%m%d)/us-east-1/s3/aws4_request"

# Upload file (requires proper AWS v4 signing)
curl -X PUT -T file.txt \
    -H "Host: syriaslost.file.noulez.app" \
    https://syriaslost.file.noulez.app/bucket-name/file.txt
```

## File Browser

### Access Details
- URL: https://files.noulez.app
- Username: admin
- Password: noulez@Admin123

### Features
- Full system file access (/)
- File upload/download
- Directory creation/deletion
- File sharing
- Web-based file management

### Usage Examples

#### 1. Using Web Interface
1. Navigate to https://files.noulez.app
2. Login with admin credentials
3. Browse and manage files through the web interface

#### 2. Using curl
```bash
# Login and get token
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"username":"admin","password":"noulez@Admin123"}' \
    https://files.noulez.app/api/login

# List files (with token)
curl -H "X-Auth: YOUR_TOKEN" https://files.noulez.app/api/resources
```

## Security Notes

1. Password Security
   - Change default passwords after first login
   - Use strong, unique passwords
   - Regularly rotate credentials

2. Access Control
   - MinIO: Use bucket policies and user policies
   - PostgreSQL: Create specific users with limited privileges
   - File Browser: Use sharing features carefully

3. SSL/TLS
   - All services are configured with HTTPS
   - Valid SSL certificates are in place
   - Regular certificate renewal is automated



# Environment Variables for All Services

# PostgreSQL - Syria Database
SYRIA_DB_HOST=syriaslost.db.noulez.app
SYRIA_DB_PORT=5432
SYRIA_DB_NAME=syriaslost
SYRIA_DB_USER=syria_admin
SYRIA_DB_PASSWORD=syriaslost345@db_34
SYRIA_DB_URL=postgresql://syria_admin:syriaslost345@db_34@syriaslost.db.noulez.app:5432/syriaslost

# PostgreSQL - Contact Database
CONTACT_DB_HOST=contact.db.noulez.app
CONTACT_DB_PORT=5433
CONTACT_DB_NAME=postgres
CONTACT_DB_USER=postgres
CONTACT_DB_PASSWORD=contact123@noulez.app
CONTACT_DB_URL=postgresql://postgres:contact123@noulez.app@contact.db.noulez.app:5433/postgres

# MinIO Object Storage
MINIO_API_ENDPOINT=https://syriaslost.file.noulez.app
MINIO_CONSOLE_URL=https://syriaslost.file.noulez.app/console/
MINIO_ACCESS_KEY=483f166836971280
MINIO_SECRET_KEY=9dqxipSuR0FOhZRofnqEjRAAopxDo3yNzXCGnKT6wjQ=

# File Browser
FILEBROWSER_URL=https://files.noulez.app
FILEBROWSER_USER=admin
FILEBROWSER_PASSWORD=noulez@Admin123
FILEBROWSER_DATABASE=/home/rohan/filebrowser.db
FILEBROWSER_ROOT=/

# Container Ports (Local)
LOCAL_SYRIA_DB_PORT=5434
LOCAL_CONTACT_DB_PORT=5435
LOCAL_MINIO_API_PORT=9000
LOCAL_MINIO_CONSOLE_PORT=9001
LOCAL_FILEBROWSER_PORT=8080

# Additional Information
NGINX_SSL_PATH=/etc/letsencrypt/live
MINIO_DATA_PATH=/srv/minio/data
MINIO_CONFIG_PATH=/srv/minio/config


