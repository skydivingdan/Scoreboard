#!/usr/bin/python
import time, datetime
from urllib import urlopen 

class game(object):
  def __init__(self, team):
    #self.team = team
    self.team = 'Houston' # for testing now 

  def game_string(self, gamestring):
    gs = gamestring.split('   ')
    t1s = gs[0]
    t2s = gs[1].split(' (')[0]
    inning = gs[1].split(' (')[1].split(')')[0]
    base = gs[1].split('%')[1][0:2]
    print t1s
    print t2s
    print inning
    bases = self.getbase(base)
    print bases

  def getbase(self, base):
    BASES = { 'A2' : "Nobody on",
          'A3' : "Runner on First",
          'A5' : "Runner on Second",
          'A7' : "Runner on Third",
          'AC' : "Runners on First and Second",
          'AB' : "Runners at the Corners",
          'BB' : "Runners at Second and Third",
          'B1' : "BASES LOADED" }
    bases = BASES[base]
    return bases 
    
  

def get_scores(): #to follow many teams per url open
  score_url = "http://www.espn.com/mlb/bottomline/scores"
  lines = urlopen(score_url).read().split('mlb_s_left')
  return lines
  
def get_game_line(lines, team):
  for line in lines:
    if team in line:
      s = ' '.join(line.replace('%20',' ').split('=')[1:])
      return s 
  return "You should never see this"

if __name__ == '__main__':
  astro = game('Houston')
  scores = get_scores()
  astro.game_string( get_game_line(scores, 'Houston'))
    
