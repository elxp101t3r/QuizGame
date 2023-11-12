import requests as r
amount_of_questions = '10'
type_of = 'boolean'
response = r.get(f'https://opentdb.com/api.php?amount={amount_of_questions}&type={type_of}')
question_data = response.json()