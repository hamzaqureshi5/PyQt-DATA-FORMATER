import datetime
import time
p_time = str(time.strftime("%H_%M_%S", time.localtime()))
p_date = str(datetime.date.today().strftime("%Y_%m_%d"))
out =p_date+"_"+p_time

print(out)