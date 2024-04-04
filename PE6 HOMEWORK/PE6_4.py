current_users = ["admin", "Tom", "Jerry", "Dora", "George"]

input_username = input("Enter your username: ")

input_username_lower = input_username.lower()

if input_username_lower in [username.lower() for username in current_users]:
    print(f"Sorry {input_username}, that name is taken.")
    print("Current users:", current_users)
else:
    print(f"Great, {input_username}, is still available.")
    current_users.append(input_username)
    print("Updated user list:", current_users)