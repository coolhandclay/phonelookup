import os
import requests

def getName(phoneNumber):
	apiKey = os.environ.get('APIKEY')
	headers = {'X-FullContact-APIKey': apiKey}
	payload = {'phone': str(phoneNumber)}
	url = 'https://api.fullcontact.com/v2/person.json'
	r = requests.get(url, headers=headers, params=payload)
	if r.status_code == '200':
		results = r.json()
		name = results.get('contactInfo').get('fullName')
		return name
	else:
		return "FC API cannot be reached right now"