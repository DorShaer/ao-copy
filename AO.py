#HI! 
import requests
import json 
from sys import stdout as terminal
from time import sleep
import itertools
from threading import Thread
import pyfiglet 
import time

## Banner 
ascii_banner = pyfiglet.figlet_format("BrightSec")
print(ascii_banner)
print("[+] Copy and paste Authentication Objects from one user to the other!\n\n")


## The source API Key where we are copying the AO from  
SOURCE_API_KEY = input("Please enter your API Key: ")
if SOURCE_API_KEY == "":
	print("Error: No API KEY specified\n[+] Exiting... ")
	exit()
else:
	SOURCE_API_KEY = SOURCE_API_KEY

	## The Authentication Object ID shown in the "Authentications" tab
AO_ID = input("Please enter the Authentication Object ID which you want to copy: ")
if AO_ID == "":
	print("Error: No Authentication Object specified\n[+] Exiting...")
	exit()
else:
	AO_ID = AO_ID

## The Neuralegion Base Api URL
BASE_URL = 'https://app.neuralegion.com/api/v1/auth-objects/' + AO_ID

if SOURCE_API_KEY == "":
	print("Error: No API Key specified\n[+] Exiting... ")
	exit()
else:
	SOURCE_API_KEY = 'api-key ' + SOURCE_API_KEY

## Create the request
headers = {
"Authorization": SOURCE_API_KEY,
"accept": "application/json"
}
req = requests.get(BASE_URL, headers=headers)


## If the req.status_code response will be '200' then it will initiate the function and ask for the target user API KEY 
def user_questions():
	global DES_API_KEY
	Question = input("[+] Successfully copied the Authentication Object.\nDo you want to paste it to another user? (Y/n)  ").lower()
	if Question == "":
		DES_API_KEY = input("Please enter the API Key of the target user: ")
		if DES_API_KEY == "":
			print("Error: No API KEY specified\n[+] Exiting... ")
			exit()
		elif DES_API_KEY != "":
			DES_API_KEY = DES_API_KEY
	elif Question == "y":
		DES_API_KEY = input("Please enter the API Key of the target user: ")
		if DES_API_KEY == "":
			print("Error: No API KEY specified\n[+] Exiting... ")
			exit()
		elif DES_API_KEY != "":
			DES_API_KEY = DES_API_KEY
	elif Question == "n":
		ans = input("Before exiting, do you want to print the AO json body? (Y/n) ").lower()
		if ans == 'y':
			print(req.text)
			exit()
		elif ans == '':
			print(req.text)
			exit()	
		else:
			print("OK, exiting... ")
			exit()
	else:
		print("Could not understand, please try again. ")
		user_questions()

## Checks if we got a '200' response code
if req.status_code == 200:
	user_questions()

else:
	print("Error, can not GET the Authentication Object using the specified credentials.\nplease make sure you are using a User API Key and not Organizaitional API Key.\n[+] Exiting... ")
	exit()

## User animation while the request is sent
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        terminal.write('\r[+] Sending the POST Request to the API ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.write('\r\n[+] Done!\n')
    terminal.flush()

t = Thread(target=animate)
t.start()
sleep(3)
done = True

## If the response code is '200' and the 
def createPost():

	BASE_URL = 'https://app.neuralegion.com/api/v1/auth-objects'
	headers = {
	"Authorization": "api-key " + DES_API_KEY,
	"accept": "application/json"
	}
	
	data = req.json()
	
	r = requests.post(BASE_URL, headers=headers,json=data)
	
	## Verify that the post request has been created successfully, if we get respose code '201' it means we are successfully created the AO
	## If you want to debug / check for the status code you can uncomment the following line:
	# print(r.status_code)
	if r.status_code == 201:
		print("\nSuccessfully created the Authentication Object, please check your Authentication Object Dashboard")
	else:
		print("Something is wrong, please check your credentials and try again. ")
		
createPost()
