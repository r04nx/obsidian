---
share_link: https://share.note.sx/37x3rhs6#p2+oQaLN3aEqUwj+b+rJ0OjqYagwGFWhUx4aXpyH/ug
share_updated: 2025-05-22T16:51:33+05:30
---

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe-XLdAD8BtL5_YBTeZ0413p4Jc29gB5IU6SgCJv8K5dd7KIGwrp3RApyMT5mnEQatVQJ9hF9TeylR01UWEMMlhk5RxDsjJxQslQERD0lTnHmovXQn4HCZy6HvEO04OKZCeakWDyQ?key=TFQ4HtOREcr1OtbiqDJ7OQ)

# Cloud Computing Lab 9: Advanced AWS Services

> [!note] Student Details
> - **Name:** Rohan Prakash Pawar
> - **UID:** 2023201020
> - **Branch:** EE
> - **Date:** May 22, 2025
> - **Course:** OECS1- Cloud Computing
> - **Academic Year:** 2024-2025
> - **Module:** Module-3: Cloud Computing Services
> - **Part:** Part-I: AWS Cloud Services 

## Lab Exercise 1: Building Data Pipelines from Ingestion to Analytics

> [!abstract] Objective
> To design and implement a real-time data pipeline for processing telecom customer call data using AWS services, enabling analytics and insights generation.

### Requirements

> [!info] Requirements
> - AWS Account with appropriate permissions
> - Knowledge of AWS Kinesis, Glue, and Redshift
> - Python for data simulation
> - Basic understanding of data processing workflows

### Scenario

A telecom company needs to implement real-time analytics on customer call data to improve service quality and business decision-making. The solution must handle continuous data ingestion, processing, and storage for analytical queries.

### Problem Statement

Build an end-to-end data pipeline using AWS Kinesis for data ingestion, AWS Glue for data processing, and Amazon Redshift for data warehousing and analytics.

### Expected Outcomes

> [!success] Expected Outcomes
> - Real-time data ingestion and processing pipeline
> - Structured data storage in a queryable format
> - Ability to generate insights from Redshift queries
> - Scalable architecture that can handle increasing data volumes

### Solution Architecture

> [!tip] Solution Steps
> 1. Stream data using Amazon Kinesis
> 2. Process and transform data with AWS Glue
> 3. Store and analyze data in Amazon Redshift
    

### Procedure

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdXVta4oKtQUtZir4UUyNeW4ZuDrXjfSGV0XggmuXOMrImOz9M8aeLv5IwPoE9IYlJdrrkjruYbh4Cpntk9zquJ9cA53IBx0ClAxwlsOVTEeKq9lWp1as3ufIRFaf190eDwamdecg?key=TFQ4HtOREcr1OtbiqDJ7OQ)

#### Step 1: Data Ingestion using Amazon Kinesis

1. Create a Kinesis Data Stream named `call-data-stream`
2. Implement a Python script to simulate and push call data to Kinesis:

```python
import boto3, json, time
from datetime import datetime
import random

# Initialize Kinesis client
kinesis = boto3.client('kinesis', region_name='us-east-1')
stream_name = 'call-data-stream' # Replace with your stream name

def generate_call_data():
    return {
        "call_id": random.randint(1000, 9999),
        "caller": f"User_{random.randint(1, 100)}",
        "duration": random.randint(1, 600),
        "timestamp": datetime.utcnow().isoformat()
    }

while True:
    data = generate_call_data()
    kinesis.put_record(
        StreamName=stream_name,
        Data=json.dumps(data),
        PartitionKey=str(data["call_id"])
    )
    print(f"Sent: {data}")
    time.sleep(1) # Send one record per second
```

#### Step 2: Data Processing with AWS Glue

1. Create an AWS Glue job or crawler to fetch data from the Kinesis stream
2. Transform and clean the data (e.g., parsing timestamps, filtering unnecessary fields)
3. Convert and store the data in a format suitable for Redshift (e.g., Parquet or CSV)

