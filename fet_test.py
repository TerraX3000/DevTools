
import json

schedule = {
    "a12345678" :
    {"firstName" : "Testy",
    "lastName" : "Tester",
    "activities" :
        {

        1 : {
            "subject" : "Algebra II",
            "day" : "Monday",
            "startTime" : "09:30",
            "endTime" : "10:30",
            "campus" : "STEM School",
            "mergedActivity" : False
            },
        2 : {
            "subject" : "Algebra II",
            "day" : "Tuesday",
            "startTime" : "09:30",
            "endTime" : "10:30",
            "campus" : "STEM School",
            "mergedActivity" : False
            },
        3 : {
            "subject" : "Algebra II",
            "day" : "Wednesday",
            "startTime" : "09:30",
            "endTime" : "10:30",
            "campus" : "STEM School",
            "mergedActivity" : False
            }
        }
    },
    "a87654321" :
    {"firstName" : "Testy",
    "lastName" : "Tester",
    "activities" :
        {
        1 : {
            "subject" : "Algebra II",
            "day" : "Monday",
            "startTime" : "09:30",
            "endTime" : "10:30",
            "campus" : "STEM School",
            "mergedActivity" : False
            },
        2 : {
            "subject" : "Algebra II",
            "day" : "Tuesday",
            "startTime" : "09:30",
            "endTime" : "10:30",
            "campus" : "Chattanooga State",
            "mergedActivity" : False
            },
        3 : {
            "subject" : "Algebra II",
            "day" : "Wednesday",
            "startTime" : "09:30",
            "endTime" : "10:30",
            "campus" : "STEM School",
            "mergedActivity" : False
            }
        }
    }
}

chattStateANumber = 'a12345679'
if chattStateANumber not in schedule :
    print('student not in schedule!')
    schedule.update({chattStateANumber : {"firstName" : "Testy",
    "lastName" : "Tester",
    "activities" : { }}})
# Loop through each student's schedule and merge classes spread across days into consolidated class listings
for student in schedule :
    print(student, schedule[student]["firstName"],schedule[student]["lastName"])
    for activity in schedule[student]["activities"] :
        #print(schedule[student]["activities"][activity])
        subject = schedule[student]["activities"][activity]["subject"]
        day = schedule[student]["activities"][activity]["day"]
        startTime = schedule[student]["activities"][activity]["startTime"]
        endTime = schedule[student]["activities"][activity]["endTime"]
        campus = schedule[student]["activities"][activity]["campus"]
        mergedActivity = schedule[student]["activities"][activity]["mergedActivity"]
        print(activity, subject, day, startTime, endTime, campus, mergedActivity)
        # Compare each class to all of the other classes to find classes to merge
        for comparisonActivity in schedule[student]["activities"] :
            # Don't compare the activity if it's the same activity
            if activity == comparisonActivity : continue
            # Don't compare the activity if it was already been merged
            if mergedActivity == True : continue
            # Don't compare the comparison activity if it was aleady been merged
            if schedule[student]["activities"][comparisonActivity]["mergedActivity"] == True : continue
            # Extract the parameters from the oomparison activity
            comparisonSubject = schedule[student]["activities"][comparisonActivity]["subject"]
            comparisonDay = schedule[student]["activities"][comparisonActivity]["day"]
            comparisonStartTime = schedule[student]["activities"][comparisonActivity]["startTime"]
            comparisonEndTime = schedule[student]["activities"][comparisonActivity]["endTime"]
            comparisonCampus = schedule[student]["activities"][comparisonActivity]["campus"]
            # Check to see if the activities are the same class but on different days
            if subject == comparisonSubject and startTime == comparisonStartTime and endTime == comparisonEndTime and campus == comparisonCampus :
                # If they are the same class, update the day parameter in the activity and
                # set the mergedActivity flag in the comparisonActivity to True so it's ignored
                #print('--- Merge this class:', schedule[student]["activities"][comparisonActivity])
                newDay = schedule[student]["activities"][activity]["day"] + schedule[student]["activities"][comparisonActivity]["day"]
                schedule[student]["activities"][activity]["day"] = newDay
                schedule[student]["activities"][comparisonActivity]["mergedActivity"] = True
                continue
            #print('---',comparisonActivity,comparisonSubject,comparisonDay,comparisonStartTime,comparisonEndTime)

prettySchedule = json.dumps(schedule, indent=4, separators=(". ", " = "))
print(prettySchedule)
