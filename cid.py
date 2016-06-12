from opencnam import Phone
import os

def returnName(phoneNumber):
	account_sid=os.environ.get('SID')
	auth_token=os.environ.get('TOKEN')
	
	result = Phone(str(phoneNumber), account_sid=account_sid, auth_token=auth_token)
	return result.cnam