class FlightData:
    def __init__(self):
        self.destination_data = {}
        pass

    def format_data(self,city,flights_to_city):
        flight_list = []
        for day in flights_to_city:
            for flight in day:
                departureDate = flight["lastTicketingDate"]
                returnDate = flight["itineraries"][-1]["segments"][-1]["arrival"]["at"].split("T")[0]
                price = flight["price"]["total"]
                stops = len(flight["itineraries"][0]["segments"])
                flight_list.append({"departureDate": departureDate, "returnDate": returnDate, "price": price, "stops": stops})
        self.destination_data[city] = flight_list

    def find_cheapest_flight(self,city):
        min_price = float("inf")
        min_iter = 0
        for iter, flight in enumerate(self.destination_data[city]):
            if float(flight["price"]) < min_price:
                min_price = float(flight["price"])
                min_iter = iter
        return min_price, min_iter
