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