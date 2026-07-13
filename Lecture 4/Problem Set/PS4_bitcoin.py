#Import relevant packages
import sys
import requests

#Gather volume information
try:
    volume = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")

#Execute API call
response = requests.get(
    "https://rest.coincap.io/v3/price/bysymbol/BTC",
    headers={"Authorization": "Bearer 42706a087a110053429feddb149183ab319a357648932c1b56944915097871b8"}
    )

#Extract price from results
bitcoin = response.json()
price = float(bitcoin["data"][0])

#Develop quote based on input
quote = price * volume

#Format and print results
print(f"${quote:,.4f}")