class BaseStation:
    """base station
    
    Attributes:
         Id: number
         Address: name address
         Latitude: latitude
         Longitude: longitude
         User_num: number of users
         Workload: total usage time in minutes
    """

    def __init__(self, id, addr, lat, lng):
        self.id = id
        self.address = addr
        self.latitude = lat
        self.longitude = lng
        self.user_num = 0
        self.workload = 0

    def __str__(self):
        return "No.{0}: {1}".format(self.id, self.address)
