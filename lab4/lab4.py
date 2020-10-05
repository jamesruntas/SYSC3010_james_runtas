import http.client
import urllib.parse
key = "54CDA6FJF4RCJ92C"
def writeData():
    email = "jamesruntas@cmail.carleton.ca"
    group = "L2-M-12"
    memberId = "c"
    params = urllib.parse.urlencode({'field1': email , 'field2':group, 'field3': memberId, 'key': key})
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print (email, group, memberId)
        print (response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print ("connection failed")
if __name__ == "__main__":
    writeData()