
We will use Wireguard for setting up a Client 

We will use the AWS CLient VPN fully managed VPN service provided by AWS

our use case will be, Onprem application will connect to the Database on cloud will connect via Client VPN

let us begin 
to simulte the on prem application we will use the Notu a note taking app in the python flask developed and designed by me which will be using the postgres database running in the aws cloud on ec2 and we will establish a vpn connection between these microservice

the following are some screenshots of the application 


let us check if there are any available vpc in my aws account 
there are none as shown in the following screenshot when i runthe commnd
aws ec2 describe-vpcs
![[Pasted image 20250519040920.png]]

Now i have created a VPC with the following command 
![[Pasted image 20250519041303.png]]

Now i have created a subnet in the availability zone ap-south-1a with the following command
![[Pasted image 20250519041354.png]]

Now i have created a Internet Gateway 
![[Pasted image 20250519041425.png]]
now connect or attach the internet gateway with the newly created vpc
![[Pasted image 20250519041512.png]]

let us check the default routing table for this setup we have created 
![[Pasted image 20250519041601.png]]

now let me create a route to the internet gateway 
![[Pasted image 20250519041733.png]]
now let us make sure that the subnet is associated with our routing table 
![[Pasted image 20250519041848.png]]

Now let us create a Security Group for the VPN 
![[Pasted image 20250519041932.png]]

now let us put the rule for the security group to allow ingress traffic 
![[Pasted image 20250519042028.png]]
now let us create the security group for the vpn endpoints
![[Pasted image 20250519042336.png]]
now let us do the same for this sg as well but instead of allowing all traffic let us put in rule to allow only ssh 22 traffic 
![[Pasted image 20250519042611.png]]

now let us modify the subnet to get the public ip up on launch 
![[Pasted image 20250519042715.png]]

now let us create the ec2 instance with the Amzon Linux Machine id with the existing key value pairs and in the subnet and vpc we created previously and associate it with the security group we just created 
![[Pasted image 20250519042802.png]]

and now when i do describe instances it shows me the successfull output
![[Pasted image 20250519042930.png]]
Now what we have done till now
1. Created a VPC with CIDR block 10.0.0.0/16

2. Created a subnet with CIDR 10.0.1.0/24 in the ap-south-1a availability zone
3. Created and attached an Internet Gateway to the VPC

4. Updated the route table to allow internet access

5. Created security groups for the instance

6. Generated an SSH key pair (saved as my-vpc-key.pem in your current directory)
7. Launched an Amazon Linux 2 t2.micro instance in the subnet

My EC2 instance is now running with these details:
¢ Instance ID: i-02c4ca057df492d7c
e Public IP: 13.126.132.2
¢ Private IP: 10.0.1.28

You can connect to your instance using SSH:

 ssh -i my-vpc-key.pem ec2-user@13.126.132.2

let us clone this repo for generating the certificates and keys required for the client vpn setup in the AWS
![[Pasted image 20250519045555.png]]
then run the following commands  
![[Pasted image 20250519045628.png]]
![[Pasted image 20250519045657.png]]

![[Pasted image 20250519045723.png]]

type yes wherever necessary
![[Pasted image 20250519045759.png]]

now make the directory to store all the creds related files

copyall the important files in that dir
![[Pasted image 20250519045915.png]]
then run the following command
![[Pasted image 20250519045938.png]]







