import urllib.request
import requests
import threading
import json

def read_data_thingspeak():
    url='https://api.thingspeak.com/channels/557500/fields/1.json?api_key='
    key='DH884ECZP7Q4WYBF' #read
    header='&results=2'
    new_url=url+key+header
    print(new_url)

    get_data=requests.get(new_url).json()
    print(get_data)
    channel_id = get_data['channel']['id']

    field_1=get_data['feeds']
    print(field_1)

    t=[]
    for x in field_1:
        print(x['field1'])
        t.append(x['field1'])

if __name__ == '__main__':
    read_data_thingspeak()
