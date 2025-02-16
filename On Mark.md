**Todo**
- [ ] Yash friend App 
- [ ] Lora Mobile App (Final Year)
- [ ] Hackathon Registration for SGGS
- [ ] College Main Website Development
- [ ] Discuss the Board and Dashboard Design
- [ ] VPC creation in  2 Labs
- [ ] Palo alto book reading for container sec
- [ ] Self Hosted Docker Registry
- [ ] Azure & AWS CI/CD Pipeline


```mermaid
graph TB
    subgraph Network Infrastructure
        subgraph HR_Network[HR & Executive Network 10.1.1.0/24]
            hr_system1[hr_system1<br/>Kali Linux<br/>10.1.1.4]
            hr_system2[hr_system2<br/>Kali Linux<br/>10.1.1.6]
            hr_ubuntu1[hr_ubuntu1<br/>Ubuntu 18.04<br/>10.1.1.11]
            hr_windows[hr_windows<br/>Windows 10<br/>10.1.1.15]
        end

        subgraph Marketing_Network[Marketing Network 10.1.2.0/24]
            marketing_windows1[marketing_windows1<br/>Windows 10<br/>10.1.2.8]
            marketing_ubuntu[marketing_ubuntu<br/>Ubuntu 18.04<br/>10.1.2.9]
        end

        subgraph IT_Network[IT Network 10.1.3.0/24]
            it_ubuntu1[it_ubuntu1<br/>Ubuntu 18.04<br/>10.1.3.8]
            it_kali1[it_kali1<br/>Kali Linux<br/>10.1.3.11]
        end

        subgraph DMZ_Public[DMZ Public Subnet 10.1.4.0/24]
            honeypot[honeypot<br/>Ubuntu 18.04<br/>10.1.4.10]
            webserver[webserver<br/>Ubuntu 18.04<br/>10.1.4.16]
        end

        subgraph DMZ_Private[DMZ Private Subnet 10.1.5.0/24]
            sftp_server[sftp_server<br/>Ubuntu 18.04<br/>10.1.5.7]
            db_server[db_server<br/>Ubuntu 18.04<br/>10.1.5.8]
        end

        firewall{Firewall}
        ids[Snort IDS]

        %% Connect networks to firewall
        HR_Network --> firewall
        Marketing_Network --> firewall
        IT_Network --> firewall
        DMZ_Public --> firewall
        DMZ_Private --> firewall

        %% Connect IDS
        HR_Network --> ids
        Marketing_Network --> ids
        IT_Network --> ids

        style HR_Network fill:#f9f,stroke:#333,stroke-width:2px
        style Marketing_Network fill:#bbf,stroke:#333,stroke-width:2px
        style IT_Network fill:#fbf,stroke:#333,stroke-width:2px
        style DMZ_Public fill:#fbb,stroke:#333,stroke-width:2px
        style DMZ_Private fill:#bfb,stroke:#333,stroke-width:2px
        
        style firewall fill:#f96,stroke:#333,stroke-width:4px
        style ids fill:#ff9,stroke:#333,stroke-width:2px
end
```


