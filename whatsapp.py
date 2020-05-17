from twilio.rest import Client
import json
from messageformat import FormatMessages


class TwilioMessages:
    def __init__(self):
        self._account_sid = ""
        self._auth_token = ""
        self._creds_file = 'credentials.txt'
        self._from_phone_number = ""
        self._receiver = ""
        self.getCreds()
        self._input = 'input.txt'
        self._state = ""
        self._district = ""
        self.getInput()
        self._platform = "whatsapp:"

    def getCreds(self):
        with open(self._creds_file) as json_file:
            data = json.load(json_file)
            for c in data['credentials']:
                self._account_sid = c['account_sid']
                self._auth_token = c['auth_token']
                self._from_phone_number = c['from_']
                self._receiver = c['my_phone']

    def getInput(self):
        with open(self._creds_file) as json_file:
            data = json.load(json_file)
            for c in data['input']:
                self._state = c['state']
                self._district = c['district']

    def getMessage(self, state, district):
        message = FormatMessages(state, district)
        return message.setMessageBody()

    def sendMessage(self):
        client = Client(self._account_sid, self._auth_token)
        from_phone_number = self._platform + self._from_phone_number
        to_phone_number = self._platform + self._receiver
        message = self.getMessage(self._state, self._district)
        # print(message)
        client.messages.create(body=message,
                               from_=from_phone_number,
                               to=to_phone_number)


twilio = TwilioMessages()
twilio.sendMessage()
