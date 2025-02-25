# Set a secret password
correct_password = "topsecretstuff"

password = input("Enter the password: ")

# Check if it matches
if password == correct_password:
    print("Access granted!")
else:
    print("Access denied!")
