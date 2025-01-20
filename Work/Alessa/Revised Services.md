# Service Credentials and Endpoints Documentation

## 1. Database Services

### 1.1 Syriaslost Database
```
Host: syriaslost.db.noulez.app
Port: 5434
Database: syriaslost
Username: syria_admin
Password: syriaslost345@db_34
Connection URL: postgresql://syria_admin:syriaslost345%40db_34@syriaslost.db.noulez.app:5434/syriaslost
```

Example connection (Python with psycopg2):
```python
import psycopg2

conn = psycopg2.connect(
    host="syriaslost.db.noulez.app",
    port="5434",
    database="syriaslost",
    user="syria_admin",
    password="syriaslost345@db_34"
)
```

### 1.2 Contact Database
```
Host: contact.db.noulez.app
Port: 5432
Database: postgres
Username: postgres
Password: contact123@noulez.app
Connection URL: postgresql://postgres:contact123%40noulez.app@contact.db.noulez.app:5432/postgres
```

Example connection (Python with psycopg2):
```python
import psycopg2

conn = psycopg2.connect(
    host="contact.db.noulez.app",
    port="5432",
    database="postgres",
    user="postgres",
    password="contact123@noulez.app"
)
```

### 1.3 Database Management (pgAdmin)
```
URL: https://db.noulez.app

For Artin
Email: artin@noulez.app 
Password: Artin@noulez.app

For Zeb
Email: zeb@noulez.app
Password: Zeb@noulez.app
```

## 2. File Storage Service (MinIO)

### 2.1 Endpoints
```
API Endpoint: https://syriaslost.file.noulez.app
Console URL: https://syriaslost.file.noulez.app/console/
```

### 2.2 Credentials
```
Access Key: 483f166836971280
Secret Key: 9dqxipSuR0FOhZRofnqEjRAAopxDo3yNzXCGnKT6wjQ=
```

### 2.3 Usage Examples

#### Python (using boto3)
```python
import boto3

s3_client = boto3.client(
    's3',
    endpoint_url='https://syriaslost.file.noulez.app',
    aws_access_key_id='483f166836971280',
    aws_secret_access_key='9dqxipSuR0FOhZRofnqEjRAAopxDo3yNzXCGnKT6wjQ=',
    region_name='us-east-1'
)

# Upload file
s3_client.upload_file('file.txt', 'bucket-name', 'file.txt')

# Download file
s3_client.download_file('bucket-name', 'file.txt', 'downloaded.txt')

# Generate pre-signed URL (valid for 1 hour)
url = s3_client.generate_presigned_url(
    'get_object',
    Params={'Bucket': 'bucket-name', 'Key': 'file.txt'},
    ExpiresIn=3600
)
```

#### JavaScript (AWS SDK)
```javascript
const AWS = require('aws-sdk');

const s3 = new AWS.S3({
    endpoint: 'https://syriaslost.file.noulez.app',
    accessKeyId: '483f166836971280',
    secretAccessKey: '9dqxipSuR0FOhZRofnqEjRAAopxDo3yNzXCGnKT6wjQ=',
    s3ForcePathStyle: true,
    signatureVersion: 'v4',
    region: 'us-east-1'
});

// Upload file
s3.upload({
    Bucket: 'bucket-name',
    Key: 'file.txt',
    Body: fileContent
}).promise();

// Download file
s3.getObject({
    Bucket: 'bucket-name',
    Key: 'file.txt'
}).promise();

// Generate pre-signed URL
const url = s3.getSignedUrl('getObject', {
    Bucket: 'bucket-name',
    Key: 'file.txt',
    Expires: 3600  // URL valid for 1 hour
});
```

#### AWS CLI
```bash
# Configure AWS CLI
aws configure
# Enter the following:
# AWS Access Key ID: 483f166836971280
# AWS Secret Access Key: 9dqxipSuR0FOhZRofnqEjRAAopxDo3yNzXCGnKT6wjQ=
# Default region name: us-east-1
# Default output format: json

# Use MinIO with AWS CLI
aws --endpoint-url https://syriaslost.file.noulez.app s3 ls
aws --endpoint-url https://syriaslost.file.noulez.app s3 cp file.txt s3://bucket-name/
aws --endpoint-url https://syriaslost.file.noulez.app s3 cp s3://bucket-name/file.txt ./
```

## Security Notes

1. All services are accessible only via HTTPS
2. All connections use SSL/TLS encryption
3. No direct port access is available (all through reverse proxy)
4. CORS is configured to allow cross-origin requests
5. Credentials should be stored securely and not exposed in client-side code
6. Use environment variables for sensitive information
7. For temporary file access, use pre-signed URLs instead of sharing credentials

## Support

For issues or access requests, contact the Linux team.