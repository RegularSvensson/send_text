from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACafdad160a10780e1e8ee8b4e0c6c023e"
auth_token  = "cd62bb26131cbb60ae327379eeb6fec8"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Say my name...",
    to="+46727431990",    # Replace with your phone number
    from_="+46 10 138 86 98") # Replace with your Twilio number
print message.sid