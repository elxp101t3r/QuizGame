import requests as r
amount_of_questions = '10'
response = r.get(f'https://opentdb.com/api.php?amount={amount_of_questions}&category=32&type=boolean')
question_data = response.json()