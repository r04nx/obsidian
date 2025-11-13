---
share_link: https://share.note.sx/11q0qh9a#NtsYFyJEC+n1RKI82zH7HCs40Mk+Oi4O2FBG5dbqPvk
share_updated: 2025-11-06T15:06:20+05:30
---

# 🔬 ASN.1 Compiler (asn1c) - Lab Practical Guide

> **A beginner's guide to ASN.1, TLV encoding, and the asn1c compiler**

---

## 📋 Table of Contents

1. [What is ASN.1?](#what-is-asn1)
2. [Installation](#installation)
3. [Understanding TLV Format](#understanding-tlv-format)
4. [Basic ASN.1 Schema Creation](#basic-asn1-schema-creation)
5. [Compiling ASN.1 to C Code](#compiling-asn1-to-c-code)
6. [Encoding: ASN.1 → TLV](#encoding-asn1--tlv)
7. [Decoding: TLV → ASN.1](#decoding-tlv--asn1)
8. [Encoding Types (BER/DER/PER/XER)](#encoding-types)
9. [Practical Examples](#practical-examples)
10. [Troubleshooting](#troubleshooting)

---

## 🤔 What is ASN.1?

**ASN.1** (Abstract Syntax Notation One) is a standard language for defining data structures that can be serialized and deserialized across different platforms.

### Key Concepts:
- **Schema Definition**: Like a blueprint for data (similar to JSON schema)
- **Platform Independent**: Works across languages and systems
- **Binary Efficient**: Compact encoding for network protocols
- **Used In**: SSL/TLS certificates, mobile networks (4G/5G), SNMP, etc.

### Simple Analogy:
Think of ASN.1 as a **recipe** (schema) and TLV as the **packaged meal** (encoded data).

---

## 💻 Installation

### Step 1: Install Dependencies
```bash
sudo apt-get update
sudo apt-get install -y git build-essential automake libtool
```

### Step 2: Clone asn1c Repository
```bash
cd ~
git clone https://github.com/vlm/asn1c.git
cd asn1c
```

### Step 3: Build the Compiler
```bash
# Generate configure script
test -f configure || autoreconf -iv

# Configure the build
./configure

# Compile (use all CPU cores)
make -j$(nproc)

# Optional: Install system-wide
sudo make install
```

### Step 4: Verify Installation
```bash
./asn1c/asn1c -h
```

You should see: `ASN.1 Compiler, v0.9.29`

---

## 🏷️ Understanding TLV Format

**TLV = Tag-Length-Value**

### Structure:
```
┌─────┬────────┬──────────────┐
│ Tag │ Length │    Value     │
└─────┴────────┴──────────────┘
```

### Example: Encoding the integer `42`
```
BER/DER Encoding:
┌────┬────┬────┐
│ 02 │ 01 │ 2A │  
└────┴────┴────┘
  │    │    │
  │    │    └─ Value: 42 in hex (0x2A)
  │    └────── Length: 1 byte
  └─────────── Tag: 02 = INTEGER type
```

### Tag Meanings (Common):
| Tag (Hex) | Type | Description |
|-----------|------|-------------|
| `02` | INTEGER | Whole numbers |
| `04` | OCTET STRING | Raw bytes |
| `0C` | UTF8String | Text strings |
| `30` | SEQUENCE | Container (like struct) |
| `A0-AF` | CONTEXT | Tagged fields |

---

## 📝 Basic ASN.1 Schema Creation

### Example 1: Simple Person Record

Create file: `person.asn1`
```asn1
PersonModule DEFINITIONS ::= BEGIN

    Person ::= SEQUENCE {
        name    UTF8String,
        age     INTEGER (0..150),
        email   UTF8String OPTIONAL
    }

END
```

### Syntax Breakdown:
- `PersonModule`: Module name (like namespace)
- `DEFINITIONS ::= BEGIN ... END`: Module boundary
- `Person ::= SEQUENCE`: Define a structure
- `UTF8String`: Text data type
- `INTEGER (0..150)`: Number with constraint
- `OPTIONAL`: Field can be omitted

---

## ⚙️ Compiling ASN.1 to C Code

### Basic Compilation:
```bash
# Create output directory
mkdir -p ~/person-output

# Compile ASN.1 schema to C code
~/asn1c/asn1c/asn1c \
    -S ~/asn1c/skeletons \
    -D ~/person-output \
    person.asn1
```

### What Gets Generated:
```
person-output/
├── Person.c              ← Implementation
├── Person.h              ← Header with struct definition
├── Makefile.am.*         ← Build files
├── converter-example.c   ← Example program
└── [skeleton files]      ← Support libraries (BER, DER, etc.)
```

### Generated C Structure:
```c
// In Person.h
typedef struct Person {
    UTF8String_t  name;
    long          age;
    UTF8String_t *email;  /* OPTIONAL - pointer */
    
    asn_struct_ctx_t _asn_ctx;
} Person_t;
```

---

## 📤 Encoding: ASN.1 → TLV

### Step 1: Create a C Program

File: `encode_person.c`
```c
#include <stdio.h>
#include <assert.h>
#include "Person.h"

int main() {
    Person_t person;
    asn_enc_rval_t er;
    
    // Initialize structure
    memset(&person, 0, sizeof(person));
    
    // Set name
    OCTET_STRING_fromBuf(&person.name, "Alice", 5);
    
    // Set age
    person.age = 30;
    
    // Email is NULL (optional field not set)
    person.email = NULL;
    
    // Encode to DER (TLV format)
    er = der_encode_to_buffer(&asn_DEF_Person, &person, 
                               buffer, sizeof(buffer));
    
    if(er.encoded == -1) {
        fprintf(stderr, "Encoding failed\n");
        return 1;
    }
    
    // Print TLV hex dump
    printf("Encoded %ld bytes:\n", (long)er.encoded);
    for(int i = 0; i < er.encoded; i++) {
        printf("%02X ", buffer[i]);
    }
    printf("\n");
    
    // Cleanup
    ASN_STRUCT_FREE_CONTENTS_ONLY(asn_DEF_Person, &person);
    return 0;
}
```

### Step 2: Compile
```bash
cd ~/person-output
gcc -I. encode_person.c Person.c [skeleton *.c files] -o encode_person
```

### Step 3: Run
```bash
./encode_person
```

**Output (TLV):**
```
30 0D 0C 05 41 6C 69 63 65 02 01 1E
│  │  │  │  └─────┬──────┘ │  │  └─ 0x1E = 30 (age)
│  │  │  │        └────────── "Alice" in ASCII
│  │  │  └─────────────────── Length: 5 bytes
│  │  └────────────────────── Tag: 0C (UTF8String)
│  └───────────────────────── Length: 13 bytes total
└──────────────────────────── Tag: 30 (SEQUENCE)
```

---

## 📥 Decoding: TLV → ASN.1

### Method 1: Using C Code

File: `decode_person.c`
```c
#include <stdio.h>
#include "Person.h"

int main() {
    // TLV data (from encoding example)
    uint8_t tlv[] = {0x30, 0x0D, 0x0C, 0x05, 0x41, 0x6C, 
                     0x69, 0x63, 0x65, 0x02, 0x01, 0x1E};
    
    Person_t *person = NULL;
    asn_dec_rval_t rval;
    
    // Decode TLV to structure
    rval = ber_decode(0, &asn_DEF_Person, (void **)&person,
                      tlv, sizeof(tlv));
    
    if(rval.code != RC_OK) {
        fprintf(stderr, "Decoding failed\n");
        return 1;
    }
    
    // Print decoded values
    printf("Name: %.*s\n", (int)person->name.size, 
           person->name.buf);
    printf("Age: %ld\n", person->age);
    printf("Email: %s\n", person->email ? "present" : "absent");
    
    // Cleanup
    ASN_STRUCT_FREE(asn_DEF_Person, person);
    return 0;
}
```

### Method 2: Using unber Tool (Quick Inspection)

```bash
# Save TLV data to file
echo "300D0C05416C69636502011E" | xxd -r -p > person.ber

# Decode and inspect
~/asn1c/asn1-tools/unber/unber person.ber
```

**Output:**
```xml
<P O="0" T="[UNIVERSAL 16]" TL="2" V="13">
  <P O="2" T="[UNIVERSAL 12]" TL="2" V="5">Alice</P>
  <P O="9" T="[UNIVERSAL 2]" TL="2" V="1">30</P>
</P>
```

---

## 🔄 Encoding Types

### Comparison Table:

| Encoding | Type | Size | Use Case |
|----------|------|------|----------|
| **BER** | Binary | Variable | General purpose, flexible |
| **DER** | Binary | Canonical | Certificates, signatures (deterministic) |
| **PER** | Binary | Compact | Mobile networks (space-critical) |
| **XER** | Text/XML | Large | Debugging, human-readable |

### API Functions:

```c
// BER (Basic Encoding Rules)
ber_decode()    // Decode TLV → struct
der_encode()    // Encode struct → TLV (DER is BER subset)

// PER (Packed Encoding Rules) - more compact
uper_decode()   // Decode
uper_encode()   // Encode

// XER (XML Encoding Rules) - human readable
xer_decode()    // Decode XML
xer_encode()    // Encode to XML

// OER (Octet Encoding Rules) - newest
oer_decode()
oer_encode()
```

### Example: Encoding in Different Formats

```c
// DER (binary, canonical)
der_encode_to_buffer(&asn_DEF_Person, &person, buf, sizeof(buf));

// XER (XML format)
xer_encode(&asn_DEF_Person, &person, XER_F_BASIC, 
           write_to_stdout, stdout);

// UPER (compact binary)
uper_encode_to_buffer(&asn_DEF_Person, NULL, &person, 
                      buf, sizeof(buf));
```

---

## 🧪 Practical Examples

### Example 1: Certificate Structure (X.509)

```bash
# Compile X.509 certificate schema
cd ~/asn1c-x509
~/asn1c/asn1c/asn1c \
    -fcompound-names \
    -S ~/asn1c/skeletons \
    ~/asn1c/examples/rfc3280-*.asn1

# Generated files include:
# - Certificate.c/h
# - TBSCertificate.c/h
# - AlgorithmIdentifier.c/h
# etc.
```

### Example 2: Mobile Network Message (RRC)

```bash
# 3GPP RRC messages (used in 4G/5G)
~/asn1c/asn1c/asn1c \
    -S ~/asn1c/skeletons \
    ~/asn1c/examples/rrc-7.1.0.asn1
```

### Example 3: Custom Protocol

Create `message.asn1`:
```asn1
MessageProtocol DEFINITIONS ::= BEGIN

    Message ::= SEQUENCE {
        messageId   INTEGER (0..65535),
        timestamp   INTEGER,
        payload     OCTET STRING,
        priority    ENUMERATED { low(0), medium(1), high(2) }
    }

END
```

Compile:
```bash
~/asn1c/asn1c/asn1c \
    -S ~/asn1c/skeletons \
    -D ~/message-output \
    message.asn1
```

---

## 🛠️ Troubleshooting

### Issue 1: Name Clashes
**Error:** `FATAL: Name 'xyz' is generated by...`

**Solution:** Use compound names flag
```bash
~/asn1c/asn1c/asn1c -fcompound-names ...
```

### Issue 2: Missing Skeleton Files
**Error:** `Cannot find standard modules in /usr/local/share/asn1c`

**Solution:** Specify skeleton directory explicitly
```bash
~/asn1c/asn1c/asn1c -S ~/asn1c/skeletons ...
```

### Issue 3: Compilation Errors
**Error:** `fatal error: asn_application.h: No such file or directory`

**Solution:** Include current directory and compile with skeleton files
```bash
gcc -I. your_program.c Person.c [other generated files] *.c
```

### Issue 4: Decoding Fails
**Problem:** `ber_decode()` returns error

**Debug:**
```bash
# Inspect TLV with unber
~/asn1c/asn1-tools/unber/unber -p your_file.ber

# Check if tags match your schema
```

---

## 📚 Quick Reference Card

### Essential Commands:

```bash
# Compile ASN.1 schema
~/asn1c/asn1c/asn1c -S ~/asn1c/skeletons schema.asn1

# Inspect BER/DER file
~/asn1c/asn1-tools/unber/unber file.ber

# Print ASN.1 tree (debugging)
~/asn1c/asn1c/asn1c -E schema.asn1

# Validate and fix syntax
~/asn1c/asn1c/asn1c -EF schema.asn1
```

### Common ASN.1 Types:

```asn1
BOOLEAN              -- true/false
INTEGER              -- whole numbers
OCTET STRING         -- raw bytes
UTF8String           -- text
SEQUENCE             -- struct/record
SEQUENCE OF          -- array
CHOICE               -- union (one of)
ENUMERATED           -- enum
BIT STRING           -- bit flags
OBJECT IDENTIFIER    -- OID (e.g., 1.2.840.113549)
```

### Encoding Function Pattern:

```c
// Encode
asn_enc_rval_t result = XXX_encode_to_buffer(
    &asn_DEF_YourType,    // Type descriptor
    &your_struct,          // Data to encode
    buffer,                // Output buffer
    buffer_size            // Buffer size
);

// Decode
asn_dec_rval_t result = XXX_decode(
    0,                     // Options (usually 0)
    &asn_DEF_YourType,    // Type descriptor
    (void **)&ptr,         // Pointer to receive data
    input_buffer,          // Input TLV data
    input_size             // Input size
);
```

Replace `XXX` with: `ber`, `der`, `uper`, `xer`, `oer`

---

## 🎯 Lab Exercise Checklist

- [ ] Install asn1c successfully
- [ ] Create a simple ASN.1 schema (Person example)
- [ ] Compile schema to C code
- [ ] Write encoding program (ASN.1 → TLV)
- [ ] Write decoding program (TLV → ASN.1)
- [ ] Use `unber` to inspect TLV data
- [ ] Try different encoding types (DER, XER, UPER)
- [ ] Compile and test X.509 certificate example
- [ ] Handle OPTIONAL and CHOICE types
- [ ] Debug a decoding error

---

## 📖 Additional Resources

- **Official Documentation**: `~/asn1c/doc/asn1c-usage.pdf`
- **Examples**: `~/asn1c/examples/`
- **Man Page**: `man asn1c`
- **ASN.1 Book**: "ASN.1 Communication between heterogeneous systems" by Olivier Dubuisson
- **Online Compiler**: http://lionet.info/asn1c

---

## 💡 Key Takeaways

1. **ASN.1** = Schema language (like XSD for XML)
2. **TLV** = Binary format (Tag-Length-Value)
3. **asn1c** = Compiler that generates C code for encoding/decoding
4. **BER/DER** = Most common TLV encodings
5. **Use unber** to inspect/debug binary data
6. **Generated code** handles all TLV complexity for you

---

*Last Updated: 2025-11-06*
*Lab Guide Version: 1.0*