```mermaid
flowchart TD
    Internet((Internet))

    subgraph SECURITY["Security Infrastructure"]
        FW[Firewall\nSquid Proxy]
        IDS[IDS/IPS\nSecurity Onion]
    end

    subgraph PUBLIC_DMZ["Public DMZ (10.1.4.0/24)"]
        WEB[Public Web Server\nNGINX\n10.1.4.10]
        MAIL[Mail Server\nPostfix/Dovecot\n10.1.4.16]
    end

    subgraph PRIVATE_DMZ["Private DMZ (10.1.5.0/24)"]
        LDAP[OpenLDAP\n10.1.5.7\nAdmin: Ldap@dm1n2024!]
        MAIN_DB[(Main MySQL DB\n10.1.5.8\nAdmin: Db@dm1n2024!)]
    end

    subgraph HR["HR Network (10.1.1.0/24)"]
        HR_PORTAL[HR Portal\nWordPress\n10.1.1.4\nAdmin: Hr@dm1n2024!]
        HR_DB[(HR MySQL DB\n10.1.1.5)]
        HR_FTP[FTP Server\n10.1.1.6\nUser: hr_ftp\nPass: HrFtp@2024!]
    end

    subgraph MARKETING["Marketing Network (10.1.2.0/24)"]
        MKT_CMS[Marketing CMS\nDrupal\n10.1.2.8\nAdmin: Mkt@dm1n2024!]
        MKT_DB[(Marketing PostgreSQL\n10.1.2.9)]
    end

    subgraph IT["IT Network (10.1.3.0/24)"]
        GRAFANA[Grafana Monitoring\n10.1.3.8\nAdmin: It@dm1n2024!]
        JENKINS[Jenkins CI/CD\n10.1.3.11\nAdmin: Jnk@dm1n2024!]
    end

    %% External connections
    Internet <--> FW
    FW <--> WEB
    FW <--> MAIL

    %% Security monitoring
    FW --> IDS
    IDS --> PUBLIC_DMZ
    IDS --> PRIVATE_DMZ
    IDS --> HR
    IDS --> MARKETING
    IDS --> IT

    %% Internal connections
    FW --> HR_PORTAL
    FW --> MKT_CMS
    FW --> GRAFANA
    FW --> JENKINS

    %% Database connections
    HR_PORTAL --> HR_DB
    MKT_CMS --> MKT_DB
    HR_PORTAL -.-> MAIN_DB
    MKT_CMS -.-> MAIN_DB

    %% Authentication
    HR_PORTAL --> LDAP
    MKT_CMS --> LDAP
    GRAFANA --> LDAP
    JENKINS --> LDAP

    %% File server connections
    HR_PORTAL --> HR_FTP

    classDef default fill:#fff,stroke:#333,stroke-width:2px;
    classDef internet fill:#f9f,stroke:#333,stroke-width:4px;
    classDef public fill:#ff9,stroke:#333,stroke-width:2px;
    classDef private fill:#9f9,stroke:#333,stroke-width:2px;
    classDef hr fill:#99f,stroke:#333,stroke-width:2px;
    classDef marketing fill:#f99,stroke:#333,stroke-width:2px;
    classDef it fill:#9ff,stroke:#333,stroke-width:2px;
    classDef security fill:#999,stroke:#333,stroke-width:2px;
    classDef database fill:#fff,stroke:#333,stroke-width:4px;

    class Internet internet;
    class WEB,MAIL public;
    class LDAP,MAIN_DB private;
    class HR_PORTAL,HR_DB,HR_FTP hr;
    class MKT_CMS,MKT_DB marketing;
    class GRAFANA,JENKINS it;
    class FW,IDS security;
    class HR_DB,MKT_DB,MAIN_DB database;
```


# NEW ONE

```mermaid

flowchart LR
    subgraph Public-DMZ["Public DMZ (10.1.4.0/24)"]
        direction TB
        web[Public Web\nNGINX\n10.1.4.10]
        mail[Mail Server\n10.1.4.16\nmail:M@il@dm1n2024!]
    end

    subgraph Private-DMZ["Private DMZ (10.1.5.0/24)"]
        direction TB
        ldap[OpenLDAP\n10.1.5.7\nLdap@dm1n2024!]
        maindb[(Main MySQL\n10.1.5.8\ndb_admin:Db@dm1n2024!)]
    end

    subgraph HR["HR Network (10.1.1.0/24)"]
        direction TB
        hrportal[WordPress Portal\n10.1.1.4\nhr_admin:Hr@dm1n2024!]
        hrdb[(HR MySQL\n10.1.1.5)]
        hrftp[FTP Server\n10.1.1.6\nhr_ftp:HrFtp@2024!]
    end

    subgraph Marketing["Marketing Network (10.1.2.0/24)"]
        direction TB
        mktcms[Drupal CMS\n10.1.2.8\nmarketing_admin:Mkt@dm1n2024!]
        mktdb[(PostgreSQL\n10.1.2.9)]
    end

    subgraph IT["IT Network (10.1.3.0/24)"]
        direction TB
        grafana[Grafana\n10.1.3.8\nit_admin:It@dm1n2024!]
        jenkins[Jenkins\n10.1.3.11\njenkins_admin:Jnk@dm1n2024!]
        portainer[Portainer\n10.1.3.12]
    end

    %% Database connections
    hrportal --> hrdb
    mktcms --> mktdb
    hrportal -.-> maindb
    mktcms -.-> maindb

    %% Authentication flows
    hrportal --> ldap
    mktcms --> ldap
    grafana --> ldap
    jenkins --> ldap
    portainer --> ldap

    %% File server connections
    hrportal --> hrftp

    %% Styling
    classDef public fill:#ffccd5,stroke:#495057,stroke-width:2px;
    classDef private fill:#caf0f8,stroke:#495057,stroke-width:2px;
    classDef hr fill:#dee2ff,stroke:#495057,stroke-width:2px;
    classDef marketing fill:#ffd7ba,stroke:#495057,stroke-width:2px;
    classDef it fill:#c1fba4,stroke:#495057,stroke-width:2px;
    classDef database fill:#f8f9fa,stroke:#495057,stroke-width:4px,stroke-dasharray: 5 5;

    class web,mail public;
    class ldap,maindb private;
    class hrportal,hrdb,hrftp hr;
    class mktcms,mktdb marketing;
    class grafana,jenkins,portainer it;
    class hrdb,mktdb,maindb database;
```



