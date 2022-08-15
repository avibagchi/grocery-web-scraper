from bs4 import BeautifulSoup
import urllib.request

class SmartCart:
    global hannameslist
    global hanpriceslist
    global walnameslist
    global walpriceslist
    hannameslist = []
    hanpriceslist = []
    walnameslist = []
    walpriceslist = []
    storing=0
    def __init__(self, store):
        self.storing= int (store)

    def description(self, nameslist, priceslist):
        countnumtimes=0
        request = input("Give a one word description of the product you want \n")
        totalnamelist=[]
        totalpricelist=[]
        totaltotalpricelist=[]
        totaltotalnamelist=[]
        for count in range(len(nameslist)):
            if request in nameslist[count]:
                print(nameslist[count])
                print(priceslist[count])
                totalnamelist.append(nameslist[count])
                totalpricelist.append(priceslist [count])
                countnumtimes+=1

        if countnumtimes == 0:
            print("We could not find anything matching your request" + "\n")
            SmartCart.description(self, nameslist, priceslist)
        if countnumtimes>1:
            anotherrequest=input("Give a another word \n")
            for count in range(len(totalnamelist)):
                if anotherrequest in totalnamelist[count]:
                    print(totalnamelist[count])
                    print(totalpricelist[count])
                    totaltotalnamelist.append(totalnamelist[count])
                    totaltotalpricelist.append(totalpricelist[count])
            global storenamelist
            global storepricelist
            global storerequest
            global storeanotherrequest
            if countnumtimes>1:
                storepricelist=totaltotalpricelist
                storenamelist=totaltotalnamelist
                storerequest=request
                storeanotherrequest=anotherrequest
            elif countnumtimes==1:
                storepricelist = totalpricelist
                storenamelist = totalnamelist
                storerequest = request


    def pricecompare (self, nameslist, priceslist, code):
        totalnamelist = []
        totalpricelist = []
        totaltotalpricelist = []
        totaltotalnamelist = []
        countnumtimes = 0
        compareminindex=-1
        for count in range(len(nameslist)):
            if storerequest in nameslist[count]:
                #print(nameslist[count])
                #print(priceslist[count])
                totalnamelist.append(nameslist[count])
                totalpricelist.append(priceslist[count])
                countnumtimes += 1
        if countnumtimes == 0:
            print("We could not find anything matching your request in other stores" + "\n")
            return
        if countnumtimes > 1:
            for count in range(len(totalnamelist)):
                if storeanotherrequest in totalnamelist[count]:
                    #print(totalnamelist[count])
                    #print(totalpricelist[count])
                    totaltotalnamelist.append(totalnamelist[count])
                    totaltotalpricelist.append(totalpricelist[count])

        if countnumtimes > 1:
            min=100000
            for x in range (len (totaltotalpricelist)):
                p=totaltotalpricelist [x]
                if code == 1:
                    p = p[1:]
                elif code == 2:
                    p = p[p.find('$') + 1:p.find("n") - 1]
                if float (p)<min:
                    min= float (p)
                    minindex=x
            print("min:" + str(min))
            comparemin=10000
            for x in range (len (storepricelist)):
                p=storepricelist [x]
                if code==2:
                    p=p[1:]
                elif code==1:
                    p=p[p.find ('$')+1:p.find ("n")-1]
                if float (p)<comparemin:
                    comparemin= float (p)
                    compareminindex = x
            print("Comparemin:" + str (comparemin))
        else:
            min = 100000
            for x in range(len(totalpricelist)):
                p=totalpricelist [x]
                p=p[1:]
                if float (p) < min:
                    min = float (p)
                    minindex = x

            comparemin = 10000
            for x in range(len(storepricelist)):
                p=storepricelist[x]
                p=p[1:]
                if float (p) < comparemin:
                    comparemin = float (p)
                    compareminindex=x
        print ("DO YOU GET HERE")
        for v in range (len (totalnamelist)):
            totalnamelist [v].upper ()
        for vv in range (len (totaltotalnamelist)):
            totaltotalnamelist[vv].upper ()
        for vvv in range (len (storenamelist)):
            storenamelist[vvv].upper ()

        if len (totaltotalpricelist)==0:
            print ("Here is an option in another store:"+"\n")
            print (totalnamelist)
            print (totalpricelist)
            if "OZ." in storenamelist [compareminindex]:
                finder=storenamelist [compareminindex] [0:storenamelist.find ("OZ")-1]
                floater=float (finder)
                comparemin/=floater
                print ("HEREE")

            elif "OZ" in storenamelist [compareminindex]:
                finder= storenamelist [compareminindex] [storenamelist.find (",")+1:storenamelist.find ("OZ")]
                floater=float (finder)
                comparemin/=floater
                print("HEREE")

            if "OZ." in totalnamelist [minindex]:
                finder=totalnamelist [minindex] [0:totalnamelist.find ("OZ")-1]
                floater=float (finder)
                comparemin/=floater
                print("HEREE")

            elif "OZ" in totalnamelist [minindex]:
                findertwo= totalnamelist [minindex][totalnamelist.find (",")+1:totalnamelist.find ("OZ")]
                floatertwo=float (findertwo)
                min/=floatertwo
                print("HEREE")

        else:
            print ("Almost THERE")
            print ("Here is an option in another store:"+"\n")
            print (totaltotalnamelist)
            print (totaltotalpricelist)
            if "OZ." in storenamelist [compareminindex]:
                finder = storenamelist[compareminindex][0:storenamelist.find("OZ") - 1]
                floater = float(finder)
                comparemin /= floater
                print("HEREE")

            elif "OZ" in storenamelist [compareminindex]:
                finder = storenamelist[compareminindex][storenamelist.find(",") + 1:storenamelist.find("OZ")]
                floater = float(finder)
                comparemin /= floater
                print("HEREE")

            if "OZ." in totaltotalnamelist [minindex]:
                finder = totaltotalnamelist[minindex][0:totaltotalnamelist.find("OZ") - 1]
                floater = float(finder)
                comparemin /= floater
                print("HEREE")

            elif "OZ" in totaltotalnamelist [minindex]:
                findertwo = totaltotalnamelist[minindex][totaltotalnamelist.find(",") + 1:totaltotalnamelist.find("OZ")]
                floatertwo = float(findertwo)
                min /= floatertwo
                print("HEREE")



        if code==1:
            print ("\n"+"Per Quantity the price for Walamart is: "+str (comparemin)+ "\n")
            print ("\n"+"Per Quantity the price for Hanaford is "+str (min)+ "\n")
        elif code==2:
            print("\n"+"Per Quantity the price for Walamart is: " + str (min)+ "\n")
            print("\n" + "Per Quantity the price for Hanaford is " + str (comparemin)+ "\n")

        if comparemin<min and code==1:
            print ("Walamart is a better deal")
        elif comparemin<min and code==2:
            print ("Hanaford is a better deal")
        elif comparemin>min and code==1:
            print ("Hanaford is a better deal")
        elif comparemin<min and code==2:
            print ("Walamart is a better deal")



    def walamart(self, skipper):
        compareminindex = -1
        def store (y,code):
            values=[x.get_text () for x in y]
            #global walnameslist
            #global walpriceslist
            for value in values:
                if code==1:
                    walnameslist.append (value)
                else:
                    walpriceslist.append (value)
            print ("This is WALAMART")
            print ('\n')
            print (walnameslist)
            print (walpriceslist)
        def maker (link, stringer):
            global walnameslist
            global walpriceslist
            #url forming
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
            url=link+"?"+stringer
            req=urllib.request.Request (url, headers=headers)

            #url opening and reading
            resp=urllib.request.urlopen(req)
            html=resp.read ()
            soup=BeautifulSoup (html, 'html.parser')

            #finding products and prices
            names=soup.find_all ("div",{'class':"search-result-product-title gridview"})
            prices=soup.find_all ("span",{'class':"price-group"})
            store (names,1)
            store (prices,2)

            #printer
            #for count in range (0,len(nameslist)):
                #print (nameslist [count])
                #print (priceslist [count])
        if skipper==-1:
            #ask user
            num = input("What are you looking for:\n" + "Grilling Foods press 1\n" + "Breakfast Foods press 2\n" + "Produce press 3\n" + "Snacks press 4\n" + "Candy press 5\n" + "Beverages press 6\n"+"Canned Vegetables press 7\n")
            num = int(num)
        else:
            num=skipper

        #Grilling Foods
        if num==1:
            for page in range (1,25):
                maker ("https://www.walmart.com/browse/seasonal-grocery/summer-grilling-foods/976759_1567409_8808777", "page="+str (page))

        #Breakfast foods
        if num==2:
            for page in range (1,25):
                maker ("https://www.walmart.com/browse/breakfast/976759_976783", "page="+str (page))

        #Produce
        if num==3:
            for page in range (1,25):
                maker ("https://www.walmart.com/browse/food/produce/976759_1071964_976793", "page="+str (page))

        #Snacks
        if num==4:
            for page in range (1,25):
                maker ("https://www.walmart.com/browse/seasonal-grocery/back-to-school-foods/976759_1567409_7966149","page="+str (page))

        #Candy
        if num==5:
            for page in range (1,25):
                maker ("https://www.walmart.com/browse/food/cold-packed-groceries/976759_1567409_7329770", "page="+str (page))

        #Juice
        if num==6:
            for page in range (1,25):
                maker ("https://www.walmart.com/browse/juices/all-juices/976759_976782_1001321_8981297", "page="+str (page))

        #CannedVegetables
        if num==7:
            for page in range (1,25):
                maker ("https://www.walmart.com/browse/food/canned-vegetables/976759_976794_976785_3605629", "page="+str (page))

        if skipper==-1:
            SmartCart.description(self, walnameslist, walpriceslist)
            SmartCart.hanaford(self,num)
        else:
            SmartCart.pricecompare(self, walnameslist, walpriceslist, 1)


    def hanaford (self, skipper):

        def storeagain (y, code):
            values = [x.get_text() for x in y]
            #global hannameslist
            #global hanpriceslist
            for value in values:
                if code == 1:
                    hannameslist.append(value)
                else:
                    hanpriceslist.append(value)
            print ("This is HANAFORD")
            print('\n')
            print (hannameslist)
            print (hanpriceslist)

        #Hannoford
        def makerh (link):
            #url forming
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
            url=link
            req=urllib.request.Request (url, headers=headers)

            #url opening and reading
            resp=urllib.request.urlopen(req)
            html=resp.read ()
            soup=BeautifulSoup (html, 'html.parser')

            #finding products and prices
            names=soup.find_all ("div", {'class':'productPriceInfoInner'})
            prices=soup.find_all ("div", {'class':'product-price'})
            storeagain (names,1)
            storeagain (prices,2)

            #printer
            #for count in range (0,len(nameslist)):
                #print (nameslist [count])
                #print (priceslist [count])

        #ask user
        if skipper==-1:
            num = input("What are you looking for:\n" + "Breakfast Foods press 2\n" + "Beverages press 6\n"+"Canned Vegetables press 7\n")
            num = int(num)
        else:
            num=skipper
        #BreakfastFoods
        if num==2:
            makerh ('https://www.hannaford.com/departments/grocery/breakfast-cereal?displayAll=true')
        #Juice
        if num==6:
            makerh ('https://www.hannaford.com/departments/beverages/juice?displayAll=true')
        #CannedVegetables
        if num==7:
            makerh ('https://www.hannaford.com/departments/grocery/canned-vegetables?displayAll=true')

        if skipper==-1:
            SmartCart.description(self, hannameslist, hanpriceslist)
            SmartCart.walamart(self,num)
        else:
            SmartCart.pricecompare (self, hannameslist, hanpriceslist, 2)

            #print (priceslist[count]+"\n")
            #check=input ("If these are products you are looking for press 1; if not press 0 ")




print ("\nLet's make your grocery list!\n")
print ("Keep typing items. When you are done press 0")
print ("                                                                Groceries: ")
grocerylist=[]
c=True
while (c):
    item=input ("Type an item, press 0 to quit:\n")
    if item=='0':
        break
    print ("                                                                   "+item)
    grocerylist.append (item)
print ("Here is your list")
print (grocerylist)


p1 = input("What shop would you like? Press 1 for Walmart, Press 2 for Hanaford")
ob=SmartCart (p1)
if ob.storing == 1:
    ob.walamart(-1)
elif ob.storing == 2:
    ob.hanaford(-1)
