![[Pasted image 20250503211119.png]]
# CCN Lab Practical: Using SSL Server and Client Tests

> [!info]+ Student Information
> **Name:** Rohan Prakash Pawar
> **UID:** 2023201020
> **Experiment No.:** 08  

## Aim
Using SSL Server and Client Tests

## Objectives
In this activity, you will use online tests to determine the security of web servers and your local web browser.

## Website Analysis

### Website 1: mahadbt.maharashtra.gov.in

#### Overview
The SSL report for the website mahadbt.maharashtra.gov.in shows an overall security rating of **A+**, indicating excellent HTTPS configuration and adherence to industry best practices. The site scores nearly 100% across key evaluation metrics.

> [!placeholder]+ SSL Labs Overall Rating Screenshot
> *Insert screenshot of the overall SSL Labs rating for mahadbt.maharashtra.gov.in*
> 

#### Certificate Configuration
The SSL certificate configuration for mahadbt.maharashtra.gov.in demonstrates a secure and properly managed setup.

| Certificate Property | Value |
|---------------------|-------|
| Key Type | RSA 2048-bit |
| Signature Algorithm | SHA256withRSA |
| Issued To | *.maharashtra.gov.in |
| Issued By | GlobalSign RSA OV SSL CA 2018 |
| Valid From | January 24, 2025 |
| Valid To | February 25, 2026 |
| Status | Valid (Not Revoked) |
| Compliance | Certificate Transparency Compliant |

The certificate is trusted by major platforms:
- ✅ Mozilla
- ✅ Apple
- ✅ Android
- ✅ Java
- ✅ Windows

> [!note] Minor Chain Issue
> The report highlights a minor chain issue: "Contains anchor". This means the server has included a root certificate in the chain, which is typically unnecessary and may cause compatibility warnings in strict configurations—although it usually doesn't affect real-world browser trust.

> [!placeholder]+ Details Screenshot
> ![[Pasted image 20250503210226.png]]

#### Certification Path
The certificate chain is properly structured and trusted by all major platforms with a 3-step certification path:

1. **Leaf Certificate**: *.maharashtra.gov.in (2048-bit RSA key with SHA256withRSA)
2. **Intermediate Certificate**: GlobalSign RSA OV SSL CA 2018
3. **Root Certificate**: GlobalSign (Self-signed)

> [!placeholder]+ Screenshot
> ![[Pasted image 20250503210314.png]]

#### Protocol Support

| Protocol | Status |
|----------|--------|
| TLS 1.3 | ❌ Disabled |
| TLS 1.2 | ✅ Enabled |
| TLS 1.1 | ❌ Disabled |
| TLS 1.0 | ❌ Disabled |
| SSL 3 | ❌ Disabled |
| SSL 2 | ❌ Disabled |
![[Pasted image 20250503210455.png]]
> [!warning] Opportunity for Improvement
> The absence of TLS 1.3, the most modern and efficient protocol, indicates a missed opportunity for improved performance and stronger security.

#### Cipher Suites
The server supports two TLS 1.2 cipher suites, both using strong encryption and forward secrecy:

1. **TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256** (Preferred)
2. **TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384**
![[Pasted image 20250503210511.png]]

Both utilize Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) with the secp256r1 curve (equivalent to 3072-bit RSA security) to ensure Perfect Forward Secrecy (FS).

#### Security Features

| Feature | Status | Description |
|---------|--------|-------------|
| Secure Renegotiation | ✅ Supported | Protects against certain man-in-the-middle attacks |
| BEAST Attack | ✅ Mitigated | Not a concern |
| Forward Secrecy | ✅ Enabled | Ensures past sessions remain secure even if the server's key is compromised |
| Session Resumption | ✅ Supported | Improves performance by reusing secure session info |
| HSTS | ✅ Enabled | Forces browsers to use HTTPS for future visits |
| ALPN | ✅ Supported | Allows HTTP/2 |
| Key Exchange Parameters | ✅ No reuse | Prevents some types of attacks |
| Elliptic Curve Support | ✅ Good | Supports secp256r1, secp384r1, secp521r1 |

> [!success] Disabled/Not Supported (Mostly Good)
> - ✅ Old/insecure protocols & ciphers (SSL 2/3, TLS compression, RC4, Heartbeat) are disabled
> - ✅ No vulnerabilities like POODLE, Zombie POODLE, GOLDENDOODLE
> - ✅ Public Key Pinning (HPKP) not used (this is OK, as HPKP is deprecated)

> [!warning] Areas for Improvement
> - ❌ OCSP Stapling not supported (not ideal, but not critical)
> - ❌ HSTS Preloading not enabled (would enhance HSTS effect but not mandatory)
> - ❓ Downgrade attack prevention is "Unknown" (likely because older protocols are disabled)

### Website 2: multimedbilling.com

#### Overview
The SSL Labs report for the website multimedbilling.com shows a failing grade of **F**, indicating serious security misconfigurations.

> [!placeholder]+ SSL Labs Overall Rating Screenshot
> ![[Pasted image 20250503210532.png]]

#### Certificate Configuration

| Certificate Property | Value |
|---------------------|-------|
| Key Type | RSA 2048-bit |
| Signature Algorithm | SHA256withRSA |
| Issued To | *.multimedbilling.com |
| Issued By | Go Daddy Secure Certificate Authority - G2 |
| Valid From | March 29, 2024 |
| Valid To | May 31, 2025 |
| Status | **REVOKED** ⚠️ |
| OCSP Must Staple | Not enabled |

