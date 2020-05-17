from CoronaUpdates import CoronaUpdates
from datetime import date


class FormatMessages:
    def __init__(self, state, district):
        self.state = state
        self.district = district
        self.rawMessage = self.getMessageRaw()
        self.valid = ["active", "confirmed", "deceased", "recovered"]

    def getMessageRaw(self):
        updates = CoronaUpdates(self.state, self.district)
        return updates.getDistrictWise()

    def setMessageBody(self):
        message = [self.district + " , " + self.state, str(date.today())]
        for key, value in self.rawMessage.items():
            if key in self.valid:
                message.append(key + ":" + str(value))
        return "\n".join(message)


# s = FormatMessages("Telangana", "Ranga Reddy")
# print(s.setMessageBody())
