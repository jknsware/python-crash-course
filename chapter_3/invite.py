invitees = ['mickey', 'minnie', 'donald']
message = f"{invitees[0].title()}, you're invited to dinner!"
print(message)
message = f"{invitees[1].title()} can't make it to dinner."
print(message)
invitees[1] = 'goofy'
message = f"{invitees[1].title()} will come instead."
print(message)
print()

invitees.insert(0, 'dale')
invitees.insert(2, 'chip')
invitees.append('daisy')
print(invitees)
print()

pop_invitee = invitees.pop()
message = f"Sorry, {pop_invitee.title()}. There's not enough room at the table."
print(message)
pop_invitee = invitees.pop()
message = f"Sorry, {pop_invitee.title()}. There's not enough room at the table."
print(message)
pop_invitee = invitees.pop()
message = f"Sorry, {pop_invitee.title()}. There's not enough room at the table."
print(message)
pop_invitee = invitees.pop()
message = f"Sorry, {pop_invitee.title()}. There's not enough room at the table."
print(message)
print(invitees)
invitees.remove('dale')
invitees.remove('mickey')
print(invitees)
