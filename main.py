from github import Github

atk = "" # delete later!
g = Github(atk)

user = g.get_user()
print('Loading repos for... ' + user.name)

repos = g.get_user().get_repos()

print('-------------REPOSITORIES---------------')
for r in repos:
    print(r.name)
