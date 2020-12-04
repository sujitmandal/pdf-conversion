import json
import pandas as pd 

"""
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn
"""

with open('data/data.json') as a:
    data = json.load(a)

users = data.get('users')
pd.DataFrame(users).to_excel('data/data.xlsx')