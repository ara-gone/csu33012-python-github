
# a script to do python based access to the github api
# step 2 - let's get PyGitHub going.
# we have to pip install PyGithub on the command line.

print("Demonstration python based github api access");

#import Github from the PyGithub library
from github import Github

#we initialise a PyGithub Github object with our access token.
# note that this token is ours, and now deleted. You must crete your own access
# token and use here instead. 
g = Github("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")

#Let's get the user object and print some trivial details
usr = g.get_user()
print("user:     " + usr.login)
print("fullname: " + usr.name)
print("location: " + usr.location)
print("company:  " + usr.company)


