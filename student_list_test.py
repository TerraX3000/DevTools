import re
import json

def getChattStateANumber(studentSets) :
    chattStateANumber = re.findall("^A[0-9]+", studentSets)
    # Check if student set is for a student or a team
    if len(chattStateANumber) < 1 :
        chattStateANumber = 'team'
    else :
        chattStateANumber = chattStateANumber[0]
    return chattStateANumber

def getName(studentSets) :
    name = studentSets.split('_')
    # Check if student set is for a student or a team
    if len(name) == 1 :
        lastName = name[0]
        firstName = ''
    else :
        lastName = name[1]
        firstName = name[2]
    return firstName, lastName

student_file_name = input('Enter the name of the student input file (in CSV format)')
if len(student_file_name) < 1 : student_file_name = 'FET Schedule Input Files 2020-2021 - FET Students - Juniors - New Te.csv'
student_file = open(student_file_name)

teamStudentMap = dict()
for row in student_file :
    rowValues = row.split(',')
    teamName = rowValues[2]
    studentSets = rowValues[4]
    chattStateANumber = getChattStateANumber(studentSets)
    firstName, lastName = getName(studentSets)
    #studentSets = re.search('A[0-9]+', row)
    if len(studentSets) == 0 : continue
    if teamName == 'Group' : continue
    if teamName not in teamStudentMap :
        teamStudentMap.update({teamName : {"students" : {}}})
    teamStudentMap[teamName]["students"].update({chattStateANumber : {"firstName" : firstName, "lastName" : lastName}})

print(teamStudentMap)
jsonTeamStudentMap = json.dumps(teamStudentMap, indent=4, separators=("", " = "))
print(jsonTeamStudentMap)

list_of_teams = ['Junior Team 01', 'Junior Team 02', 'Junior Team 03']
list_of_ANumbers = ['A00336279', 'A00337863', 'A00349928', 'A00336427']

for studentSets in list_of_teams :
    if studentSets in teamStudentMap :
        #print(Chatt_State_A_Number, " - ", teamStudentMap[Chatt_State_A_Number]["students"])
        for student in teamStudentMap[studentSets]["students"] :
            firstName = teamStudentMap[studentSets]["students"][student]["firstName"]
            lastName = teamStudentMap[studentSets]["students"][student]["lastName"]
            print(student, firstName, lastName)

# if chattStateANumber not in fullSchedule :
#     fullSchedule.update({chattStateANumber : {"firstName" : firstName,
#     "lastName" : lastName,
#     "activities" : { }}})
#
# # If this activity ID is already in fullSchedule, only update the endTime and move on
# if activityId in fullSchedule[chattStateANumber]["activities"] :
#     fullSchedule[chattStateANumber]["activities"][activityId]["endTime"] = endTime
# # If this activity is not in fullSchedule, populate the scheduleRow dictionary with key-value pairs
# else:
#     scheduleRow = {
#     "day" : day,
#     "startTime" : startTime,
#     "endTime" : endTime,
#     "subject" : subject,
#     "campus" : campus,
#     "comments" : comments,
#     "activityTags" : activityTags,
#     "mergedActivity" : False
#     }
#     # Add the scheduleRow to the full schedule dictionary
#     fullSchedule[chattStateANumber]["activities"].update({activityId : scheduleRow})
#     activityCounter = activityCounter + 1
# currentFetRow = currentFetRow + 1
