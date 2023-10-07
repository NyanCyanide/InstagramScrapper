from Module.Instat import Instat

# Create an instance for the driver and activate the class
instat = Instat()

# Load Instagram login page
instat.loadPage("https://www.instagram.com/")

# Login into Instagram
instat.login()

# Go to user main profile
instat.mainUserProfile()

# Get the followers list
# users in the form of list example
# users = ["charles_leclerc", "f1", "scuderiaferrari"]
# deafult is your profile
instat.getFollowers(exhaustlimit=50)

# Get the following list
# users in the form of list example
# users = ["charles_leclerc", "f1", "scuderiaferrari"]
# deafult is your profile
instat.getFollowing(exhaustlimit=50)