The certificate is **NOT** trusted by any major platforms due to revocation:
- ❌ Mozilla
- ❌ Apple
- ❌ Android
- ❌ Java
- ❌ Windows

> [!danger] Critical Issue
> Despite using strong encryption standards, the presence of an untrusted certificate alone is enough for SSL Labs to assign the lowest possible grade.

> [!placeholder]+ Certificate Details Screenshot
> *Insert screenshot of certificate details showing revocation*

#### Certification Path
Two certification paths are listed, both including the revoked server certificate at the top of the chain:

1. **Leaf Certificate**: *.multimedbilling.com (Revoked)
2. **Intermediate Certificate**: Go Daddy Secure Certificate Authority - G2
3. **Root Certificate**: Go Daddy Root Certificate Authority - G2 or The Go Daddy Group, Inc. / Go Daddy Class 2 Certification Authority
![[Pasted image 20250503210612.png]]

> [!warning] Trust Broken
> Because the server certificate has been explicitly revoked, the entire chain is considered untrustworthy, regardless of the validity of the root certificates.

> [!placeholder]+ Certification Path Screenshot
> ![[Pasted image 20250503210633.png]]

#### Protocol Support

| Protocol | Status |
|----------|--------|
| TLS 1.3 | ✅ Enabled |
| TLS 1.2 | ✅ Enabled |
| TLS 1.1 | ❌ Disabled |
| TLS 1.0 | ❌ Disabled |
| SSL 3 | ❌ Disabled |
| SSL 2 | ❌ Disabled |
![[Pasted image 20250503210656.png]]
> [!note] 
> The server was tested using No-SNI (Server Name Indication) mode, which is experimental, but this does not affect the support for these protocols.

#### Cipher Suites

**TLS 1.3 Cipher Suites:**
1. TLS_AES_256_GCM_SHA384
2. TLS_AES_128_GCM_SHA256

**TLS 1.2 Cipher Suites:**

| Cipher Suite | Security Rating | Forward Secrecy |
|--------------|-----------------|-----------------|
| ECDHE_RSA_WITH_AES_256_GCM_SHA384 | Strong | ✅ Yes |
| ECDHE_RSA_WITH_AES_128_GCM_SHA256 | Strong | ✅ Yes |
| *Various AES-CBC mode ciphers* | Weak | ❌ No |
| *Various RSA key exchange ciphers* | Weak | ❌ No |
![[Pasted image 20250503210710.png]]
> [!warning]
> The presence of weak cipher suites represents a potential security risk.

#### Security Features

| Feature | Status | Description |
|---------|--------|-------------|
| Secure Renegotiation | ✅ Supported | Good |
| Client-initiated Renegotiation | ❌ Not supported | Reduces potential attack vectors |
| BEAST Attack | ✅ Mitigated | Server-side mitigation in place |
| POODLE Vulnerabilities | ✅ Not vulnerable | Not applicable or server does not support vulnerable protocols |
| RC4 Cipher | ✅ Not used | Positive since RC4 is deprecated |
| Heartbleed & Ticketbleed | ✅ Not vulnerable | Not exploitable |
| OpenSSL Vulnerabilities | ✅ Not vulnerable | CVE-2014-0224 and CVE-2016-2107 not present |
| ROBOT Attack | ✅ Not exploitable | Not vulnerable |
| SSL/TLS Compression | ✅ Disabled | Helps prevent CRIME attacks |
| Downgrade Attack Prevention | ❌ Not implemented | TLS_FALLBACK_SCSV not supported |
| Forward Secrecy | ✅ ROBUST | Excellent from a cryptographic perspective |
| Session Resumption (caching) | ❌ Not functioning | ID is assigned but not accepted |
| Session Tickets | ⚠️ Supported but not trusted | Due to untrusted certificate |
| OCSP Stapling | ❌ Not verified | Affects certificate revocation checking |
| HSTS | ❌ Not enabled | Missing key header for protection against protocol downgrade attacks |
| HSTS Preloading | ❌ Not configured | Not preloaded in major browsers |
| ALPN and NPN | ✅ Supported | Used for HTTP/2 negotiation |
| Public Key Pinning (HPKP) | ❌ Not in use | Not implemented |
| Elliptic Curves Support | ✅ Strong | Includes secp521r1, secp384r1, and secp256r1 |

> [!danger] Resolution Required
> To resolve these issues, the site administrator should:
> - Install a valid certificate from a trusted CA
> - Ensure the correct certificate chain is served
> - Enable OCSP stapling and preload HSTS for better security

## Conclusion
In this experiment, we performed SSL Server and Client Tests using SSL Labs to evaluate the SSL/TLS configurations of mahadbt.maharashtra.gov.in and multimediabilling.com. We understood the importance of both strong encryption protocols and valid certificate management in securing web communications.

Key findings:
- Mahadbt.maharashtra.gov.in showed a secure setup with TLS 1.2 support, strong cipher suites, and a valid, trusted certificate chain, indicating proper implementation of security best practices.
- In contrast, although multimediabilling.com also supported modern TLS protocols (including TLS 1.3), it failed due to a revoked SSL certificate, leading to an untrusted status on all major platforms.

This experiment highlighted that even with modern protocol support, a revoked or invalid certificate compromises the overall trust and security of a site. It emphasizes the critical need for continuous monitoring and timely renewal of SSL certificates to ensure secure and trusted web services.
