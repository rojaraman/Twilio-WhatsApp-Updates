import requests


class CoronaUpdates:
    def __init__(self, state, district):
        self.state = state
        self.district = district
        self.api = 'https://api.covid19india.org/state_district_wise.json'
        self.resultSet = self.getAllData()

    def getAllData(self):
        resp = requests.get(self.api)
        if resp.status_code != 200:
            # This means something went wrong.
            raise Exception('GET  {}'.format(resp.status_code))
        return resp.json()

    def getStateWise(self):
        res = self.resultSet
        result = {}
        for state in res:
            if state == self.state:
                result = res[self.state]
        return result

    def getDistrictWise(self):
        res = self.getStateWise()
        result = {}
        for district in res['districtData']:
            if district == self.district:
                result = res['districtData'][self.district]
        return result


# s = CoronaUpdates("Telangana", "Ranga Reddy")
# print(s.getDistrictWise())

# https://api.covid19india.org/state_district_wise.json
