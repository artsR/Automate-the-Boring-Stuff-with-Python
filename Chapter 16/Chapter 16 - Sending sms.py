########## CHAPTER 16 ##########

from twilio.rest import TwilioRestClient

accountSID = input()
authToken = input()
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = input()
myCellPhone = input()

message = twilio.Cli.messages.create(body='Mr. Watson - Come here - I want..',
                                     from_=myTwilioNumber, to=myCellPhone)
print(message.to)
print(message.from_)
print(message.body)
print(message.status)   # queued
print(message.date_created)
print(message.date_sent == None) # true

print(message.sid) # ID of sent message (unique value)
updateMessage = twilioCli.messages.get(message.sid)
print(updateMessage.status) # delivered
print(updateMessage.date_sent == None) # false


# Project: "Just Text Me"

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
    
