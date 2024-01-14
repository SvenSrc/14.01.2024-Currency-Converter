import requests

currencyLines = {
    "AED": 6,
    "AFN": 7,
    "ALL": 8,
    "AMD": 9,
    "ANG": 10,
    "AOA": 11,
    "ARS": 12,
    "AUD": 13,
    "AWG": 14,
    "AZN": 15,
    "BAM": 16,
    "BBD": 17,
    "BDT": 18,
    "BGN": 19,
    "BHD": 20,
    "BIF": 21,
    "BMD": 22,
    "BND": 23,
    "BOB": 24,
    "BRL": 25,
    "BSD": 26,
    "BTC": 27,
    "BTN": 28,
    "BWP": 29,
    "BYN": 30,
    "BZD": 31,
    "CAD": 32,
    "CDF": 33,
    "CHF": 34,
    "CLF": 35,
    "CLP": 36,
    "CNH": 37,
    "CNY": 38,
    "COP": 39,
    "CRC": 40,
    "CUC": 41,
    "CUP": 42,
    "CVE": 43,
    "CZK": 44,
    "DJF": 45,
    "DKK": 46,
    "DOP": 47,
    "DZD": 48,
    "EGP": 49,
    "ERN": 50,
    "ETB": 51,
    "EUR": 52,
    "FJD": 53,
    "FKP": 54,
    "GBP": 55,
    "GEL": 56,
    "GGP": 57,
    "GHS": 58,
    "GIP": 59,
    "GMD": 60,
    "GNF": 61,
    "GTQ": 62,
    "GYD": 63,
    "HKD": 64,
    "HNL": 65,
    "HRK": 66,
    "HTG": 67,
    "HUF": 68,
    "IDR": 69,
    "ILS": 70,
    "IMP": 71,
    "INR": 72,
    "IQD": 73,
    "IRR": 74,
    "ISK": 75,
    "JEP": 76,
    "JMD": 77,
    "JOD": 78,
    "JPY": 79,
    "KES": 80,
    "KGS": 81,
    "KHR": 82,
    "KMF": 83,
    "KPW": 84,
    "KRW": 85,
    "KWD": 86,
    "KYD": 87,
    "KZT": 88,
    "LAK": 89,
    "LBP": 90,
    "LKR": 91,
    "LRD": 92,
    "LSL": 93,
    "LYD": 94,
    "MAD": 95,
    "MDL": 96,
    "MGA": 97,
    "MKD": 98,
    "MMK": 99,
    "MNT": 100,
    "MOP": 101,
    "MRU": 102,
    "MUR": 103,
    "MVR": 104,
    "MWK": 105,
    "MXN": 106,
    "MYR": 107,
    "MZN": 108,
    "NAD": 109,
    "NGN": 110,
    "NIO": 111,
    "NOK": 112,
    "NPR": 113,
    "NZD": 114,
    "OMR": 115,
    "PAB": 116,
    "PEN": 117,
    "PGK": 118,
    "PHP": 119,
    "PKR": 120,
    "PLN": 121,
    "PYG": 122,
    "QAR": 123,
    "RON": 124,
    "RSD": 125,
    "RUB": 126,
    "RWF": 127,
    "SAR": 128,
    "SBD": 129,
    "SCR": 130,
    "SDG": 131,
    "SEK": 132,
    "SGD": 133,
    "SHP": 134,
    "SLL": 135,
    "SOS": 136,
    "SRD": 137,
    "SSP": 138,
    "STD": 139,
    "STN": 140,
    "SVC": 141,
    "SYP": 142,
    "SZL": 143,
    "THB": 144,
    "TJS": 145,
    "TMT": 146,
    "TND": 147,
    "TOP": 148,
    "TRY": 149,
    "TTD": 150,
    "TWD": 151,
    "TZS": 152,
    "UAH": 153,
    "UGX": 154,
    "USD": 155,
    "UYU": 156,
    "UZS": 157,
    "VES": 158,
    "VND": 159,
    "VUV": 160,
    "WST": 161,
    "XAF": 162,
    "XAG": 163,
    "XAU": 164,
    "XCD": 165,
    "XDR": 166,
    "XOF": 167,
    "XPD": 168,
    "XPF": 169,
    "XPT": 170,
    "YER": 171,
    "ZAR": 172,
    "ZMW": 173,
    "ZWL": 174
}

# Get Exchange Rate, where the base currency is USD (others are blocked as base)
api_request = "https://openexchangerates.org/api/latest.json?app_id=26360b53202b41d483e672296a6d1706"

headers = {"accept": "application/json"}

receive = requests.get(api_request, headers=headers)

# Save the received response in a local text file
with open("currency_exchange_rate.txt", "w") as fileWrite:
    fileWrite.write(receive.text)

# Ask the user how much it wants to convert
print("Sum to convert (USD):")
sum = int(input())

print()

# Read the file with the currency rate list
openFile = open("currency_exchange_rate.txt")
readFile = openFile.readlines()

# Ask the user to what currency it should convert
print("Convert to:")
target_rate = input().upper()

print()

# Print the exchange rate
print(readFile[currencyLines.get(target_rate)])

# User types in the rate
print("Type in the target currency rate:")
converted = float(input())

print()

# Print the result
print(f"With {sum} USD you get: {converted * sum} {target_rate}")
