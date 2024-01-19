# class FlightData:
#     #This class is responsible for structuring the flight data.
#     pass

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport_code, destination_city, destination_airport_code, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport_code = origin_airport_code
        self.destination_city = destination_city
        self.destination_airport_code = destination_airport_code
        self.out_date = out_date
        self.return_date = return_date
