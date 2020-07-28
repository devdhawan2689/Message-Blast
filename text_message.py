import requests
from bs4 import BeautifulSoup
import pprint
from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService


res = requests.get('https://transcripts.fandom.com/wiki/A_Bug%27s_Life')
soup = BeautifulSoup(res.text, 'html.parser')
story = soup.select('p')
# print(story)
# print('____________________________________')
# script = [item.getText() for item in story]
# pprint.pprint(script)

for item in story:
	script = item.getText().split('\n')
# pprint.pprint(script)

mobileNumber = '(Enter the Mobile Number of the Victim)'
androidIP = IPv4Address("(Enter your Phone's IP Address)")
androidSession = AirmoreSession(androidIP)
smsService = MessagingService(androidSession)

for i in range(len(script)):
	textMessage = script[i]
	smsService.send_message(mobileNumber,textMessage)
	print(textMessage)

