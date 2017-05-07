from time import sleep
from datetime import time, datetime
import sys

hour = int(sys.argv[1])
min = int(sys.argv[2])
delayTime = time(hour, min)

while datetime.today().time() < delayTime:
  print "\r not yet",
  sys.stdout.flush()
  sleep(10)

print "I have completed my time"
