Monday = (1,'M')
Tuesday = (2,'T')
Wednesday = (3,'W')
Thursday = (4,'R')
Friday = (5,'F')

days = list()
plusdays = list()
days.append(Monday)
plusdays.append(Friday)
plusdays.append(Wednesday)
days3 = days + plusdays
print(days, type(days))
print(plusdays, type(plusdays))
print(days3, type(days3))
days.append(plusdays)
print(days, type(plusdays))
days3.sort()
print(days3)
if (1,'M') in days3 :
    print('This list includes Monday')
orderedDays = ''
for day in days3 :
    orderedDays = orderedDays + day[1]
print(orderedDays)
testDay = Thursday
if testDay in days3 :
    print('Test day is in days!')
