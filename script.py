
# a script to do python based access to the github api
# step 3 - let's fix return type handling

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

if usr.name is not None:
    print("fullname: " + usr.name)
    
if usr.location is not None:    
    print("location: " + usr.location)
    
if usr.company is not None:    
    print("company:  " + usr.company)


