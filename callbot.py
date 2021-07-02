try:
    from twilio.rest import Client
    from twilio.twiml.voice_response import Dial, VoiceResponse, Say
except:
    import pip
    pip.main(['install', 'twilio'])
    from twilio.rest import Client
    from twilio.twiml.voice_response import Dial, VoiceResponse, Say
from os import system
import time

#####INFORMATION#####
#YOUR PHONE NUMBER
NUMBER = "+1"
#TWILIO NUMBER
FROM = "+1"
#EDD NUMBER
CALL = "+18339782511"
#TWILIO ACCOUNT SID
ACCOUNT_SID = ""
#TWILIO AUTH TOKEN
AUTH_TOKEN = ""
#XML FILE (CALL SCRIPT)
XML_URL = ""
#HOW MANY CALLS (PER 3 MINUTES 30 Seconds)
BOT_NUM = 20
#####################

client = Client(ACCOUNT_SID, AUTH_TOKEN)

responseCall = VoiceResponse()
dial = Dial()
dial.number(
    NUMBER
)
responseCall.append(dial)

calc = BOT_NUM * 17
count = 0
calling = True
call = {}

while calling:
    system('clear')
    print("EDD Call Bot Now Running [Press CTRL-C To Exit]\nCalling", calc , "Times Per Hour \n")
    print("--Call Count :" , count)
    for number in range(0,BOT_NUM):
        call["call%s" %number] = client.calls.create(
            url=XML_URL,
            to=CALL,
            from_=FROM
        )
    print("--Making Calls")
    try:
        time.sleep(210)
        count += BOT_NUM
        for number in range(0,BOT_NUM):
            call["call%s" %number]
            call["call%s" %number] = client.calls(call["call%s" %number].sid) \
            .update(twiml=responseCall)
            print("--Connecting", NUMBER ,"To EDD")
            calling = False
    except:
        pass
print("Thank You For Using EDD Call Bot!")
