def hello(**kwargs):
    #print("hello "+kwatgs["first"]+" "+kwargs["last"])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title = "mr. ", first = "Sina", middle = 'leon' , last = "rasooli")