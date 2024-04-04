usernames = ["Tom", "Jerry", "Bob", "Dora", "admin"]

if len(usernames) == 0:
    print("We need to find some users.")
else:
    for username in usernames:
        if username.lower() == "admin":
            print("Hello ADMIN, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again!")