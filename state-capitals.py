import random

state_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
}

counterQuestions = 0 # Represents the number of questions asked to the user
counterCorrect = 0

for state in random.sample(list(state_capitals), 50):
    capital = state_capitals[state]
    capital_guess = input('What is the capital of {}? '.format(state))
    if capital_guess == 'skip':
        #print('The Capital of {} is {}.'.format(state, capital)) #study mode - use comment feature to turn this on/off.
        counterQuestions = counterQuestions + 1    
        continue
    elif capital_guess == 'quit':
        break
    elif capital_guess == capital:
        print('Correct! Nice job!')
        counterCorrect = counterCorrect + 1
        counterQuestions = counterQuestions + 1
    else:
        print('Incorrect.  The Capital of {} is {}.'.format(state, capital))
        counterQuestions = counterQuestions + 1

score = (counterCorrect / counterQuestions) * 100
counterIncorrect = counterQuestions - counterCorrect
print('All done. Your score is ' + str(score) + '% correct, or ' + str(counterCorrect) + ' out of ' + str(counterQuestions) + ' (' + str(counterIncorrect) + ' incorrect)')