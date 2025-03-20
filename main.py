#Import Time
import time

Vehicle_Number=['XXXX-XX-XXXX']
Vehicle_Type=['Bike']
vehicle_Name=['Intruder']
Owner_Name=['Unknown']
Date=['22-22-3636']
Time=['22:22:22']
bikes=100
cars=250
bicycles=78
def main():
    global bikes,cars,bicycles
    try:
        while True:
            print("----------------------------------------------------------------------------------------")
            print("\t\tParking Management System")
            print("----------------------------------------------------------------------------------------")
            print("1.Vehicle Entry")
            print("2.Remove Entry" )
            print("3.View Parked Vehicle ")
            print("4.View Left Parking Space ")
            print("5.Amount Details ")
            print("6.Bill")
            print("7.Close Programme ")
            print("+---------------------------------------------+")
            ch=int(input("\tSelect option:"))
            if ch==1:
                no=True
                while no==True:
                    Vno=input("\tEnter vehicle number (XXXX-XX-XXXX) - ").upper()
                    if Vno=="":
                        print("###### Enter Vehicle No. ######")
                    elif Vno in Vehicle_Number:
                        print("###### Vehicle Number Already Exists")
                    elif len(Vno)==12:
                        no=not True
                        Vehicle_Number.append(Vno)
                    else:
                        print("###### Enter Valid Vehicle Number ######")
                typee=True
                while typee==True:
                    Vtype=str(input("\tEnter vehicle type(Bicycle=A/Bike=B/Car=C):")).lower()
                    if Vtype=="":
                        print("###### Enter Vehicle Type ######")
                    elif Vtype=="a":
                        Vehicle_Type.append("Bicycle")
                        bicycles-=1
                        typee=not True
                    elif Vtype=="b":
                        Vehicle_Type.append("Bike")
                        bikes-=1
                        typee=not True
                    elif Vtype=="c":
                        Vehicle_Type.append("Car")
                        cars-=1
                        typee=not True
                    else:
                        print("###### Please Enter Valid Option ######")
                name=True
                while name==True:
                    vname=input("\tEnter vehicle name - ")
                    if vname=="":
                        print("########Please Enter Vehicle Name ########")
                    else:
                        vehicle_Name.append(vname)
                        name=not True
                o=True
                while o==True:
                    OName=input("\tEnter owner name - ")
                    if OName=="":
                        print("###### Please Enter Owner Name ######")
                    else:
                        Owner_Name.append(OName)
                        o=not True
                d=True
                while d==True:
                    date=input("\tEnter Date (DD-MM-YYYY) - ")
                    if date=="":
                        print("###### Enter Date ######")
                    elif len(date)!=10:
                        print("###### Enter Valid Date ######")
                    else:
                        Date.append(date)
                        d=not True
                t=True
                while t==True:
                    time=input("\tEnter Time (HH:MM:SS) - ")
                    if t=="":
                        print("###### Enter Time ######")
                    elif len(time)!=8:
                        print("###### Please Enter Valid Date ######")
                    else:
                        Time.append(time)
                        t=not True
                print("\n............................................................Record detail saved..................................................................")
            elif ch==2:
                no=True
                while no==True:
                    Vno=input("\tEnter vehicle number to Delete(XXXX-XX-XXXX) - ").upper()
                    if Vno=="":
                        print("###### Enter Vehicle No. ######")
                    elif len(Vno)==12:
                        if Vno in Vehicle_Number:
                            i=Vehicle_Number.index(Vno)
                            Vehicle_Number.pop(i)
                            Vehicle_Type.pop(i)
                            vehicle_Name.pop(i)
                            Owner_Name.pop(i)
                            Date.pop(i)
                            Time.pop(i)
                            no=not True
                            print("\n............................................................Removed Sucessfully..................................................................")
                        elif Vno not in Vehicle_Number:
                            print("###### No Such Entry ######")
                        else:
                            print("Error")
                    else:
                        print("###### Enter Valid Vehicle Number ######")
            elif ch==3:
                count=0
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tParked Vehicle")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("Vehicle No.\tVehicle Type        Vehicle Name\t       Owner Name\t     Date\t\tTime")
                print("----------------------------------------------------------------------------------------------------------------------")
                for i in range(len(Vehicle_Number)):
                    count+=1
                    print(Vehicle_Number[i],"\t  ",Vehicle_Type[i],"\t            ",vehicle_Name[i],"\t       ",Owner_Name[i],"      " ,Date[i],"          ",Time[i])
                print("----------------------------------------------------------------------------------------------------------------------")
                print("------------------------------------------ Total Records - ",count,"-------------------------------------------------------")
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch==4:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tSpaces Left For Parking")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\tSpaces Available for Bicycle - ",bicycles)
                print("\tSpaces Available for Bike - ",bikes)
                print("\tSpaces Available for Car - ",cars)
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch==5:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tParking Rate")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("*1.Bicycle      Rs20 / Hour")
                print("*2.Bike         Rs40/ Hour")
                print("*3.Car          Rs60/ Hour")
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch==6:
                print(".............................................................. Generating Bill ..........................................................................")
                no=True
                while no==True:
                    Vno=input("\tEnter vehicle number to Delete(XXXX-XX-XXXX) - ").upper()
                    if Vno=="":
                        print("###### Enter Vehicle No. ######")
                    elif len(Vno)==12:
                        if Vno in Vehicle_Number:
                            i=Vehicle_Number.index(Vno)
                            no=not True
                        elif Vno not in Vehicle_Number:
                            print("###### No Such Entry ######")
                        else:
                            print("Error")
                    else:
                        print("###### Enter Valid Vehicle Number ######")
                print("\tVehicle Check in time - ",Time[i])
                print("\tVehicle Check in Date - ",Date[i])
                print("\tVehicle Type - ",Vehicle_Type[i])
                inp=True
                amt=0
                while inp==True:
                    hr=input("\tEnter No. of Hours Vehicle Parked - ").lower()
                    if hr=="":
                        print("###### Please Enter Hours ######")
                    elif int(hr)==0 and Vehicle_Type[i]=="Bicycle":
                        amt=20
                        inp=not True
                    elif int(hr)==0 and Vehicle_Type[i]=="Bike":
                        amt=40
                        inp=not True
                    elif int(hr)==0 and Vehicle_Type[i]=="Car":
                        amt=60
                        inp=not True
                    elif int(hr)>=1:
                        if Vehicle_Type[i]=="Bicycle":
                            amt=int(hr)*int(20)
                            inp=not True
                        elif Vehicle_Type[i]=="Bike":
                            amt=int(hr)*int(40)
                            inp=not True
                        elif Vehicle_Type[i]=="Car":
                            amt=int(hr)*int(60)
                            inp=not True
                print("\t Parking Charge - ",amt)
                ac=18/100*int(amt)
                print("\tAdd. charge 18 % - ",ac)
                print("\tTotal Charge - ",int(amt)+int(ac))
                print("..............................................................Thank you for using our service...........................................................................")
                a=input("\tPress Any Key to Proceed - ")
            elif ch==7:
                print("..............................................................Thank you for using our service...........................................................................")
                print("                                     *********(: Bye Bye :)*")
                break
                quit
    except:
        main()
main()