print("****WELCOME TO D-MART -DAIRY SHOP***")
import os
import sys
import datetime
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='sairam',database='mysql');
#creating  customer  table
def customer():
    myCursor=mydb.cursor();
    query='create table if not exists customer(custname varchar(30),Mobilephn int PRIMARY KEY, grossprice int,paymode varchar(20),Timefpr datetime);'
    myCursor.execute(query);
    print('Table custname created successfully!')
    

#creating product table
def prod():
    myCursor=mydb.cursor();
    query='create table if not exists Products(Product varchar(50) not null unique,Unitprice int, Stock int);'
    myCursor.execute(query);
    print('Table Products created successfully!')



def Prodlist():#error
    myCursor=mydb.cursor();
    a=[('Milk-(1 Litre)',60,10),('Curd-(250g)',30,20),('Ghee-(1 litre)',540,15),('Cheese-(200g)',118,15),('Butter-(100g)',55,20),('Paneer-(200g)',100,20),('Freshcream-(250 ml)',63,10),('Buttermilk-(200ml)',30,20),('Badam milk-(200 ml)',50,20),('Rose milk-(200 ml)',50,20),('Vanilla Ice cream-(1 litre)',140,15),('Chocolate Ice cream-(1 litre)',155,15),('Strawberry Ice cream-(1 litre)',140,15),('Butterscotch Ice cream-(1 litre)',152,15),('Condensed Milk-(200 g)',55,15)]    
    for i in a:
        q1="insert into Products (Product,Unitprice,Stock) values('{}',{},{})".format(i[0],i[1],i[2])
        myCursor.execute(q1)
        mydb.commit()
    mycursor12=mydb.cursor();
    q12="Select * from Products "
    mycursor12.execute(q12)
    prin=mycursor12.fetchall()
    for k in prin:
        print(k)
def display():
    mycursor=mydb.cursor();
    q12="Select * from Products "
    mycursor.execute(q12)
    prin=mycursor.fetchall()
    for k in prin:
        print(k)
    


items={1:'Milk-(1 Litre)',2:'Curd-(250g)',3:'Ghee-(1 litre)',4:'Cheese-(200g)',5:'Butter-(100g)',6:'Paneer-(200g)',7:'Freshcream-(250 ml)',8:'Buttermilk-(200ml)',9:'Badam milk-(200 ml)',10:'Rose milk-(200 ml)',11:'Vanilla Ice cream-(1 litre)',12:'Chocolate Ice cream-(1 litre)',13:'Strawberry Ice cream-(1 litre)',14:'Butterscotch Ice cream-(1 litre)',15:'Condensed Milk-(200 g)'}
##Product varchar(50) not null unique,Unitprice decimal(9,2), Stock int

def insNEWPROD():
    n=int(input("Enter how many record you want to enter:"))
    myCursor=mydb.cursor();
    for i in range (n):
        pname=input('Enter product name:')#product and quantity
        up=int(input('Enter unit price:'))
        qty=int(input("Enter  quantity of product:"))
        myCursor.execute("insert into Products(Product,Unitprice,Stock) values('{}',{},{})".format(pname,up,qty));
        mydb.commit()
        global items
        pcode=len(items)+1
        items[pcode]=pname
        print(items)
        print(' New Product Record inserted successfully...')


        
def Updatestock():
    global items
    print(items)
    prd=int(input('Enter the Product number whose stock is to be incremented:'))
    tot=int(input('Enter the quantity to be added:'))
    val1=items[prd]
    print(val1)
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='sairam',database='mysql');
    myCursor1=mydb.cursor();
    myCursor1.execute("select Stock from Products where Product='{}'".format(val1));
    a=myCursor1.fetchall()
    
    for i in a:
        for j in i:
            upd=(j)+(tot)    
    myCursor2=mydb.cursor();
    myCursor2.execute("update Products set Stock={} where Product='{}'".format(upd,val1));
    print('Record updated(Added stock) successfully...')
    mydb.commit();
    show_stock()
                
def show_stock():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='sairam',database='mysql');
    myCursor=mydb.cursor();
    myCursor.execute('select * from Products');
    myTable=myCursor.fetchall();
    for i in myTable:
        print(i)
    #if stock=0 calling del record function 

##x=product
##y=quantity

def ReduceRecord(x,y):
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='sairam',database='mysql');
    myCursor=mydb.cursor();
    myCursor.execute("select Stock from Products where Product = '{}'".format(x,))
    tot=myCursor.fetchone()
    for i in tot:
        total=i-y   
    myCursor3=mydb.cursor();    
    myCursor3.execute("update Products set Stock={} where Product = '{}'".format(total,x));
    print('Record updated successfully...')
    items[x]=total
    mydb.commit();
    print("Stock left =",total) 

    
def Outofstock():
    val=0
    myCursor=mydb.cursor();
    sql_query = "select Product from Products where Stock = {}".format(val);
    myCursor.execute(sql_query)
    record = myCursor.fetchall()
    for i in record:
        print("Product out of stock=",i)
    if  len(record)==0:
        print("No product out of stock")

def findCRname():
    ano=input('Enter the  Customer Name:')
    myCursor=mydb.cursor()
    sqlStat="select * from customer where custname = '{}'".format(ano);
    myCursor.execute(sqlStat)
    rec=myCursor.fetchall()
    for i in rec:
        print( "Customer details",i)
    if rec==None:
        print('Sorry!! no record found')
      
