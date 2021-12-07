# Initial version of house_sim.py
# housing and houseappliances objects, used to take in data from dteh data simulator and output them accordingly.

class housing():

    def __init__(self, address, residents):
        self.address = address
        self.residents = residents
    def __str__(self):
        return(self.address)
# class housing(): formats and outputs existing addresses and outputs them for the user to select an address
    def displayhouse(self):
        print('Address: ', self.address, '\tResident(s): ',self.residents) # Display function

class houseappliances():
    def __init__(self,onoff,totalusage, kWh):
        self.onoff = onoff
        self.totalusage = totalusage
        self.kWh = kWh
# class houseappliances(): formats and outputs on and off times, total usage in watts and total usage in kw
    def displayappliances(self):
        print('Total accumulated usage hours', self.onoff)
        print('Total usage', self.totalusage)
        print('Total usage (kWh)', self.kWh)
