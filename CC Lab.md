
After creating a brand new vm for this practical, i got the terminal access of the vm and run  this  command to clone the dev stack repositry as shown in the below screenshot

![[Pasted image 20250507010154.png]]
after that i cd to devstack and edited the local.conf file using nano as shown in the below screenshot
![[Pasted image 20250507010317.png]]

put in the following details for ADMIN_PASSWORD, DATABASE_PASSWORD etc 
ADMIN_PASSWORD=secret
DATABASE_PASSWORD=SADMIN_PASSWORD
RABBIT_PASSWORD=SADMIN_PASSWORD
SERVICE_PASSWORD=S$ADMIN_PASSWORD
HOST_IP=10.0.2.15
![[Pasted image 20250507010424.png]]
Started the stack.sh execution as shown in the below screenshot
![[Pasted image 20250507010650.png]] and launched the installation

after 20 mins of installation, we get the last output with the dashboard, url as shown in the below screenshot
![[Pasted image 20250507010844.png]] along with the summary

when  i open this url in the web browser i am presented with the following auth page of the openstack as shown in the below screeenshot
![[Pasted image 20250507011003.png]]
We can see the openstack dashboard as shown in the below screenshot
![[Pasted image 20250507011053.png]]
this is the instances section where we can see the VMs in our openstack
![[Pasted image 20250507011141.png]]
as shown below, this is the network topology already designed by openstack by default
![[Pasted image 20250507011219.png]]
now i will pull the ubuntu cloud image via wget command as shown below 
![[Pasted image 20250507011423.png]]
I have successfully imported the image with name demo here
as shown below
![[Pasted image 20250507011623.png]]
now i will go to instances tab, to create a VM from the image we just imported, now click on Launch Instance as shown below
![[Pasted image 20250507011810.png]]
after filling necessary information i will, click on next
![[Pasted image 20250507011904.png]]
select the boot source, and and then volume size as shown below
![[Pasted image 20250507011946.png]]
and then select the instance type like m1.nano , m1.micro, m1.tiny etc.

![[Pasted image 20250507012019.png]]