#### Step 3: Data Storage and Analysis in Amazon Redshift

1. Set up an Amazon Redshift cluster
2. Create tables to match the processed schema
3. Load data from S3 (processed by Glue) into Redshift using COPY command
4. Use SQL queries to generate insights, such as:
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcU3oiJJ6AcQ1IYdnr9LtXvbvDrWOcF0M_nhqormfJCH69E8W7NWHYnlBNlYNATHJT-cQF-Xj3MwVQI7r0p28nJPV3OCbfdU2hhNzMpuzYmVBwWrdYgDIm1Gu0Fi76gY4HvSk7d?key=TFQ4HtOREcr1OtbiqDJ7OQ)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf86k3yrdW-ZITgaj21UK-YAnn0S6zM06vxIWsSOjgP7trRc_jYcsnQArJtKkailLjgfK97pJkiugfeVe9GnAPgkpWSw1TL40FsSPgTMpXuZj75jsQa9w03ss0iOJyxMs7ePNKxjg?key=TFQ4HtOREcr1OtbiqDJ7OQ)

### Observation

> [!important] Key Observations
> - The Kinesis Data Stream successfully ingested simulated call data at a rate of one record per second
> - AWS Glue effectively processed and transformed the streaming data
> - The data was successfully loaded into Redshift tables
> - SQL queries on the Redshift cluster provided valuable insights such as:
>   - Average call duration by user
>   - Call volume patterns by time of day
>   - Identification of users with abnormally long calls

### Conclusion

> [!success] Conclusion
> In this lab exercise, I successfully built a complete data pipeline for real-time analytics on telecom call data using AWS services. The implementation demonstrated how to:
> 
> 1. Use Kinesis for real-time data ingestion
> 2. Process and transform streaming data with AWS Glue
> 3. Store and analyze data in Amazon Redshift
> 4. Generate actionable insights through SQL queries
> 
> This architecture provides a scalable, reliable solution for handling real-time data processing needs. The telecom company can now analyze customer call patterns, optimize service quality, and make data-driven business decisions based on the insights generated from this pipeline.

---

## Lab Exercise 2: Multi-Cloud Strategies & Hands-on Implementation

> [!abstract] Objective
> To design and implement a hybrid cloud environment spanning multiple cloud providers (AWS and Azure) with centralized logging capabilities, demonstrating cross-cloud application deployment and monitoring.

### Requirements

> [!info] Requirements
> - AWS and Azure accounts with appropriate permissions
> - Node.js and Express.js for application development
> - Winston logging library with Elasticsearch integration
> - Docker and Docker Compose for containerization
> - Basic understanding of multi-cloud architectures

### Scenario

A multinational corporation needs to implement a hybrid cloud setup to leverage the strengths of different cloud providers, ensure geographic redundancy, and avoid vendor lock-in. The solution must include centralized logging to maintain visibility across all cloud environments.

### Problem Statement

Deploy a multi-cloud environment using AWS and Azure with centralized logging capabilities to monitor and manage applications running across both cloud platforms.

### Expected Outcomes

> [!success] Expected Outcomes
> - Successfully deployed workloads running across AWS and Azure
> - Centralized logging system collecting and visualizing logs from both cloud environments
> - Ability to monitor application health and performance across clouds
> - Demonstration of multi-cloud architecture benefits

### Solution Architecture

> [!tip] Solution Steps
> 1. Deploy application instances on both AWS EC2 and Azure VMs
> 2. Configure a common logging and monitoring solution using ELK stack
> 3. Test the multi-cloud deployment with centralized visibility

### Procedure

#### Step 1: Create a Sample Application with Centralized Logging

1. Develop a Node.js application with Winston and Elasticsearch for logging:

