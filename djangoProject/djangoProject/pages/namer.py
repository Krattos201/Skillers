import urllib.request
import urllib.parse
import random
from pages.views import Register_form
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

def otp(apikey, numbers, sender, message):   
	 
	resp =  sendSMS(apikey, numbers, sender, message)
	