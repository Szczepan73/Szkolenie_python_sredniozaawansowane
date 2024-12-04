from dotenv import load_dotenv   # pip install python-dotenv
import os
import requests # pip install requests

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
print(os.getenv('Domain'))
print(os.getenv('PASSWORD'))



url = "http://jsystems.pl/Universe/samaTabelka.do"
response = requests.get(url)
data = response.json()

for training in data:
    print(training)