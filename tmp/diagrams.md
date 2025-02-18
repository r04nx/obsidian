# 📊 Exam Central System Documentation

## 🏗 System Architecture Overview

```mermaid
graph TB
    subgraph Cloud Infrastructure
        API[API Gateway]
        WS[Web Server]
        DB[(Database)]
        AUTH[Auth Service]
        CACHE[Redis Cache]
    end
    
    subgraph Client Layer
        WEB[Web Interface]
        MOB[Mobile App]
    end
    
    subgraph Services
        EXAM[Exam Service]
        USER[User Service]
        RESULT[Result Service]
        NOTIFY[Notification Service]
    end
    
    WEB --> API
    MOB --> API
    API --> AUTH
    API --> WS
    WS --> EXAM
    WS --> USER
    WS --> RESULT
    WS --> NOTIFY
    EXAM --> DB
    USER --> DB
    RESULT --> DB
    NOTIFY --> CACHE
```

## 🔄 Data Flow Diagram

```mermaid
flowchart TD
    A[Student] -->|Login| B(Authentication)
    B -->|Verify| C{Auth Valid?}
    C -->|Yes| D[Dashboard]
    C -->|No| E[Login Error]
    D -->|Select| F[Exam Portal]
    F -->|Start| G[Active Exam]
    G -->|Submit| H[Processing]
    H -->|Store| I[(Database)]
    H -->|Generate| J[Results]
    J -->|Notify| K[Email Service]
    J -->|Display| L[Result Portal]
```

## 🔄 Module Interaction Workflow

```mermaid
sequenceDiagram
    participant U as User
    participant FE as Frontend
    participant API as API Gateway
    participant AS as Auth Service
    participant ES as Exam Service
    participant DB as Database
    
    U->>FE: Access System
    FE->>API: Request Access
    API->>AS: Validate User
    AS->>DB: Check Credentials
    DB-->>AS: User Valid
    AS-->>API: Auth Token
    API-->>FE: Session Established
    U->>FE: Request Exam
    FE->>API: Get Exam Data
    API->>ES: Fetch Exam
    ES->>DB: Query Exam
    DB-->>ES: Exam Data
    ES-->>API: Exam Details
    API-->>FE: Display Exam
```

## 👤 User Journey Flows

```mermaid
journey
    title Exam Taking Process
    section Login
    Access Portal: 5: User
    Enter Credentials: 3: User
    Verify Identity: 3: System
    section Exam
    View Available Exams: 5: User
    Select Exam: 4: User
    Start Exam: 5: User, System
    Answer Questions: 3: User
    Submit Exam: 5: User, System
    section Results
    Process Submission: 3: System
    Generate Result: 4: System
    View Result: 5: User
```

## 🔒 Security Flow

```mermaid
stateDiagram-v2
    [*] --> Login
    Login --> Authentication
    Authentication --> MFA
    MFA --> SessionCreation
    SessionCreation --> AuthorizedAccess
    AuthorizedAccess --> ExamAccess
    ExamAccess --> Proctoring
    Proctoring --> SecurityChecks
    SecurityChecks --> MonitoringActive
    MonitoringActive --> ExamCompletion
    ExamCompletion --> [*]
    
    state SecurityChecks {
        Browser_Check --> Screen_Record
        Screen_Record --> Webcam_Check
        Webcam_Check --> System_Check
    }
```

## 📊 Database Relationships

```mermaid
erDiagram
    USERS ||--o{ EXAMS : takes
    USERS {
        string user_id PK
        string username
        string email
        string password_hash
        string role
    }
    EXAMS ||--|{ QUESTIONS : contains
    EXAMS {
        string exam_id PK
        string title
        datetime start_time
        datetime end_time
        int duration
    }
    QUESTIONS ||--o{ ANSWERS : has
    QUESTIONS {
        string question_id PK
        string exam_id FK
        string content
        int marks
        string type
    }
    ANSWERS {
        string answer_id PK
        string question_id FK
        string content
        boolean is_correct
    }
    RESULTS ||--|| EXAMS : generates
    RESULTS {
        string result_id PK
        string user_id FK
        string exam_id FK
        float score
        datetime submission_time
    }
```

