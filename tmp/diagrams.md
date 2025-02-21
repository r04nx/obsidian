---
share_link: https://share.note.sx/vmujrng8#+tNth4KijjFCUnm7X3SY4zUXebt+qaCqekztI+6vDBc
share_updated: 2025-02-18T23:21:32+05:30
---
# 📊 Exam Central System Documentation

## 🏗 System Architecture Overview

```mermaid
graph TB
    subgraph Kubernetes Cluster
        subgraph Infrastructure
            LB[NGINX Load Balancer]
            API[API Gateway]
            CACHE[(Redis Cache)]
            DB[(PostgreSQL Database)]
        end
        
        subgraph Client Applications
            WEB[React TypeScript SPA]
            MOB[React Native Mobile]
        end
        
        subgraph Microservices
            WS[Flask Web Server]
            AUTH[JWT Auth Service]
            EXAM[Exam Service]
            USER[User Service]
            RESULT[Result Service]
            NOTIFY[Notification Service]
        end
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
flowchart LR
    A[Student Browser] -->|HTTPS| B(NGINX Load Balancer)
    B -->|Route| C[React Frontend]
    C -->|API Call| D{JWT Auth}
    D -->|Invalid| E[401 Unauthorized]
    D -->|Valid| F[React Dashboard]
    F -->|REST API| G[Flask Backend]
    G -->|Query| H[(PostgreSQL)]
    G -->|Cache| I[(Redis)]
    H -->|Data| J[Exam Service]
    J -->|Events| K[Message Queue]
    K -->|Process| L[Result Generation]
    L -->|Store| H
    L -->|Cache| I
```

## 🔄 Module Interaction Workflow

```mermaid
sequenceDiagram
    participant U as User Browser
    participant LB as NGINX LB
    participant FE as React Frontend
    participant API as Flask API
    participant AS as JWT Auth
    participant ES as Exam Service
    participant REDIS as Redis Cache
    participant DB as PostgreSQL
    
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
        uuid user_id PK
        varchar username
        varchar email
        varchar password_hash "bcrypt"
        varchar role
        timestamp created_at
        timestamp updated_at
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

## 👥 Use Case Diagram

```mermaid
%%{init: { 'theme': 'base', 'themeVariables': { 'primaryColor': '#FFA500', 'textColor': '#000000', 'lineColor': '#000000' } } }%%
graph LR
    subgraph Actors
        Student((Student))
        Faculty((Faculty))
        Admin((Admin))
        System((System))
    end

    subgraph Exam Management
        CreateExam[Create Exam]
        ManageQuestions[Manage Questions]
        ScheduleExam[Schedule Exam]
        ModifyExam[Modify Exam]
    end

    subgraph Student Activities
        TakeExam[Take Exam]
        ViewResults[View Results]
        SubmitAnswers[Submit Answers]
        ViewSchedule[View Exam Schedule]
    end

    subgraph Result Processing
        GenerateResults[Generate Results]
        AnalyzePerformance[Analyze Performance]
        PublishResults[Publish Results]
    end

    subgraph System Operations
        Authentication[Authentication]
        Authorization[Authorization]
        Proctoring[Proctoring]
        Monitoring[Monitoring]
    end

    Student --> Authentication
    Student --> TakeExam
    Student --> ViewResults
    Student --> SubmitAnswers
    Student --> ViewSchedule

    Faculty --> Authentication
    Faculty --> CreateExam
    Faculty --> ManageQuestions
    Faculty --> ModifyExam
    Faculty --> PublishResults
    Faculty --> AnalyzePerformance

    Admin --> Authentication
    Admin --> ScheduleExam
    Admin --> GenerateResults
    Admin --> Monitoring

    System --> Proctoring
    System --> Authorization
    System --> GenerateResults
    System --> Monitoring
```