from github import Github
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

atk = "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" # insert own access token
g = Github(atk)

user = g.get_user()
print('Loading repos for... ' + user.name)

repos = g.get_user().get_repos()

print('-------------REPOSITORIES---------------')
for r in repos:
    print(r.name)