# Next V1

```mermaid
graph TD
    %% Define Networks
    subgraph HR_Network["HR Network (10.1.1.0/24)"]
        HRP["hr_portal - 10.1.1.4<br/>DB: hr_db<br/>User: hr_admin<br/>Pass: Hr@dm1n2024!"]
        HRDB["hr_db - 10.1.1.5<br/>Root Pass: Hr@dm1n2024!"]
        HRFS["hr_file_server - 10.1.1.6<br/>User: hr_ftp<br/>Pass: HrFtp@2024!"]
        HRP --> HRDB
        HRFS --> HRP
    end

    subgraph Marketing_Network["Marketing Network (10.1.2.0/24)"]
        MKTCMS["marketing_cms - 10.1.2.8<br/>DB: marketing_db<br/>User: marketing_admin<br/>Pass: Mkt@dm1n2024!"]
        MKTDB["marketing_db - 10.1.2.9<br/>Root Pass: Mkt@dm1n2024!"]
        MKTCMS --> MKTDB
    end

    subgraph IT_Network["IT Network (10.1.3.0/24)"]
        ITM["it_monitoring - 10.1.3.8<br/>User: it_admin<br/>Pass: It@dm1n2024!"]
        JKS["jenkins_server - 10.1.3.11<br/>User: jenkins_admin<br/>Pass: Jnk@dm1n2024!"]
        PTN["portainer - 10.1.3.12"]
    end

    subgraph Public_Subnet["Public Subnet (10.1.4.0/24)"]
        PUBW["public_web - 10.1.4.10"]
        MAIL["mail_server - 10.1.4.16<br/>User: admin@targetorg.local<br/>Pass: M@il@dm1n2024!"]
        HNP["honeypot - 10.1.4.20"]
    end

    subgraph Private_Subnet["Private Subnet (10.1.5.0/24)"]
        LDAP["internal_ldap - 10.1.5.7<br/>Org: TargetORG<br/>Domain: targetorg.local<br/>Pass: Ldap@dm1n2024!"]
        MAINDB["main_db - 10.1.5.8<br/>User: db_admin<br/>Pass: Db@dm1n2024!"]
        INTFTP["internal_ftp - 10.1.5.9<br/>User: internal_ftp<br/>Pass: IntFtp@2024!"]
        RSYSLOG["rsyslog_server - 10.1.5.10"]
    end

    %% External Connections
    Internet(("Internet"))
    PUBW --> Internet
    MAIL --> Internet
    HNP --> Internet

    %% Service Dependencies
    ITM --> JKS
    JKS --> HRP
    JKS --> MKTCMS
    PTN --> LDAP

    %% Logging
    HRP -.->|logs| RSYSLOG
    MKTCMS -.->|logs| RSYSLOG
    JKS -.->|logs| RSYSLOG
    MAIL -.->|logs| RSYSLOG
    PUBW -.->|logs| RSYSLOG

    %% Authentication
    LDAP --> MAINDB
    HRP --> LDAP
    MKTCMS --> LDAP
    ITM --> LDAP
    JKS --> LDAP
    PTN --> LDAP
    INTFTP --> LDAP

    %% File Storage
    HRP --> INTFTP
    MKTCMS --> INTFTP

    %% Styling
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef network fill:#e6f3ff,stroke:#333,stroke-width:2px
    classDef logging stroke-dasharray: 5 5
    
    class HR_Network,Marketing_Network,IT_Network,Public_Subnet,Private_Subnet network
    class RSYSLOG logging
```

