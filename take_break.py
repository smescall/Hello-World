import webbrowser
import time

total_breaks = 3
break_count = 0
url = "https://www.youtube.com/watch?v=RB-RcX5DS5A"

print("This program started on"+time.ctime())
while(break_count < total_breaks) :
   time.sleep(10)
   webbrowser.open(url)
   break_count = break_count + 1
