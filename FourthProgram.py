# If name is less than 3 character long
# name must be at least 3 characters
# otherwise if it's more than 50 character long
name = 'j'
if len(name) < 3:
    print("Name must be at least 3 characters.")
if len(name) > 50:
    print("Name must be a maximum of 50 character.")
else:
    print("Name looks good!")