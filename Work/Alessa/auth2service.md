# Authentication and Services Documentation

## Service Status Check (2025-01-14 09:54:51)

### 1. Syria Lost Database
```plaintext
Host: syriaslost.db.noulez.app
Port: 5432
Status: ✅ Connected
```

### 2. Contact Database
```plaintext
Host: contact.db.noulez.app
Port: 5433
Status: ✅ Connected
```

### 3. File Storage Service (MinIO)
```plaintext
Host: syriaslost.file.noulez.app
Status: DNS Record Pending (Service Ready)
Access Points:
- Console: http://syriaslost.file.noulez.app/console/
- API: http://syriaslost.file.noulez.app
```

## Connection Details

### 1. Syria Lost Database

#### Connection URL:
```plaintext
postgresql://syria_admin:syriaslost345%40db_34@syriaslost.db.noulez.app:5432/syriaslost
```

#### Connection Parameters:
- Host: syriaslost.db.noulez.app
- Port: 5432
- Database: syriaslost
- Username: syria_admin
- Password: syriaslost345@db_34

### 2. Contact Database

#### Connection URL:
```plaintext
postgresql://postgres:contact123%40noulez.app@contact.db.noulez.app:5433/postgres
```

#### Connection Parameters:
- Host: contact.db.noulez.app
- Port: 5433
- Database: postgres
- Username: postgres
- Password: contact123@noulez.app

### 3. File Storage Service

#### Access Details:
- API Endpoint: http://syriaslost.file.noulez.app
- Console URL: http://syriaslost.file.noulez.app/console/
- Access Key: 483f166836971280
- Secret Key: 9dqxipSuR0FOhZRofnqEjRAAopxDo3yNzXCGnKT6wjQ=

## Implementation Examples

### PostgreSQL Databases

#### Node.js
```javascript
// Syria Lost Database
const syriaDB = new Pool({
  host: 'syriaslost.db.noulez.app',
  database: 'syriaslost',
  user: 'syria_admin',
  password: 'syriaslost345@db_34',
  port: 5432,
});

// Contact Database
const contactDB = new Pool({
  host: 'contact.db.noulez.app',
  database: 'postgres',
  user: 'postgres',
  password: 'contact123@noulez.app',
  port: 5433,
});
```

#### Python
```python
# Syria Lost Database
syria_conn = psycopg2.connect(
    host='syriaslost.db.noulez.app',
    port=5432,
    database='syriaslost',
    user='syria_admin',
    password='syriaslost345@db_34'
)

# Contact Database
contact_conn = psycopg2.connect(
    host='contact.db.noulez.app',
    port=5433,
    database='postgres',
    user='postgres',
    password='contact123@noulez.app'
)
```

### File Storage Service

#### Node.js
```javascript
const Minio = require('minio');

const minioClient = new Minio.Client({
  endPoint: 'syriaslost.file.noulez.app',
  port: 80,
  useSSL: false,
  accessKey: '483f166836971280',
  secretKey: '9dqxipSuR0FOhZRofnqEjRAAopxDo3yNzXCGnKT6wjQ='
});

// Upload file
minioClient.fPutObject('bucket-name', 'file.txt', '/path/to/file.txt');

// Download file
minioClient.fGetObject('bucket-name', 'file.txt', '/path/to/download/file.txt');
```

#### Python
```python
from minio import Minio

client = Minio(
    'syriaslost.file.noulez.app',
    access_key='483f166836971280',
    secret_key='9dqxipSuR0FOhZRofnqEjRAAopxDo3yNzXCGnKT6wjQ=',
    secure=False
)

# Upload file
client.fput_object('bucket-name', 'file.txt', '/path/to/file.txt')

# Download file
client.fget_object('bucket-name', 'file.txt', '/path/to/download/file.txt')
```

## Infrastructure Notes

1. All services are hosted behind HAProxy for load balancing
2. PostgreSQL services use TCP mode routing:
   - Syria Lost DB on port 5432
   - Contact DB on port 5433
3. File Storage uses HTTP mode routing on port 80
4. Internal network isolation between services

## DNS Configurations

Added the following DNS A records:
```plaintext
syriaslost.file.noulez.app.  IN  A  46.202.141.56
contact.db.noulez.app.       IN  A  46.202.141.56
syriaslost.db.noulez.app.    IN  A  46.202.141.56
```

### Databases
1. Daily full backups using pg_dump
2. Point-in-time recovery setup
3. Regular backup testing
4. Separate backup storage location

### File Storage
1. Bucket versioning enabled
2. Cross-region replication for critical data
3. Regular consistency checks
4. Automated backup verification

Last Updated: 2025-01-14 09:54:51
