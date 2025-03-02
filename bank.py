
def bank(action):
    tot_bal=int(input("tot bal:"))
    amount=int(input("enter amount:"))
    match action:
        case "deposit":
            print(tot_bal + amount)
        case "withdraw":
            print(tot_bal - amount)
        case "balance":
            print(tot_bal)

def main():
    action=input("enter an action:")
    bank(action)
        
main()
