from twilio.rest import Client

def sms():
    account_sid = 'AC70919f1a6ee2ac0c1d29f700d5b8e2ba'
    auth_token = '6c85b035328941f4f302d7c8fa3c5a58'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Psalm 23:4 Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me. ",
                        from_='+16204104934',
                        to='+639051149345'
                    )

    print(message.body)

if __name__ == "__main__":
    
    sms()

