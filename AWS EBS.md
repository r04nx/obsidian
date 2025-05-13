
I have this Python Flask Application as shown in the below  screenshot
![[Pasted image 20250513232704.png]]
when run this is the output
![[Pasted image 20250513232812.png]]
the project can be found at https://www.github.com/r04nx/loraid/webserver

it has a tree structure of as follows
```
├── app.py
├── data.db
├── requirements.txt
├── setup_db.py
├── static
│   ├── script.js
│   └── style.css
├── templates
│   └── index.html
├── transmissions1.csv
├── transmissions.csv
└── transmissions_test_2.csv

3 directories, 10 files
```
now i will run  
eb --version to make sure i have eb cli installed 
![[Pasted image 20250513233053.png]]
```
eb init -p python-3.11 loraid-connect
```

![[Pasted image 20250513233145.png]]

now i just created a environment  via 
```
eb create loraid-env 
```

![[Pasted image 20250513233426.png]]

aws need, the default name as application.py so i renamed my app.py to the application.py
and then i run eb create loraid-env

and env was created successfully

after i run 
eb deploy the application was successfully deployed
![[Pasted image 20250513235758.png]]
and when i run eb status it shows status ready and green as shown in the below screenshot
![[Pasted image 20250513235643.png]] 

when i run eb open it opened the deployed and running application in my default browser as shown in the below screenshot
as shown in the below screenshot the application is fully functional and running 
![[Pasted image 20250514000032.png]]

let us test it by putting some data in, via curl request 
![[Pasted image 20250514000114.png]]
the data is being successfully submitted via exposed api, 
and also the data is being reflected in the frontend application as shown below screenshot
![[Pasted image 20250514000158.png]]