PREARRANGED_STOP = 0
highest_bid = 0

# reserve price and item name
item = input('What is the auction for: ')
while True:
    reserve_price = input('What is the reserve price: $')
    if reserve_price.isdigit():
        reserve_price = float(reserve_price)
        break
    else:
        print('Please enter a valid number')

print()
print(f'The auction for the {item} has started!')
print()

# main starts
while PREARRANGED_STOP != -1:
    print(f'Highest bid so far is: {highest_bid}')
    while True:
        bid = input('What is your bid: $')
        if bid == '-1':
            PREARRANGED_STOP = -1
            break
        if bid.isdigit():
            bid = float(bid)
            if bid > highest_bid:
                highest_bid = bid
                break
            else:
                print('Please enter a bigger bid')
        else:
            print('Please enter a valid bid')

# final message
if highest_bid > reserve_price:
    print(f'The auction for the {item} finished with a bid of ${highest_bid}!')
else:
    print(f'The {item} did not sell!')