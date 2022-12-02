import requests

data = requests.get("https://opentdb.com/api.php?amount=10&category=9#")
print(data.json())