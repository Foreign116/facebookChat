import fbchat
from fbchat.models import *
import time
import getpass



def myPassword():
	password = getpass.getpass("Enter your password: ")
	return password

def myEmail():
	email = input("Enter your email: ")
	return email

def friendName():
	name = input("Enter the name of the friend you want to send a message to: ")
	return name

def enterMessage():
	message = input("Enter message you want to send to friend: ")
	return message


client = fbchat.Client(myEmail(),myPassword())
friend = friendName()
friends = client.searchForUsers(friend)

index = 0

for i in friends:
	print(str(index)+ " " + i.first_name + " " + i.last_name)
	index = index + 1

index = 0

pick_index = input("Which friend (index) do you want to pick to send a message to?")

friend = friends[int(pick_index)]

if(client.sendMessage(enterMessage(), friend.uid)):
	print("Sent message")
else:
	print("There was a problem")


		