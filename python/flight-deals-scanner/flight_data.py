class FlightData:
    def __init__(self):
        pass

    def find_cheapest_flight(self,flights_to_city):
        min_price = float("inf")
        min_dates = ""
        for flight in flights_to_city:
            if float(flight["price"]) < min_price:
                min_price = float(flight["price"])
                min_dates = f"{flight["departure_time"]}-{flight["arrival_time"]}"
        return min_price, min_dates
