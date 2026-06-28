usernames=["raj","priyal12","ilma","alex","computer"]

valid_usernames=list(filter(lambda name:len(name)>=6,usernames))

print("Valid usernames:",valid_usernames)