#in the lopplist.py instead of using the range len some list technique we can simmple call the enumerate() function instead

supplies = ['pens' , 'staplers' , 'binders']
for index, item in enumerate(supplies):
    print("Index " + str(index) + ' in supplies is : ' + item) 