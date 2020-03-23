current_users = ['Jason', 'kelli', 'Natalie', 'Sydney', 'leo', 'chief']
new_users = ['monkey', 'kelfer', 'Noodle', 'Stinker', 'Leo', 'bear']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
  if new_user.lower() in current_users_lower:
    print(f"Sorry {new_user}, that name is taken.")
  else:
    print(f"Great, {new_user} is still available.")
