## Create a program that will take the dictionary of USDA item# and item name, and allow the user to choose which one they want. 
## The program will then go back to USDA and pull nutritional information for that food
## It will then calculate, based on user input, the nutritional values of the foods. 
## A separate script will need to be created to generate a nutrition label. 
## Another script will be needed to wrap a GUI around the processing. 


#from USDA_SingleFoodQuery import *
from tkinter import *
from tkinter import ttk
import requests
foodIndex={}
food_brand_no=False
food_brand_yes=False

def callback():
    global fb
    global userFood
    fb=False
    if food_brand_yes.get()==True:
        fb=True
    print (fb)
    userFood=food_ent.get()
    print (userFood)

root=Tk()
root.title=("Nutritional Information")
root.geometry("500x200")
app=Frame(root)
app.grid()
# create instruction label
inst_lbl=Label(text="Please enter a food to retrieve nutritional information about it.")
inst_lbl.grid(row=0,columnspan=3,sticky=W)

# create label for food
food_lbl=Label(text="Food: ")
food_lbl.grid(row=1,column=0,sticky=E)

# create entry widget to accept food
food_ent=Entry(width=30)
food_ent.grid(row=1,column=1,sticky=W)

# create Boolean for brand names
Label(text="************************************************** ").grid(row=4,column=0,columnspan=2,sticky=W)
Label(text="Is your food name-brand? ").grid(row=5,column=0,columnspan=2,sticky=W)
Label(text="************************************************** ").grid(row=6,column=0,columnspan=2,sticky=W)

food_brand_yes=BooleanVar()
Checkbutton(text="Yes",variable=food_brand_yes).grid(row=7,column=0)
food_brand_no=BooleanVar()
Checkbutton(text="No", variable=food_brand_no).grid(row=7,column=1)

Button(root,text="Submit",command=callback).grid(row=10,column=1,sticky=W)
Button(root,text='Done',command=root.quit).grid(row=12,column=1,sticky=W)

def callback():
    user_food=food_ent
    return food_brand_yes
    return food_brand_no


root.mainloop()

def foodQuery():
    if fb==True:
        ds="Branded Food Products"
    else:
        ds="Standard Reference"
    #print ("DS:",ds,"  TypeDS:",type(ds),"  UserFood:",userFood,type(userFood))
    url=('https://api.nal.usda.gov/ndb/search/?format=json&q='+userFood+'&ds='+ds+'&group=&sort=r&max=40&offset=0&api_key=GskgvLdgJptkBE3r6WWX8bRGDgaKwy9UexF4oWTt&location=Denver+CO')
    response=requests.get(url)
    food=response.json()   

    for key,value in food.items():
        itemNumber=''
        itemName=""
        for label,lisst in value.items():
        
            if type(lisst)==list:
                for item in lisst:
                    for category,vlus in item.items():
                        #print (category,"\t|\t",vlus)
                        if category=="ndbno":
                            itemNumber=vlus
                        if category=="name":
                            itemName=vlus
                    foodIndex[itemNumber]=itemName
foodQuery()

#root.mainloop()

#r=10 # row
#c=0 # column
#for key,value in foodIndex.items():
#    value_entry=BooleanVar()
#    r=r+1
#    Checkbutton(text=value,variable=var_value).grid(row=r,column=c,sticky=W)
#    if r>30:
#        c=c+2
#        r=10



    







