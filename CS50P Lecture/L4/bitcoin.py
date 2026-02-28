import requests
import sys

def main():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit()

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")    
    try:
        bit_coin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]

    total_price = price * bit_coin
    print(f"${total_price:,.4f}")

if __name__ == "__main__":
    main()