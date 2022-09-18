print("*********************WELCOME TO ONLINE TICKET BOOKING*********************")
trans=["BUS","TRAIN","FLIGHT"]
print("Mode Of Transport: BUS,TRAIN,FLIGHT")
trans_mode=input("Enter Mode Of Transport: ").upper().strip()
print(f"Redirecting you to {trans_mode} page....","\nPlease Wait")
if trans_mode=="BUS":
    From_city=input("Enter Departure Location: ").lower()
    To_city=input("Enter Arrival Location: ").lower()
    Date_Of_Depature=int(input("Enter Your Date: "))
    print("\n1.Seater","\n2.Semi-sleeper","\n3.Sleeper","\n4.AC-seater","\n5.AC-semi-sleeper","\n6.AC-sleeper")
    Req_Bus_Type=int(input("ENTER REQUIRED BUS TYPE NUMBER: "))
    if Req_Bus_Type==1:
      print("NO.OF SEATS AVAILABLE:20","\nADULT TICKET PRICE=350","\nCHILD TICKET PRICE=175")
      Adult_Ticket=int(input("ENTER NO.OF.ADULT TICKET: "))
      Child_Ticket=int(input("ENTER NO.OF.CHILD TICKET: "))
      if Adult_Ticket+Child_Ticket <=20:
        Tot_Price=(Adult_Ticket*350)+(Child_Ticket*175)
        print("TOTAL PRICE: ",Tot_Price,"\nTHANKS FOR BOOKING...","\nYOUR TICKET HAS BEEN CONFRMED")
      else:
        print("Enter Valid No.of tickets")
    elif Req_Bus_Type==2:
       print("NO.OF SEATS AVAILABLE:25","\nADULT TICKET PRICE=400","\nCHILD TICKET PRICE=200")
       Adult_Ticket=int(input("ENTER NO.OF.ADULT TICKET: "))
       Child_Ticket=int(input("ENTER NO.OF.CHILD TICKET: "))
       if Adult_Ticket+Child_Ticket <=25:
        Tot_Price=(Adult_Ticket*400)+(Child_Ticket*200)
        print("TOTAL PRICE: ",Tot_Price,"\nTHANKS FOR BOOKING...","\nYOUR TICKET HAS BEEN CONFRMED")
       else:
        print("Enter Valid No.of tickets")
    elif Req_Bus_Type==3:
       print("NO.OF SEATS AVAILABLE:12","\nADULT TICKET PRICE=450","\nCHILD TICKET PRICE=225")
       Adult_Ticket=int(input("ENTER NO.OF.ADULT TICKET: "))
       Child_Ticket=int(input("ENTER NO.OF.CHILD TICKET: "))
       if Adult_Ticket+Child_Ticket <=12:
         Tot_Price=(Adult_Ticket*450)+(Child_Ticket*225)
         print("TOTAL PRICE: ",Tot_Price,"\nTHANKS FOR BOOKING...","\nYOUR TICKET HAS BEEN CONFRMED")
       else:
            print("Enter Valid No.of tickets")
    elif Req_Bus_Type==4:
        print("NO.OF SEATS AVAILABLE:19","\nADULT TICKET PRICE=400","\nCHILD TICKET PRICE=200")
        Adult_Ticket=int(input("ENTER NO.OF.ADULT TICKET: "))
        Child_Ticket=int(input("ENTER NO.OF.CHILD TICKET: "))
        if Adult_Ticket+Child_Ticket <=19:
          Tot_Price=(Adult_Ticket*400)+(Child_Ticket*200)
          print("TOTAL PRICE: ",Tot_Price,"\nTHANKS FOR BOOKING...","\nYOUR TICKET HAS BEEN CONFRMED")
        else:
           print("Enter Valid No.of tickets")
    elif Req_Bus_Type==5:
        print("NO.OF SEATS AVAILABLE:30","\nADULT TICKET PRICE=500","\nCHILD TICKET PRICE=250")
        Adult_Ticket=int(input("ENTER NO.OF.ADULT TICKET: "))
        Child_Ticket=int(input("ENTER NO.OF.CHILD TICKET: "))
        if Adult_Ticket+Child_Ticket <=30:
          Tot_Price=(Adult_Ticket*500)+(Child_Ticket*250)
          print("TOTAL PRICE: ",Tot_Price,"\nTHANKS FOR BOOKING...","\nYOUR TICKET HAS BEEN CONFRMED")
        else:
           print("Enter Valid No.of tickets")
    elif Req_Bus_Type==6:
       print("NO.OF SEATS AVAILABLE:3","\nADULT TICKET PRICE=700","\nCHILD TICKET PRICE=225")
       Adult_Ticket=int(input("ENTER NO.OF.ADULT TICKET: "))
       Child_Ticket=int(input("ENTER NO.OF.CHILD TICKET: "))
       if Adult_Ticket+Child_Ticket <=3:
         Tot_Price=(Adult_Ticket*450)+(Child_Ticket*225)
         print("TOTAL PRICE: ",Tot_Price,"\nTHANKS FOR BOOKING...","\nYOUR TICKET HAS BEEN CONFRMED")
       else:
          print("Enter Valid No.of tickets")
    else:
        print("Error!!! Please Enter Valid Bus Type Number")
