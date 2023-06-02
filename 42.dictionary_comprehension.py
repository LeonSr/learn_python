# dictionary = {key : expression for (key,value) in iterable}

print("example 1")

cities_in_F = {'New york' : 32 ,
                'Boston' : 75 ,
                'Los angeles' : 100 ,
                'Chicago' : 50 }

print("version 1 (easy way) =>")

cities_in_C = {key : round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

print("------------------------------------")

print("version 2 ( long way) =>")

for key,value in cities_in_F.items():
    value = round((value-32)*(5/9))
    print(key,value)


print("====================================")

print("example 2")

weather = {
    'New york' : 'snowing',
    'Boston' : 'sunny',
    'Los angeles' : 'sunny',
    'chicago' : 'sunny',
}

sunny_weather = {key : value for (key,value) in weather.items() if value == 'sunny'}

print(sunny_weather)


print("====================================")

print("example 3")

cities = {'New york' : 32 ,
            'Boston' : 75 ,
            'Los angeles' : 100 ,
            'Chicago' : 50 }

desc_cities = {key : ("warm" if value >= 40  else "cold") for (key,value) in cities.items()}

print(desc_cities)

print("====================================")

def check_temp(value):
    if value >= 70:
        return "hot"
    elif 69>= value >= 40 :
        return "warm"
    else:
        return "cold"
    

cities = {'New york' : 32 ,
            'Boston' : 75 ,
            'Los angeles' : 100 ,
            'Chicago' : 50 }

desc_cities = {key: check_temp(value) for (key,value) in cities.items()}

print(desc_cities)



