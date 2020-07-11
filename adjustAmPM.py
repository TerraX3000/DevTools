from datetime import datetime
import re

def extractStartEndTimeFromActivityTag(activityTags) :
    # Parse the start and end times from the activityTags
    times = re.findall('[0-9]+:[0-9]+',activityTags)
    print(times)
    startTime = adjustTimeObjectForAmPm(createTimeObject(times[0]))
    endTime = adjustTimeObjectForAmPm(createTimeObject(times[1]))
    print(startTime,endTime)
    return startTime, endTime

def adjustTimeObjectForAmPm(dateTimeObject) :
    print(dateTimeObject.hour)
    if dateTimeObject.hour > 0 and dateTimeObject.hour < 8 :
        newHour = dateTimeObject.hour + 12
        adjustedTimeStr = str(newHour) + ':' + str(dateTimeObject.minute)
        dateTimeObject = createTimeObject(adjustedTimeStr)
    return dateTimeObject

def createTimeObject(timeString) :
    # Parse a time string into a datetime object
    timeObject = datetime.strptime(timeString, "%H:%M")
    return timeObject

activityTags = 'CS 1:00 - 8:00'

extractStartEndTimeFromActivityTag(activityTags)
