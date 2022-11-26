import art
print(art.logo)

bidding_completed = False
bidding_dbs={}

def calculation(bid):
    highest_bid=0
    winner=""
    for i in bid:
        bid_amount = bid[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner=i
    print(f"The winner is {winner}, with a bid of {highest_bid}")

while not bidding_completed:
    name= input("Enter your name: ")
    bid = int(input("Enter your Bid: $"))
    bidding_dbs[name]=bid
    more_user = input("Are there more bidder? type 'yes' or 'no': ")
    if more_user == "no":
        bidding_completed = True
        calculation(bidding_dbs)


