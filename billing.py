name=input("enter u r name")
# list of items
items="""
    rice             $30/kg
    oil_              $80/lit
    salt             $20/kg
    tea_        $50/kg
    soap             $20
    """
# print(items)
price=0
price_list=[]
total=0
final=0
plist=[]
qlist=[]
ilist=[]

#rating
dict_items={
    "rice":30,
    "oil_":80,
    "salt":20,
    "tea_":50,
    "soap":20
}
#print(dict_items)
optin=int(input("enter 1 for list of items"))
if optin==1:
    print(items)
for i in dict_items:
    inp1=int(input("enter 1 for buy items or 2 for exit"))
    if inp1==2:
        break
    elif inp1==1:
        item=input("enter item:")
        quantity=int(input("enter  u r item quantity"))
        if item in dict_items.keys():
            price=quantity*(dict_items[item])
            #print(price)
            price_list.append((item,quantity,dict_items,price))
            total+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(total*5)/100
            final=gst+total
        else:
            print("sorry you entred item is not avalible")
    else:
        print("you enter a worng number")
    #inp=input("enter 'yes' to generat bill 'no' to continue")
    #if inp=="yes":
        pass
if final!=0:
    print(30*"*","SR super market",30*"*")
    print(30*" ","parvathi puram")
    print("Name:",name)
    print(75*"-")
    print("s.no",8*" ","Items",8*" ","Quantity",11*" ","price")
    for i in range(len(price_list)):
        print(i+1,11*" ",ilist[i],9*" ",qlist[i],18*" ",plist[i])
    print(75*"-")
    print("total amount",40*" ","$",total)
    print("GST",49*" ","$",gst)
    print(75*"-")
    print(50*" ",final)
    print(75*"-")
    print(25*" ","Thanks for visiting")
    print(75*"-")