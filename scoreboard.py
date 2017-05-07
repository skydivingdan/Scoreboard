#!/bin/python
import time
from datetime import datetime, time
from urllib import urlopen


SCORE_URL="http://www.espn.com/mlb/bottomline/scores"
#SCORE_URL="http://127.0.0.1/scores.html"     # Local copies for each condition. 
#SCORE_URL="http://127.0.0.1/scores-between.html"
#SCORE_URL="http://127.0.0.1/score-inplay.html"   
#SCORE_URL="http://127.0.0.1/before-game.html"

 #Opens the URL and gets the first line and splits it using a unique identifier. 
 #If I want to expand this I'll have to alter this to accept a variable for 
 #The league currently 'mlb'.  Could be 'nfl' etc...
#SB = urlopen(SCORE_URL).readlines()[0].split('&mlb_s_left')

 #Setting up the Libary for Base positions.  I mapped these out myself,
 # so not promising that they work... 
BASES = { '%A2' : "Nobody on",
          '%A3' : "Runner on First",
          '%A5' : "Runner on Second",
          '%A7' : "Runner on Third",
          '%AC' : "Runners on First and Second",
          '%AB' : "Runners at the Corners",
          '%BB' : "Runners at Second and Third",
          '%B1' : "BASES LOADED"
}
def GET_SCORE():
  SB = urlopen(SCORE_URL).readlines()[0].split('&mlb_s_left')
  for i in range(1,len(SB)):
    if "Houston" in SB[i]: 
    # print SB[i].replace('%20',' ').replace('^',''),"\n\n"
    # print SB[i][SB[i].find('=')+1:]
    # print SB[i][2:].replace('%20',' ').replace('^','')
      HOU = SB[i][2:].replace('%20',' ').replace('^','')
      SHOU = HOU.split('&mlb_s_right')
      print  SHOU[0],"  :",  
      STATS = SHOU[1][SHOU[1].find('=')+1:]
      OUTS = STATS.split('         ')
      print OUTS[1], "     ", BASES.get(OUTS[0]), " "

def Get_game(tf):  
  SB = urlopen(SCORE_URL).readlines()[0].split('&mlb_s_left')
  for i in range(1,len(SB)):
    if tf in SB[i]:
      LINE = SB[i][SB[i].find('=')+1:].replace('%20',' ').replace('^','')
      #INNING, status  = find_Inning(LINE.split('(')[1].split(')')[0]) 
      #if status = 1:
    return LINE    

  #This finds if the Game is in play, not yet started, or Finished. and sets Status
def find_Inning(INNING): 
  if "TOP" in INNING or "BOT" in INNING:
    print INNING 
    status = 0     # In play
    return INNING, status
  elif "FINAL" == INNING:
    print "Thats all folks"
    status = 2      # Game over man,  Game over
  elif "ET" in INNING: 
    status = 1              #Game hasn't started
    #TIMECONV(INNING)
  else:
    print "FUCK\nFUCK\nFUCK\nFUCK\n\n\n\nF U C K ! !" #Something has gone sideways
    status = "Over 9,000!!"
  return INNING, status


 #This Takes the time as a string and turns it into 
 #something more useful to me. time should be a string that 
 # resembles the "7:10 PM ET" format.   I haven't seen any other 
 # timezones used.  I'll have to update the code if they start.  
 #
 # This is assuming we're in CT as thats where I live and where the person
 # I'm writing this for lives.  Feel free to change it. Won't hurt my feelings. 
def TIMECONV(time):
  mstring = time.split(' ')
  ampm = mstring[1]
  timez = mstring[2]
  hour, min = map(int, mstring[0].split(':'))
  if ampm == "PM":
    hour = hour + 12 #Because 24 hour clocks are better
  if timez == "ET":
    hour = hour - 1 
  hour = hour - 1  # So we can start the hour countdown timer. 
  timeDelay = time(hour, min)
  return timeDelay
 

def pregame(startTime, opponent):
  delay = TIMECONV(startTime)
  print "The game starts at %s!!" % delay 
  while delay > datetime.now().time():
    pass
  
def IN_GAME(tf):
  GAME_STR = Get_game(tf)
  Inning, status = find_Inning(GAME_STR.split('(')[1].split(')')[0])
  

IN_GAME('Houston')
