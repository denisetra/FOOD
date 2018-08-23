import requests

foodIndex={}


def foodQuery():

    ds=""
    userFood=""
    userFood=input("\nPlease enter the food you that you are looking for: ")
    userFoodType=input("Is it a name-brand food?")
    ds="Standard Reference"
    if userFoodType in ["Yes","yes","y"]:
        ds="Branded Food Products"
    else:
        ds="Standard Reference"

    url=('https://api.nal.usda.gov/ndb/search/?format=json&q='+userFood+'&ds='+ds+'&group=&sort=r&max=40&offset=0&api_key=GskgvLdgJptkBE3r6WWX8bRGDgaKwy9UexF4oWTt&location=Denver+CO')
    #url='https://api.nal.usda.gov/ndb/search/?format=json&q=cheese,cheddar&ds=Standard Reference&group=&sort=r&max=200&offset=0&api_key=GskgvLdgJptkBE3r6WWX8bRGDgaKwy9UexF4oWTt&location=Denver+CO'
    #url='https://api.nal.usda.gov/ndb/search/?format=json&q=butter&sort=n&max=25&offset=0&api_key=GskgvLdgJptkBE3r6WWX8bRGDgaKwy9UexF4oWTt&location=Denver+CO'
    response=requests.get(url)
    food=response.json()
    #print ("\n\n",response.json(),"\n\n")

    for key,value in food.items():
        itemNumber=''
        itemName=""
        for label,lisst in value.items():
        
            if type(lisst)==list:
                for item in lisst:
                    for category,vlus in item.items():
                        print (category,"\t|\t",vlus)
                        if category=="ndbno":
                            itemNumber=vlus
                        if category=="name":
                            itemName=vlus
                    foodIndex[itemNumber]=itemName

                    print()

foodQuery()

for key,value in foodIndex.items():
    print (key,"\t",value)

