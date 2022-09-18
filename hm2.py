print("WELCOME TO ARUSUVAI HOTEL")
print("choose your booking slot NUMBER")
print("1.BREAKFAST","\n2.LUNCH","\n3.DINNER")
your_slot=int(input("ENTER YOUR SLOT NUMBER: "))
if your_slot==1:
    print(f"YES,YOUR BREAKFAST SLOT IS AVAILBLE","\nCHOOSE YOUR ORDER FROM MENU")
    print("idly","\ndosa","\npoori","\npongal","\nvada")
    your_order=input("Enter your order: ").lower()
    menus=["idly","dosa","poori","pongal","vada"]
    idly_amt=10
    dosa_amt=30
    poori_amt=35
    pongal_amt=30
    vada_amt=7
    if your_order in menus: 
       print(f"yes your {your_order} is available") 
       how_many=int(input(f"how many {your_order} you want:")) 
       if your_order=="idly":
        total=idly_amt*how_many
        print(f"your total bill is RS.{total}") 
       elif your_order=="dosa":
        total=dosa_amt*how_many
        print(f"your total bill is RS.{total}")
       elif your_order=="poori":
        total=poori_amt*how_many
        print(f"your total bill is Rs.{total}")
       elif your_order=="pongal":
        total=pongal_amt*how_many
        print(f"your total bill is Rs.{total}")
       elif your_order=="vada":
        total=vada_amt*how_many
        print(f"your total bill is Rs.{total}")
    else:
       print(f"sorry your {your_order} is not available")
elif your_slot==2:
    print(f"YES,YOUR LUNCH SLOT IS AVAILBLE","\nCHOOSE YOUR ORDER FROM MENU")
    print("parrotta","\nbiriyani","\nmeals","\nlemonrice")
    your_order=input("enter your order: ").lower()
    menus=["parrotta","biriyani","meals","lemonrice"]
    parrotta_amount=15
    biriyani_amount=100
    meals_amount=80
    lemonrice_amount=35
    if your_order in menus: 
       print(f"yes your {your_order} is available") 
       how_many=int(input(f"how many {your_order} you want:")) 
       if your_order=="parrotta":
        total=parrotta_amount*how_many
        print(f"your total bill is RS.{total}") 
       elif your_order=="biriyani":
        total=biriyani_amount*how_many
        print(f"your total bill is RS.{total}")
       elif your_order=="meals":
        total=meals_amount*how_many
        print(f"your total bill is Rs.{total}")
       elif your_order=="lemonrice":
        total=lemonrice_amount*how_many
        print(f"your total bill is rs.{total}")
    else:
        print(f"sorry your {your_order} is not available")
elif your_slot==3:
    print(f"YES,YOUR DINNER SLOT IS AVAILBLE","\nCHOOSE YOUR ORDER FROM MENU")
    print("parrotta","\nnoodles","\nchappathi","\ndosa")
    your_order=input("enter your order: ").lower()
    menus=["parrotta","noodles","chappathi","dosa"]
    parrotta_amount=15
    noodles_amount=100
    chappathi_amount=30
    dosa_amount=35
    if your_order in menus: 
       print(f"yes your {your_order} is available") 
       how_many=int(input(f"how many {your_order} you want:")) 
       if your_order=="parrotta":
        total=parrotta_amount*how_many
        print(f"your total bill is RS.{total}") 
       elif your_order=="noodles":
        total=noodles_amount*how_many
        print(f"your total bill is RS.{total}")
       elif your_order=="chappathi":
        total=chappathi_amount*how_many
        print(f"your total bill is Rs.{total}")
       elif your_order=="dosa":
        total=dosa_amount*how_many
        print(f"your total bill is rs.{total}")
    else:
       print(f"sorry your {your_order} is not available")
else:
    print("Error!!! Please Enter a Valid Slot Number")