def hello(**kwargs):
    # print("hello " + kwargs['first'] + ' ' + kwargs['last'] )
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(first='sina' , middel="leon" , last= "rasooli")