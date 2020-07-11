from datetime import datetime

timeStr = '14:00'
print(timeStr)
timeObject = datetime.strptime(timeStr,"%H:%M")
print(timeObject, type(timeObject))
timevalue_12hour = timeObject.strftime( "%-I:%M")
print(timevalue_12hour)

from datetime import timedelta
delta1 = timedelta(minutes=57)
print(delta1,type(delta1))
newTime = timeObject + delta1
print(newTime)
