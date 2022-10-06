import math
import sys
import lib.util as util
import lib.vnstat as vnstat

def BaseValidations():
  if not util.isVnstatInstalled():
    sys.exit('vnstat is not running. Please configure it first.')

def OneDecPlace(num):
  return math.floor(num*10)/10

BaseValidations()
for intf in vnstat.get5MinAsJson()['interfaces']:
  traffic = intf['traffic']['fiveminute'][0]
  seconds = 5 * 60
  print ('{:>10}: rx = {:>10} B/s, tx = {:>10} B/s'.format(intf['name'], OneDecPlace(traffic['rx']/seconds), OneDecPlace(traffic['tx']/seconds)))