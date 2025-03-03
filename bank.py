
def bank(action,tot_bal):
    match action:
        case "deposit":
            amount=int(input("enter amount:"))
            print(tot_bal + amount)
        case "withdraw":
            amount=int(input("enter amount:"))
            if tot_bal<amount:
                print("insufficient bank balance")
            else:
                print(tot_bal - amount)
        case "balance":
            print(tot_bal)

def main():
    bal=int(input("tot bal:"))
    action=input("enter an action:")
    bank(action,bal)
        
main()