```javascript
const express = require('express');
const { createLogger, format, transports } = require('winston');
const { ElasticsearchTransport } = require('winston-elasticsearch');

const esTransportOpts = {
  level: 'info',
  clientOpts: {
    node: 'http://localhost:9200', // adjust if needed
  },
  indexPrefix: 'node-app-logs',
};

const logger = createLogger({
  level: 'info',
  format: format.combine(
    format.timestamp(),
    format.json()
  ),
  transports: [
    new ElasticsearchTransport(esTransportOpts),
    new transports.Console()
  ]
});

const app = express();
const port = 3000;

app.get('/', (req, res) => {
  logger.info('Home route accessed', { route: '/', method: req.method });
  res.send('Hello from Node.js + Winston + Elasticsearch');
});

app.get('/error', (req, res) => {
  logger.error('Something went wrong!', { route: '/error', method: req.method });
  res.status(500).send('Internal Server Error');
});

app.listen(port, () => {
  logger.info(`Server started on http://localhost:${port}`);
});
```

#### Step 2: Deploy the Application on Multiple Cloud Platforms

1. Deploy the application on AWS EC2 and Azure VMs
2. Configure both deployments to include a `/health` endpoint for monitoring

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXerE5MK2gvmf14pISgaI-g20gGG8pv6HufHRe9r1nK74A26qINpcYReXDjwu1-K90TjN8vxwNwKRv3iu6NFcifsDm2-S9cTYyAcPeaErBoUT3EStP-m_toHS-MRTXsM0I5N70m_KQ?key=TFQ4HtOREcr1OtbiqDJ7OQ)

#### Step 3: Set Up Centralized Logging

3. Set up Elasticsearch and Kibana containers for log collection and visualization using Docker Compose:

```yaml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.12.2
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - bootstrap.memory_lock=true
      - ES_JAVA_OPTS=-Xms1g -Xmx1g
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - esdata:/usr/share/elasticsearch/data
    ports:
      - "9200:9200"

  kibana:
    image: docker.elastic.co/kibana/kibana:8.12.2
    container_name: kibana
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
      - xpack.security.enabled=false
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch

volumes:
  esdata:
```

#### Step 4: Test the Multi-Cloud Deployment

1. Access the application endpoints from both cloud deployments
2. Verify logs are being collected in the centralized Kibana dashboard

Azure deployment logs:
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcf0yse9TvUP28HOlxxEXESll-3DsSctQlAHG60Prm5Ecuv_ddLhpE0SB8sfFK6iwWz-S4lnW0QEEcol5N8c12ZHI0SGvnXm9WMTo2mGfu22AhCaGKm0rPiaG4p4wJJWbyqfrIuOg?key=TFQ4HtOREcr1OtbiqDJ7OQ)

AWS deployment logs:
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeVVoaG_vX2mlMSaYegsbWecLkujVGzbrcelhxCbD6HY9CBY2n7rDpzW9firUNi1__F77wjXdEdPuTcZwMXJwUXiRr1lldRiA9wBVjqaU3N2M9_UKYZcz1AfYPAJL3uxVtm87zTuA?key=TFQ4HtOREcr1OtbiqDJ7OQ)

### Observation

> [!important] Key Observations
> - The Node.js application was successfully deployed on both AWS EC2 and Azure VMs
> - The Winston logging library effectively sent logs to the centralized Elasticsearch instance
> - Kibana dashboard provided a unified view of logs from both cloud environments
> - The multi-cloud setup demonstrated resilience and flexibility across providers
> - Log data was properly structured and indexed, making it searchable and analyzable

### Conclusion

> [!success] Conclusion
> In this lab exercise, I successfully implemented a multi-cloud environment using AWS and Azure with centralized logging capabilities. The implementation demonstrated:
> 
> 1. How to deploy identical workloads across multiple cloud providers
> 2. The configuration of a centralized logging system using the ELK stack
> 3. Real-time collection and visualization of logs from distributed applications
> 4. The benefits of a multi-cloud strategy for resilience and avoiding vendor lock-in
> 
> This architecture provides organizations with improved visibility across cloud environments, enhanced disaster recovery capabilities, and the ability to leverage the unique strengths of different cloud providers. The centralized logging solution significantly improves troubleshooting, monitoring, and security analysis in a distributed multi-cloud environment.