elif trans_mode=="TRAIN":
    From_city=input("Enter Departure Location: ").lower()
    To_city=input("Enter Arrival Location: ").lower()
    Date_Of_Depature=int(input("Enter Your Date: "))
    print("\n1.Second Seater","\n2.Sleeper","\n3.Three tier AC","\n4.Two tier AC","\n5.First class AC")
    Req_Seat_Type=int(input("ENTER REQUIRED SEAT TYPE NUMBER: "))
    if Req_Seat_Type==1:
      print("NO.OF SEATS AVAILABLE:20","\nADULT TICKET PRICE=350","\nCHILD TICKET PRICE=175")
      Adult_Ticket=int(input("ENTER NO.OF.ADULT TICKET: "))
      Child_Ticket=int(input("ENTER NO.OF.CHILD TICKET: "))
      if Adult_Ticket+Child_Ticket <=20:
        Tot_Price=(Adult_Ticket*350)+(Child_Ticket*175)
        print("TOTAL PRICE: ",Tot_Price,"\nTHANKS FOR BOOKING...","\nYOUR TICKET HAS BEEN CONFRMED")
      else:
        print("Enter Valid No.of tickets")
    elif Req_Seat_Type==2:
       print("NO.OF SEATS AVAILABLE:25","\nADULT TICKET PRICE=400","\nCHILD TICKET PRICE=200")
       Adult_Ticket=int(input("ENTER NO.OF.ADULT TICKET: "))
       Child_Ticket=int(input("ENTER NO.OF.CHILD TICKET: "))
       if Adult_Ticket+Child_Ticket <=25:
        Tot_Price=(Adult_Ticket*400)+(Child_Ticket*200)
        print("TOTAL PRICE: ",Tot_Price,"\nTHANKS FOR BOOKING...","\nYOUR TICKET HAS BEEN CONFRMED")
       else:
        print("Enter Valid No.of tickets")
    elif Req_Seat_Type==3:
       print("NO.OF SEATS AVAILABLE:12","\nADULT TICKET PRICE=450","\nCHILD TICKET PRICE=225")
       Adult_Ticket=int(input("ENTER NO.OF.ADULT TICKET: "))
       Child_Ticket=int(input("ENTER NO.OF.CHILD TICKET: "))
       if Adult_Ticket+Child_Ticket <=12:
         Tot_Price=(Adult_Ticket*450)+(Child_Ticket*225)
         print("TOTAL PRICE: ",Tot_Price,"\nTHANKS FOR BOOKING...","\nYOUR TICKET HAS BEEN CONFRMED")
       else:
            print("Enter Valid No.of tickets")
    elif Req_Seat_Type==4:
        print("NO.OF SEATS AVAILABLE:19","\nADULT TICKET PRICE=400","\nCHILD TICKET PRICE=200")
        Adult_Ticket=int(input("ENTER NO.OF.ADULT TICKET: "))
        Child_Ticket=int(input("ENTER NO.OF.CHILD TICKET: "))
        if Adult_Ticket+Child_Ticket <=19:
          Tot_Price=(Adult_Ticket*400)+(Child_Ticket*200)
          print("TOTAL PRICE: ",Tot_Price,"\nTHANKS FOR BOOKING...","\nYOUR TICKET HAS BEEN CONFRMED")
        else:
           print("Enter Valid No.of tickets")
    elif Req_Seat_Type==5:
        print("NO.OF SEATS AVAILABLE:30","\nADULT TICKET PRICE=500","\nCHILD TICKET PRICE=250")
        Adult_Ticket=int(input("ENTER NO.OF.ADULT TICKET: "))
        Child_Ticket=int(input("ENTER NO.OF.CHILD TICKET: "))
        if Adult_Ticket+Child_Ticket <=30:
          Tot_Price=(Adult_Ticket*500)+(Child_Ticket*250)
          print("TOTAL PRICE: ",Tot_Price,"\nTHANKS FOR BOOKING...","\nYOUR TICKET HAS BEEN CONFRMED")
        else:
           print("Enter Valid No.of tickets")
    else:
        print("Error!!! Please Enter Valid Seat Type Number")
elif trans_mode=="FLIGHT":
     print("Sorry for the inconvinence.....","\nOur Flight booking page is under maintainance")
else:
    print("Error!!! Please Enter a Valid Transport Mode")

