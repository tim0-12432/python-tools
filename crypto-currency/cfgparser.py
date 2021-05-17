import json
import datetime

with open("config.json", "r") as file:
    config = json.load(file)

# currency which the crypto prices should be compared to
CURRENCY = config["currency"]

# metric for diagrams
METRIC = config["metric"]

# list of currencies
CRYPTO = config["crypto"]

# simulation starting date
START_DATE = datetime.datetime(config["start_date"]["year"], config["start_date"]["month"], config["start_date"]["day"])