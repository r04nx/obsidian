1. acessing mobile screen remotely 
Following is the scrreenshot for installing the scrcpy package via winget

 if winget is not found in your windows machine then, use this https://learn.microsoft.com/en-us/windows/package-manager/winget/

![[Pasted image 20250917185009.png]]
   *incase of ubuntu system, simply run the following command*
```bash
sudo apt update && sudo apt install scrcpy
```

Now to access the *adb cli* install the adb for windows by this https://developer.android.com/tools/releases/platform-tools
and extract the zip file and add it to your environment variable to access it everyewhere
![[Pasted image 20250917185533.png]]AS SHOWN ABOVE SCREEN CAPTURE
make sure the adb is successfully installed by running adb in the new terminal
![[Pasted image 20250917185654.png]]
Now go to settings>about phone>find the option called build numberr version and tap it multiple times, so that you see enable developer option
and then go to the developer option
![[becoming-a-developer-in-android-13-1.webp]]

and then go to developers option and enable the USB Debugging
![[unnamed.jpg]]

now that we have evrything in place, adb installed, scrcpy installed, developer mode enabled, usb debugging enabled, 

now connect your phone to PC via USB cable
 as shown below
![[use-usb-cable-to-connect-phone-with-pc-1.png]]

now in the new terminal run the following
![[Pasted image 20250917190439.png]]
and allow the UAC prompt 
run the adb devices 
![[Pasted image 20250917190658.png]]
to remove this unauthorized, check the android screen and then press allow
then run the scrcpy command in the terminal
![[Pasted image 20250917190914.png]]

now you can control your phone screen from the wizard

PART B
Now we going to connect to the adb wirelessly, without the USB cable

Connect your PC and Mobile phone to the same wifi network
now although we can have the Phone's wifi ip address from the settings, 
but we going to install a Linux Emulator in the android phone, for also further few steps in the practical

for that navigate to the Playstore and search for Termux and install it 
as shown in the following screenshot

![[unnamed 1.jpg]]

after successfull installation open the app
![[unnamed-1.jpg]]
You will find yourself in the Linux Emulator, it is your very own linux machine inside a phone

type in the follwing command to get the ip address of your phone
```bash
ifconfig
```

![[unnamed 2.jpg]]

Now coming back to the PC terminal, get the ip addr of your phone and ping test
for the ip in this case here the ip is `10.10.51.71`
run the following command to ensure your pc can reach to the mobile phone 
```bash
ping 10.10.51.71
```
you should recive the ping response as follows
![[Pasted image 20250917192119.png]]

now after that, 
come back to your phone and search for wireless debugging in the Developer Section
as shown in the below screen shot
![[Pasted image 20250917192809.png]]
press allow to make connection on this wifi network
![[unnamed 3.jpg]]
after successfull enabling the wireless adb debugging, you need to click and open the wireless debugging as shown in the below screenshot, note the Port mentioned ![[unnamed-1 1.jpg]]
![[Pasted image 20250917193026.png]]


and now replace that port in the following command and run this in the PC terminal
```bash
adb connect <ip addr>:<port>
```
in our case the command will be 
```bash
adb connect 10.10.51.71:34605
```
after running the command you should see the output like the following
![[Pasted image 20250917193250.png]]
after the successfull connection, you should recieve a notification in your android phone as follows
![[unnamed 4.jpg]]

now that we have connected adb wirelessly you should be able to connect the screencast via scrcpy , as the following screenshot
![[Pasted image 20250917193524.png]]
now run the command `adb shell` and you should be able to access your android shell
as shown in the following screenshot
![[Pasted image 20250917193744.png]]

Things you can do with this 
File Management and App Control

- **Install/Uninstall Apps**:
    
    Use `adb install <path_to_apk>` to install an application from your computer and `adb uninstall <package_name>` to remove it. 
    

- **Remove Bloatware**:
    
    Remove unwanted pre-installed apps that can't be uninstalled through standard methods. 
    

- **Push/Pull Files**:
    
    Transfer files between your computer and device using `adb push <local_path> <remote_path>` and `adb pull <remote_path> [<local_path>]`.


Device Monitoring and Information

- **Capture Screenshots/Recordings**:
    
    Take screenshots with `adb shell screencap -p /sdcard/screenshot.png` and record your screen with `adb shell screenrecord /sdcard/record.mp4`. 
    

- **View Logs and Bug Reports**:
    
    Monitor real-time device logs with `adb logcat` or generate a comprehensive bug report with `adb bugreport`. 
    

- **Inspect System Services**:
    
    Get detailed diagnostic output for all running system services by calling `dumpsys` within the ADB shell. 
    

- **List Installed Packages**:
    
    See a list of all installed applications on the device using `adb shell pm list packages`. 
    

Device Control and System Functions

- **Reboot Device**:
    
    Reboot your phone into recovery or fastboot mode with `adb reboot recovery` or `adb reboot fastboot`. 
    

- **Simulate Inputs**:
    
    Automate tasks by scripting touch and keyboard inputs to simulate user actions, such as logging in. 
    

- **Create Backups**:
    
    Perform a full backup of your phone and its settings with `adb backup`. 
    

- **Open URLs**:
    
    Launch a specific URL in the device's default browser using `adb shell am start -a android.intent.action.VIEW -d <URL>`.

as shown in the below screenshot I have opened my website on android in default browser via adb shell by running this command
![[Pasted image 20250917194044.png]]

To send the SMS use the following command
```bash
  adb shell "am start -a android.intent.action.SENDTO -d sms:PHONE_NUMBER --es sms_body 'YOUR_MESSAGE'; sleep 2; input keyevent 22;
  input keyevent 66
```

To Start a call to the recipient number use the following command
```bash
adb shell "am start -a android.intent.action.CALL -d tel:+919028992643; sleep 3;
```

this is the command to see the logs in realtime from your android

```bash
adb logcat
```

mention more adb cool commands that 

Now enough about accessing and controlling Mobile phone via PC

now we will control the PC by Mobile 

