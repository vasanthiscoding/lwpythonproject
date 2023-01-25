import os
import getpass

os.system("tput setaf 3")

print("\t\t\t Hey Welcome To My TUI Thats Makes Life Simple")

os.system("tput setaf 7")
print("\t\t\t---------------------------------------")

passward = getpass.getpass("Enter the passward :")

apass = "lw"

if passward != apass:
    print("auth incorrect")
    exit()

print("where i want to run the command (local/remote) :" , end="" )
location=input()
print(location)

if location== "remote":
	remoteIP= input("Enter the IP :")
	
	print("""press 1: to see date
	press 2: to check cal
	press 3: config the web server
	press 4: to create a user
	press 5: to create a file 
	press 6: to setup  n/w
	press 7: to exit
	""")

while True:
	print("Enter your choice :" ,  end="" )

	ch=input()

	print(ch)

	if location =="local":
	    if int(ch) == 1:
		    os.system("date") 
	    elif int(ch) == 2:
		    os.system("cal") 
	    elif int(ch) == 3:
		    os.system("yum install httpd") 
	    elif int(ch) == 4:
		    print(" Enter the user name :" ,end="")
		    create_user=input()
		    os.system("useradd {}".format(create_user))
	    elif int(ch) == 5:
		    os.system("date") 
	    elif int(ch) == 6:
		    os.system("date") 
	    elif int(ch) == 7:
		    exit()
	    else:
		    print("option not supported")

	elif location == "remote":
            if int(ch) == 1:
                    os.system("ssh {0} date" .format(remoteIP)) 
            elif int(ch) == 2:
                    os.system("ssh {0} cal" .format(remoteIP)) 
            elif int(ch) == 3:
                    os.system("yum install httpd") 
            elif int(ch) == 4:
                    print(" Enter the user name :" ,end="")
                    create_user=input()
                    os.system("ssh {0} useradd {1}".format(remoteIP, create_user))
            elif int(ch) == 5:
                    os.system("date") 
            elif int(ch) == 6:
                    os.system("date")
            elif int(ch) == 7:
                    exit() 
            else:
                    print("option not supported") 

	
else:
        print("location doesn't exist")
                
