usernames = ["sina" , "tina" , "mani"]
passwords = ["rasooli" , "rasooli" , "bayat"]

users = dict(zip(usernames,passwords))

print(type(users))

print(users)

for key,value in users.items():
    print(key+" "+value)

print("=====================================")

usernames = ["sina" , "tina" , "mani"]
passwords = ["rasooli" , "rasooli" , "bayat"]
login_date = ["1/1/2021" , "1/2/2021" , "1/3/2021"]

users = zip(usernames,passwords,login_date)

print(users)
print(type(users))

for i in users:
    print(i)