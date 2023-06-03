import time
# print(time.ctime(0))        # epoch = when your computer thinks time began 

# print(time.time())          #return time since epoch

# print(time.ctime(time.time()))

# time_object = time.localtime()
# print(time_object)

# local_time = time.strftime("year : %Y month : %B day: %d time : %H : %M : $S", time_object)     # for more info visit https://docs.python.org/3/library/time.html
# print(local_time)

# time_utc = time.gmtime()
# print(time_utc)

# time_string = "20 April, 2024"
# time_object = time.strptime(time_string , "%d %B, %Y")
# print(time_object)

# (year , month , day , hour , monutes , secs , day of the week , day of the year , dst)
# time_tuple = (2023 , 4 , 20 , 4 ,20 , 0 , 0 , 0 , 0)
# time_string = time.asctime(time_tuple)
# print(time_string)
# time_epoch = time.mktime(time_tuple)
# print(time_epoch)

