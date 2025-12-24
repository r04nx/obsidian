---
share_link: https://share.note.sx/upcbo40v#UkuTev61iNBeGIRs8X6Ob8mYbrcEmtw2C9hM42aEx/w
share_updated: 2025-12-24T21:31:56+05:30
---
## Supabase Staging – Developer Quick Access Doc

**Environment:** STAGING  
**Hosting:** Self-hosted Supabase on Coolify  
**Gateway:** Kong  
**Network:** Public HTTPS + Tailscale (internal)

---

## 1️⃣ Base URLs

### 🌐 Public (USE THIS FOR DEV)

```
https://supabase-staging-gw.100.93.34.45.sslip.io
```

### 🔒 Internal (Infra / Docker only)

```
http://supabase-kong:8000
```

❗ **Frontend & SDKs must NEVER use internal URLs**

---

## 2️⃣ Supabase Keys (STAGING)

### ✅ Client / Frontend (SAFE – RLS enforced)

```env
SUPABASE_URL=https://supabase-staging-gw.100.93.34.45.sslip.io
SUPABASE_ANON_KEY=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdXBhYmFzZSIsImlhdCI6MTc2NjU4ODA0MCwiZXhwIjo0OTIyMjYxNjQwLCJyb2xlIjoiYW5vbiJ9.K6Bx89zymqv-JSG0ftRLitwJKlRxeuk4qSRp7Gnak50
```

---

### 🔐 Backend / Admin (SERVER ONLY)

```env
SUPABASE_SERVICE_ROLE_KEY=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdXBhYmFzZSIsImlhdCI6MTc2NjU4ODA0MCwiZXhwIjo0OTIyMjYxNjQwLCJyb2xlIjoic2VydmljZV9yb2xlIn0.jHOidEGNrfjk0uAANIwADxZw_W9pdvuB3HIt153VlqM
```

⚠️ **NEVER use this key in frontend apps**

---

## 3️⃣ Supabase APIs

|Service|Endpoint|
|---|---|
|REST|`/rest/v1/`|
|Auth|`/auth/v1/`|
|Storage|`/storage/v1/`|
|Realtime|`/realtime/v1/`|
|Functions|`/functions/v1/`|

### Example

```
GET https://supabase-staging-gw.100.93.34.45.sslip.io/rest/v1/profiles
```

---

## 4️⃣ Auth (Email-based)

### 🔑 Enabled

- Email + Password
    
- Magic Link
    
- Password Recovery
    

### ❌ Disabled

- Auto email confirmation
    

---

## 5️⃣ Auth Verify / Redirect URLs

Supabase uses **one verify endpoint for all flows**:

```
/auth/v1/verify
```

### Example confirmation link

```
https://supabase-staging-gw.100.93.34.45.sslip.io/auth/v1/verify?token=XXX&type=signup
```

Used for:

- Email signup confirmation
    
- Magic link login
    
- Password recovery
    
- Invite acceptance
    

---

## 6️⃣ SMTP (Email Sending – STAGING)

```env
SMTP_HOST=mail.grantwritingwithai.com
SMTP_PORT=465
SMTP_USER=noreply@grantwritingwithai.com
SMTP_PASS=KT!rKWOT)m~6
SMTP_SENDER_NAME=GrantWritingWithAI
SMTP_ADMIN_EMAIL=noreply@grantwritingwithai.com
```

From address:

```
noreply@grantwritingwithai.com
```

---

## 7️⃣ Supabase Studio (Admin UI)

```
https://supabase-staging-gw.100.93.34.45.sslip.io
```

**Admin Login**

```text
Username: Qlafa5vh0XDMXO57
Password: c5TUyEecLJKkpjXWlYlofwMpWPwx7qa0
```

---

## 8️⃣ Health Check (DEBUG)

```
GET /auth/v1/health
```

Expected:

```json
{ "status": "ok" }
```

---

## 9️⃣ Frontend SDK Example (JS)

```ts
import { createClient } from '@supabase/supabase-js'

export const supabase = createClient(
  'https://supabase-staging-gw.100.93.34.45.sslip.io',
  'PUBLIC_ANON_KEY'
)
```

---

## 🔐 Security Rules (MANDATORY)

- ✅ Use **Anon key** in frontend
    
- ❌ Never expose **Service Role key**
    
- ❌ Never use internal Docker URLs
    
- ✅ Use HTTPS public gateway only
    

---

## 🧠 Dev Notes

- Emails may land in **spam** (staging)
    
- RLS is enabled → queries may return empty if policies missing
    
- Kong handles routing → do not bypass it
    

---

