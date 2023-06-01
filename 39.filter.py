friend = [
    ("sina",20),
    ("tina",20),
    ("bahar",24),
    ("asal",18),
    ("sogand",14),
    ("mani",19)
]
age = lambda data : data[1] >= 18
drinking_buddoes = list(filter(age , friend))

for i in drinking_buddoes:
    print(i)