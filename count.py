import time

from sys import argv, stdout 
try:
  min = int(argv[1])
  sec = int(argv[2])
except:
  print "Arguments need to be intergers"
  print "EX.  './count.py 5 23' would count down for 5 min and 23 seconds"
  quit() 

print "Counting down for %d and %d seconds" % (min, sec)

i = min*60 + sec
while i > 0:
  print  "\r%2d : %2d   " % (min, sec),
  stdout.flush() 
  if sec == 0:
    sec = 60
    min = min - 1 
  sec = sec - 1
  i = i - 1
  time.sleep(1)
print "\n\nDone"
time.sleep(2)

