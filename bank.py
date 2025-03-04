
def bank(action,tot_bal):
    match action.strip(): #  it will strip space value in both end
        case "deposit":
            amount=int(input("enter amount:"))
            print(f"total balance is {tot_bal + amount}")
        case "withdraw":
            amount=int(input("enter amount:"))
            if tot_bal<amount:
                print("insufficient bank balance")
            else:
                print(f"total balance is {tot_bal - amount}")
        case "balance":
            print(tot_bal)
        case _:
            print("enter valid action :(")

def main():
    bal=int(input("tot bal:"))
    action=input("enter an action:")
    bank(action,bal)
        
main()
