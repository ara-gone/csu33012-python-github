
# a script to do python based access to the github api
# step 3 - Let's create a data dictionary for storage

print("Demonstration python based github api access");

#import Github from the PyGithub library
from github import Github
import json # for dictionary to string

#we initialise a PyGithub Github object with our access token.
# note that this token is ours, and now deleted. You must crete your own access
# token and use here instead. 
g = Github("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")

#Let's get the user object and build a data dictionary
usr = g.get_user()

dct = {'user': usr.login,
       'fullname': usr.name,
       'location': usr.location,
       'company': usr.company
       }

print ("dictionary is " + json.dumps(dct))



