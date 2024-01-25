bid_finished=False
empty_dic = {}
def biding(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"the winner is {winner} with a bid of {highest_bid}")
while not bid_finished:
    name=input("enter the name:\n")
    bid=int(input(" what is your bid:\n$"))
    empty_dic[name]=bid



    result=input("enter yes if there are biders or no if there are not\n")

    if result=="NO":
        bid_finished=True
        print("game over")
        biding(empty_dic)

