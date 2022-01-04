from github import Github, RateLimitExceededException, BadCredentialsException
from config import *
import pandas as pd
import numpy as np

atk = get_access_token() # insert token into config.py file
g = Github(atk)

user = g.get_user()
print('Loading repos for... ' + user.name)

repos = g.get_user().get_repos()
df = pd.DataFrame()
df_commits = pd.DataFrame()

print('-------------REPOSITORIES---------------')
for r in repos:
    repo_commits = r.get_commits()
    # full name is username/reponame format, needed for pygithub lookup
    print(r.full_name + ', with commits -> ' + str(repo_commits.totalCount))
    prs = r.get_pulls(state='all')

# after listing available repositories, choose one to analyse

repo_name = ''
while repo_name != 'quit':
    # Ask the user for a name.
    repo_name = input("\nEnter the name of a repository: ")

    if (repo_name != 'quit'):
        r = g.get_repo(repo_name)
        df = df.append({
            'ID': r.id,
            'Name': r.name,
            'Language': r.language,
            'Stars': r.stargazers_count,
            'Watchers': r.subscribers_count,
            'Pull_Requests': prs.totalCount
        }, ignore_index=True)
        df.to_csv('../repos.csv', sep=',', encoding='utf-8', index=True)
        # df.to_csv('repos.csv', mode='a', header=False)
    else:
        print('Successfully quit program.')
