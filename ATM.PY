print("WELCOME TO IOB ATM")
pin=9131
sav_amt=50000
cur_amt=500000
def main():
    user_pin=int(input("ENTER YOUR PIN: "))
    if (user_pin==pin):
       print("1.WITHDRAWAL","\n2.DEPOSIT","\n3.BALANCE ENQUIRY","\n4.OTHER SERVICES")
       services=[1,2,3,4]
       req_services=int(input("Enter Your Required Service Number: "))
       if req_services==1:
        print("1.SAVING ACCOUNT","\n2.CURRENT ACCOUNT")
        Acc_type=[1,2]
        req_Acc_type=int(input("Choose Your Account Type Number: "))
        if  req_Acc_type==1:
            with_amt=int(input("Enter Amount For Withdrawal: "))
            bal_amt=sav_amt-with_amt
            print("Your Current Balance is: ",bal_amt)
        elif req_Acc_type==2:
            with_amt=int(input("Enter Amount For Withdrawal: "))
            bal_amt=cur_amt-with_amt
            print("Your Current Balance is: ",bal_amt)
        else:
           print("Please Enter a valid account type number")
       elif req_services==2:
        dep_amt=int(input("Enter your amount to be deposit: "))
        bal_amt=sav_amt+dep_amt
        print("Your Current Balance is: ",bal_amt)
       elif req_services==3:
        with_sheet=[1000,20000,6000,500,3000]
        dep_sheet=[100,2000,100,4500,5000]
        bal_sheet=[49100,31100,25200,29200,31200]
        print("|Debit|Credit|Balance|")
        print("|1000 |100   |49100  |")
        print("|20000|2000  |31100  |")
        print("|6000 |100   |25200  |")
        print("|500  |4500  |29200  |")
        print("|3000 |5000  |32100  |")
       elif req_services==4:
        print("Other Services is under maintainance","\nSorry for the inconvinence","\nThank You...")
       else:
          print("Please Enter Valid Service Number")
    else:
      print("Enter Correct PIN Number")
      main()
      exit()
main()