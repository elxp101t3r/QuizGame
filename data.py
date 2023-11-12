import requests as r
response = r.get('https://opentdb.com/api.php?amount=10&category=32&type=boolean')
question_data = response.json()