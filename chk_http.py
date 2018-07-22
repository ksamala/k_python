import socket
from urllib2 import urlopen, URLError, HTTPError

socket.setdefaulttimeout( 23 )  # timeout in seconds
responseMessage = "";
url = 'http://google.com/'
try :
    response = urlopen( url )
except HTTPError, e:
    responseMessage =  'The server couldn\'t fulfill the request. Reason:', str(e.code)
except URLError, e:
    responseMessage = 'We failed to reach a server. Reason:', str(e.reason)
else :
    responseMessage = response.read()
    
    with open('result.txt','ab') as f:
        f.write(responseMessage)
    print responseMessage