I have installed the eb command with the following command,
```bash
python3 -m pip install --user awsebcli
```
![[Pasted image 20250409094208.png]]



Then i run eb init command and comppleted all the prompts as shown below:
![[Pasted image 20250409094323.png]]

as my application is nextjs + prisma + sqlite + nextjs routes

I had mistakenly delted the default vpc in aws, when i run aws nuke last time, that is why the above command fialed. as shown in the below screenshot
![[Pasted image 20250409094551.png]]
THen i created the Aws ec2 create-default-vpc
and this was the output
![[Pasted image 20250409094635.png]]

