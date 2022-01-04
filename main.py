from github import Github, RateLimitExceededException, UnknownObjectException
from config import *
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

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

# after listing available repositories, choose one to analyse

repo_name = ''
while repo_name != 'quit':
    # Ask the user for a name.
    repo_name = input("\nEnter the name of a repository, or enter 'quit' -> ")

    if (repo_name != 'quit'):
        while True:
            try:
                r = g.get_repo(repo_name)
                prs = r.get_pulls(state='all')
                commits = r.get_commits()

                print('got repository... ' + repo_name)
                df = df.append({
                    'ID': r.id,
                    'Name': r.name,
                    'Language': r.language,
                    'Stars': r.stargazers_count,
                    'Watchers': r.subscribers_count,
                    'Pull_Requests': prs.totalCount,
                    'Commits': commits.totalCount
                }, ignore_index=True)

                for c in commits:
                    df_commits = df_commits.append({
                        'commit_sha': c.sha,
                        'commiter_username': c.author.login if c.author is not None else '',
                        'commit_date': c.author.created_at if c.author is not None else '',
                    }, ignore_index=True)
                    print('added commit on ' + str(c.author.created_at))

                df.to_csv('../repos.csv', sep=',', encoding='utf-8', index=True)
                df_commits.to_csv('../commits.csv', sep=',', encoding='utf-8', index=True)

                print('DONE! Check for repos.csv and commits.csv')
                # df.to_csv('repos.csv', mode='a', header=False)
            except RateLimitExceededException as e:
                print (e.status)
                print ('The limit for API access has been exceeded.')
                break
            except UnknownObjectException as e:
                print (e.status)
                print ('Incorrect repo name given.')
                break
            break
    else:
        print('Successfully quit program.')