```mermaid
		HRP["hr_portal - 10.1.1.4<br/>DB: hr_db<br/>User: hr_admin<br/>Pass: Hr@dm1n2024!"]
        HRDB["hr_db - 10.1.1.5<br/>Root Pass: Hr@dm1n2024!"]
        HRFS["hr_file_server - 10.1.1.6<br/>User: hr_ftp<br/>Pass: HrFtp@2024!"]
        HRP --> HRDB
        HRFS --> HRP
    end

    subgraph Marketing_Network["Marketing Network (10.1.2.0/24)"]
        MKTCMS["marketing_cms - 10.1.2.8<br/>DB: marketing_db<br/>User: marketing_admin<br/>Pass: Mkt@dm1n2024!"]
        MKTDB["marketing_db - 10.1.2.9<br/>Root Pass: Mkt@dm1n2024!"]
        MKTCMS --> MKTDB
    end

    subgraph IT_Network["IT Network (10.1.3.0/24)"]
        ITM["it_monitoring - 10.1.3.8<br/>User: it_admin<br/>Pass: It@dm1n2024!"]
        JKS["jenkins_server - 10.1.3.11<br/>User: jenkins_admin<br/>Pass: Jnk@dm1n2024!"]
        PTN["portainer - 10.1.3.12"]
    end

    subgraph Public_Subnet["Public Subnet (10.1.4.0/24)"]
        PUBW["public_web - 10.1.4.10"]
        MAIL["mail_server - 10.1.4.16<br/>User: admin@targetorg.local<br/>Pass: M@il@dm1n2024!"]
        HNP["honeypot - 10.1.4.20"]
    end

    subgraph Private_Subnet["Private Subnet (10.1.5.0/24)"]
        LDAP["internal_ldap - 10.1.5.7<br/>Org: TargetORG<br/>Domain: targetorg.local<br/>Pass: Ldap@dm1n2024!"]
        MAINDB["main_db - 10.1.5.8<br/>User: db_admin<br/>Pass: Db@dm1n2024!"]
        INTFTP["internal_ftp - 10.1.5.9<br/>User: internal_ftp<br/>Pass: IntFtp@2024!"]
        RSYSLOG["rsyslog_server - 10.1.5.10"]
    end

    %% External Connections
    Internet(("Internet"))
    PUBW --> Internet
    MAIL --> Internet
    HNP --> Internet

    %% Service Dependencies
    ITM --> JKS
    JKS --> HRP
    JKS --> MKTCMS
    PTN --> LDAP

    %% Logging
    HRP -.->|logs| RSYSLOG
    MKTCMS -.->|logs| RSYSLOG
    JKS -.->|logs| RSYSLOG
    MAIL -.->|logs| RSYSLOG
    PUBW -.->|logs| RSYSLOG

    %% Authentication
    LDAP --> MAINDB
    HRP --> LDAP
    MKTCMS --> LDAP
    ITM --> LDAP
    JKS --> LDAP
    PTN --> LDAP
    INTFTP --> LDAP

    %% File Storage
    HRP --> INTFTP
    MKTCMS --> INTFTP

    %% Styling
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef network fill:#e6f3ff,stroke:#333,stroke-width:2px
    classDef logging stroke-dasharray: 5 5
    
    class HR_Network,Marketing_Network,IT_Network,Public_Subnet,Private_Subnet network
    class RSYSLOG logging
        HRP["hr_portal - 10.1.1.4<br/>DB: hr_db<br/>User: hr_admin<br/>Pass: Hr@dm1n2024!"]
        HRDB["hr_db - 10.1.1.5<br/>Root Pass: Hr@dm1n2024!"]
        HRFS["hr_file_server - 10.1.1.6<br/>User: hr_ftp<br/>Pass: HrFtp@2024!"]
        HRP --> HRDB
        HRFS --> HRP
    end

    subgraph Marketing_Network["Marketing Network (10.1.2.0/24)"]
        MKTCMS["marketing_cms - 10.1.2.8<br/>DB: marketing_db<br/>User: marketing_admin<br/>Pass: Mkt@dm1n2024!"]
        MKTDB["marketing_db - 10.1.2.9<br/>Root Pass: Mkt@dm1n2024!"]
        MKTCMS --> MKTDB
    end

    subgraph IT_Network["IT Network (10.1.3.0/24)"]
        ITM["it_monitoring - 10.1.3.8<br/>User: it_admin<br/>Pass: It@dm1n2024!"]
        JKS["jenkins_server - 10.1.3.11<br/>User: jenkins_admin<br/>Pass: Jnk@dm1n2024!"]
        PTN["portainer - 10.1.3.12"]
    end

    subgraph Public_Subnet["Public Subnet (10.1.4.0/24)"]
        PUBW["public_web - 10.1.4.10"]
        MAIL["mail_server - 10.1.4.16<br/>User: admin@targetorg.local<br/>Pass: M@il@dm1n2024!"]
        HNP["honeypot - 10.1.4.20"]
    end

    subgraph Private_Subnet["Private Subnet (10.1.5.0/24)"]
        LDAP["internal_ldap - 10.1.5.7<br/>Org: TargetORG<br/>Domain: targetorg.local<br/>Pass: Ldap@dm1n2024!"]
        MAINDB["main_db - 10.1.5.8<br/>User: db_admin<br/>Pass: Db@dm1n2024!"]
    end

    %% External Connections
    Internet(("Internet"))
    PUBW --> Internet
    MAIL --> Internet
    HNP --> Internet

    %% IT Services Dependencies
    ITM --> JKS
    JKS --> HRP
    JKS --> MKTCMS
    PTN --> LDAP

    %% Authentication
    LDAP --> MAINDB

    %% Styling
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef network fill:#e6f3ff,stroke:#333,stroke-width:2px
    
    class HR_Network,Marketing_Network,IT_Network,Public_Subnet,Private_Subnet network
```
