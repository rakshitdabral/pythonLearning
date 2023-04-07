import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "MqIyw1zWdLT9q-LrbFD1a_JFn97hfWnJ"


class FlightSearch:

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        response = requests.get(url=TEQUILA_ENDPOINT)
        code = "TESTING"
        return code
