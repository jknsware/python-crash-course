sandwich_orders = ['pastrami', 'ham', 'pastrami', 'egg salad', 'turkey', 'pastrami', 'bologna']
finished_sandwiches = []

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')

while sandwich_orders:
  current_sandwich = sandwich_orders.pop()
  print(f"I made your {current_sandwich} sandwich.")
  finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
  print(f"I made a {sandwich} sandwich.")
