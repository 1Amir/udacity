import time
import webbrowser
breaks = 0
totalamount = 5
print "this program started at "+ time.ctime()
while breaks < totalamount:
  time.sleep(7200)
  webbrowser.open("https://www.youtube.com/watch?v=vE2ETqUGj6Q")
  breaks = breaks + 1
