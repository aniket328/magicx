from discord_webhooks import DiscordWebhooks

#Put your discord webhook url here.

webhook_url = 'https://discordapp.com/api/webhooks/799600802406727721/OG8nj4As7fhHbTj4xqKi14YQxY19eQOTO-blgAhRcuRW0iuBP2HqdgZgi0aMnc-AQzUr'


def send_msg(class_name,status,start_time,end_time):

    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
    # Attaches a footer
    webhook.set_footer(text='-- selenium bot')

    if(status=="joined"):

      webhook.set_content(title='Class Joined Succesfully',
                          description="Here's your report with :heart:")

      # Appends a field
      webhook.add_field(name='Class', value=class_name)
      webhook.add_field(name='Status', value=status)
      webhook.add_field(name='Joined at', value=start_time)
      webhook.add_field(name='Leaving at', value=end_time)

    elif(status=="left"):
      webhook.set_content(title='Class left Succesfully',
                          description="Here's your report with :heart:")

      # Appends a field
      webhook.add_field(name='Class', value=class_name)
      webhook.add_field(name='Status', value=status)
      webhook.add_field(name='Joined at', value=start_time)
      webhook.add_field(name='Left at', value=end_time)


    elif(status=="noclass"):
      webhook.set_content(title='Seems like no class today',
                          description="No join button found! Assuming no class.")

      # Appends a field
      webhook.add_field(name='Class', value=class_name)
      webhook.add_field(name='Status', value=status)
      webhook.add_field(name='Expected Join time', value=status)
      webhook.add_field(name='Expected Leave time', value=end_time)

    webhook.send()

    print("Sent message to discord")

def send_test(textm):
    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
    # Attaches a footer
    webhook.set_footer(text='-- selenium bot')
    webhook.set_content(title='Test Message',
                        description='sending log')
    webhook.add_field(name='log', value=textm)
    webhook.send()
    print("test message sent")