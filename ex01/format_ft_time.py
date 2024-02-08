import time
import datetime

# return number of seconds since epoch 
seconds = time.time()

# return string representing local time
date_time = datetime.datetime.today().strftime("%b %d %Y")

print("Seconds since January 1, 1970: ", seconds)
print(date_time)