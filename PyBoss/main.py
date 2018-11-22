import datetime
import csv

filename = "employee_data.csv"
id = []
names = []
dob = []
ssn = []
states = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    for row in csvreader:
        id.append(row[0])
        names.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        states.append(row[4])

#separate name
firstname = []
lastname = []
for name in names:
    splitted = name.split(" ")
    firstname.append(splitted[0])
    lastname.append(splitted[1])

#reformat date
for idx in range(0, len(dob)):
    dt = datetime.datetime.strptime(dob[idx], '%Y-%m-%d').strftime('%m/%d/%y')
    dob[idx] = dt

#reformat SSN
modifiedSSN = []
for idx, number in enumerate(ssn):
    modifiedSSN.append("***-**-" + ssn[idx][7:])

#convert state so acronym
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
modifiedState = []
for state in states:
    for key in us_state_abbrev:
        if state == key:
            modifiedState.append(us_state_abbrev[key])

total = zip(id, firstname, lastname, dob, modifiedSSN, modifiedState)
totallist = list(total)
print(totallist)

with open("PyBoss.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    #,fieldnames = ["Emp ID", "First Name", #"Last Name", "DOB", "SSN", "State"])    
    #csvwriter.writeheader()
    csvwriter.writerows(totallist)