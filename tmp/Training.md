---
share_link: https://share.note.sx/m8idc5z4#zaDvyOqblxjGID+b91kuoCtGcj20uW89wj/URjjt0Mc
share_updated: 2025-03-17T11:05:59+05:30
---
# AWS IAM & S3 Training Guide

## 🟢 **1. AWS IAM Overview**

### 🔹 **What is IAM?**
- AWS IAM (Identity and Access Management) allows you to securely control access to AWS services and resources.
- Key Components:
  - **Users**: Individual accounts with permissions.
  - **Groups**: Collection of users sharing permissions.
  - **Roles**: Temporary permissions assigned to AWS services.
  - **Policies**: JSON-based permissions assigned to users, groups, or roles.

### 🛠 **Hands-On: Creating an IAM User with S3 Access**

1. **Login to AWS Console** → Navigate to **IAM**.
2. **Create a new IAM User:**
   - Name: `s3-user-demo`
   - Select **Programmatic Access** (For API/CLI usage).
3. **Attach a Custom Policy:**
   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": ["s3:ListBucket", "s3:GetObject"],
               "Resource": ["arn:aws:s3:::demo-bucket", "arn:aws:s3:::demo-bucket/*"]
           }
       ]
   }
   ```
4. **Retrieve Access Key & Secret Key**.
5. **Test access using AWS CLI:**
   ```sh
   aws configure
   aws s3 ls s3://demo-bucket
   ```

---

## 🟡 **2. AWS S3 Overview**

### 🔹 **What is Amazon S3?**
- **Object Storage**: Stores files (objects) in buckets.
- **Highly Scalable & Secure**.
- **Use Cases**: Data backup, hosting, big data, etc.

### 🛠 **Hands-On: Creating an S3 Bucket**
1. Navigate to **S3 Console → Create Bucket**.
2. Name it uniquely (e.g., `demo-bucket`).
3. Enable **Versioning** & **Encryption (SSE-S3 / KMS)**.
4. Upload a sample file.

### 🔹 **Bucket Policies & Access Control**
- Create a bucket policy for **public read access**:
  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Principal": "*",
              "Action": "s3:GetObject",
              "Resource": "arn:aws:s3:::demo-bucket/*"
          }
      ]
  }
  ```
- **Generate a presigned URL for secure access:**
  ```sh
  aws s3 presign s3://demo-bucket/sample.txt --expires-in 3600
  ```

### 🔹 **Enable Lifecycle Policies & Logging**
1. **Add Lifecycle Rule** → Move objects to **Glacier** after 30 days.
2. **Enable S3 Access Logging**.

---

## 🔴 **3. Best Practices & Security**

- **Never use Root Account for daily tasks**.
- **Enable MFA for IAM Users**.
- **Use IAM Roles instead of Access Keys**.
- **Enable CloudTrail to track S3 activities**.
- **Use VPC Endpoints for S3 (Private Access)**.

---

## 🟢 **4. Hands-On Tasks for Participants**

✅ Create an IAM User with restricted S3 access.
✅ Generate a **presigned URL** for file access.
✅ Modify Bucket Policy to allow access from a specific IP.
✅ Enable & Test **S3 Object Versioning**.

---

## S3 Demo

```bash
aws s3 mb s3://demo-bucket
```

then do 
```bash
aws s3 ls
```

then do enable the public access

```bash
aws s3api put-public-access-block --bucket r04nx --public-access-block-configuration "BlockPublicAcls=false,
IgnorePublicAcls=false,
BlockPublicPolicy=false,
RestrictPublicBuckets=false"
```

to query the bucket policy 
```bash
aws s3api get-bucket-policy --bucket r04nx
```

to put the bucket policy
```bash
aws s3api put-bucket-policy --bucket r04nx --policy '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::r04nx/*"
        }
    ]
}
'
```
