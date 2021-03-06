import json

class RatesParser:

    def __init__(self, rates_file):
        rates_info = self._open_json_file(rates_file)
        self.base = rates_info["base"]
        self.rates = rates_info["rates"]
        self.gbp = self.rates["GBP"]
# Making below method private using "_"

    def _open_json_file(self, file):
        with open(file) as rates:
            return json.load(rates)


rates_reader = RatesParser("exchange_rates.json")

print(rates_reader.rates)
