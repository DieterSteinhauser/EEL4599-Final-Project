import http.client as httplib
import urllib
import time

# Can only send data once every 15 seconds (16 for reliable transmission)
def send(data, field, key):
    params = urllib.parse.urlencode({field: data, 'key':key }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        print (temp)
        conn.close()
    except:
        pass

def test(key):
    #Calculate CPU temperature of Raspberry Pi in Degrees C
    temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
    params = urllib.parse.urlencode({'field1': temp, 'key':key }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        print (temp)
        conn.close()
    except:
        pass
        
if __name__ == "__main__":
    key = "2FXIAZTDLKSROT3W"  # Put your API Key here
    for i in range(0,10):
        thermometer(key)
        time.sleep(16)
 
