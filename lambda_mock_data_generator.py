import json
import random

def lambda_handler(event, context):
    name_list = ['Shashank', 'Ehtisham', 'Nikhil', 'Rahman', 'John', 'Joseph', 'Ayush']
    age_list = [29,27,25,23,21,22,24]
    salary_list = [10000,9000,8000,7000,7500,8500,9500]
    random_id = random.randint(0,6)
    payload = {}
    payload['name_list'] = name_list[random_id]
    payload['age_list'] = age_list[random_id]
    payload['salary_list'] = salary_list[random_id]
    return payload