def billing():
    i=1
    ch="y"
    #items={1:'Milk-(1 Litre)',2:'Curd-(250g)',3:'Ghee-(1 litre)',4:'Cheese-(200g)',5:'Butter-(100g)',6:'Paneer-(200g)',7:'Freshcream-(250 ml)',8:'Badam milk-(200 ml)',9:'Rose milk-(200 ml)',10:'Vanilla Ice cream-(1 litre)',11:'Chocolate Ice cream-(1 litre)',12:'Strawberry Ice cream-(1 litre)',13:'Butterscotch Ice cream-(1 litre)',14:'Condensed Milk-(200 g)'}
    global items
    sn=1     
    fin=0
    p=[]
    #fc=0
    input_rows=[]
    while ch in ["y","Y"]:
        
        i=i+1
        print(items)
        v=int(input("Enter product code:"))
        prod=items[v]
        prin=print("Product:",prod) 
        myCursor=mydb.cursor()
        query="select Unitprice from Products where Product='{}'".format(prod);
        myCursor.execute(query);
        unitp=myCursor.fetchone()
        qty=int(input("Enter  Product's quantity:"))
        ret=qty
        ReduceRecord(prod,ret)
        for i in unitp:
            tot=i*qty
        t=str(sn)+"." 
        a=[t,prod,qty,tot]
        p.append(a)
        sn=sn+1
        fin=fin+tot
        hsn = v
        particular= prod
        qty = float(ret)
        for t in unitp:
            n_rate = float(t)        
        input_rows.append([hsn, particular, qty, n_rate])
        ch=input("wanna enter more records?(y/n):")
    from datetime import datetime
#import pyqrcode
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_date = datetime.now().date()

    dash = "-" * 63
    print(dash.center(60))
    txt = "D Mart"
    print(txt.center(60))
    print(dash.center(60))
    txt1 = "AVENUE SUPERMARTS LTD"
    print(txt1.center(60))
    print(dash.center(60))
    text = "DMART MOTERA,City Gold Multiplex Compound,Motera Stadium Road Sabarmati Motera ,Ahmedabad - 380005"
    lines = text.split(',')
    for line in lines:
        centered = line.strip().center(60)
        print(centered.ljust(60))
                
    phone_number = "_" * 21 + " Phone : 079-30936500 " + "_" * 21
    centered_phone_number = phone_number.center(60)
    print(centered_phone_number)


    print("  TAX INVOICE ".center(63))
    print("  Bill date : ",current_date)
    print("  Bill time : ", current_time)

    print("  Vou. No : S078012-0079")
    print("  Cashier :  MJA/078175 ")
    print(dash.center(60))

    #for i in range(fc):
    print("{:<5} {:<30} {:<7} {:<8} {:<8}".format("HSN", "Particulars", "Qty", "N/Rate", "Value"))

    total_qty = 0
    total_value = 0
    for row in input_rows:
        hsn, particular, qty, n_rate = row
        value = (qty * n_rate)
        value = float(value)
        print("{:<5} {:<30} {:<7} {:<8} {:<8}".format(hsn, particular, qty, n_rate, '%.2f' % value))
        total_qty += qty
        total_value += value       
    print(dash.center(60))
    print("{:<5} {:<30} {:<7} {:<8} {:<8}".format("", "Total:", total_qty, "", total_value))
    dash2="_"*63
    print(dash2.center(60))
    print(dash2.center(60))
    print("Amount Recieved From Customer :) ".center(60))
    print("!! Thankyou Visit again !!".center(60))
    print(dash.center(60))
    print(dash.center(60))
       
    if ch in ["n","N"]:
        grossp=fin
        myCursor=mydb.cursor();
        cnm=input("Enter Customer name:")
        mbnm=int(input("Enter mobile number:"))
        paymod=input("Enter Payment mode:")
        myCursor=mydb.cursor();
        a="insert into Customer(custname,Mobilephn,grossprice,paymode,Timefpr) values ('{}',{},{},'{}','{}')".format(cnm,mbnm,grossp,paymod,datetime.now())
        myCursor.execute(a)
        mydb.commit()
        print(" Customer's Record inserted successfully...")
        print()
        print()
        for k in p:
            print(k[0],k[1],k[2],k[3])

        print("                                                              GRAND TOTAL:",fin)

while 4!=5:
            os.system('cls')
            print ("MENU \n 1-Creating table  customer \n 2-Creating table Products \n 3- Displaying product list \n 4- Insert new Product  into Product list\n 5-Update stock \n 6- Show stock \n 7- Reduce stock(record) \n 8- Display Product out of Stock \n 9-Find customer record \n 10-Billing software \n 11- Displaying product list after updating \n 12-Exit program") 
       
            ch=int(input("Enter your choice:"))
                
            if ch==1:
                customer()
                    
            elif ch==2:
                prod()
                   
            elif ch==3:
                Prodlist()
            elif ch==4:
                insNEWPROD()
            elif ch==5:
                Updatestock()
            elif ch==6:
                show_stock()
            elif ch==7:
                ReduceRecord()
            elif ch==8:
                Outofstock()
   
            elif ch==9:
                findCRname()
            elif ch==10:
                 billing()
            elif ch==11:
                 display()     
            elif ch==12:
                print(print("THANK YOU !!! VISIT AGAIN  "))
                sys.exit()
            else:
                print("Invalid option. Retry")








