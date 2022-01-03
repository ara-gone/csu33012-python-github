from github import Github
from config import *
import pandas as pd
import numpy as np

atk = get_access_token() # insert own access token
g = Github(atk)

user = g.get_user()
print('Loading repos for... ' + user.name)

repos = g.get_user().get_repos()
df = pd.DataFrame()

print('-------------REPOSITORIES---------------')
for r in repos:
    print(r.name)
    prs = r.get_pulls(state='all')
    df = df.append({
        'ID': r.id,
        'Name': r.name,
        'Language': r.language,
        'Stars': r.stargazers_count,
        'Watchers': r.subscribers_count,
        'Pull_Requests': prs.totalCount
    }, ignore_index=True)

df.to_csv('../repos.csv', sep=',', encoding='utf-8', index=True)
