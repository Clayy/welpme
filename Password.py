testScore = int(input('Enter test score: '))
if testScore > 100:
   print ('Please input the correct data. You cannot have more than 100%') 
if testScore >= 90 and testScore < 100:
        print('Your grade is A')
elif testScore >= 80 and testScore < 100:
        print('Your grade is B')
elif testScore >= 70 and testScore < 100:
        print('Your grade is C')
elif testScore >= 60 and testScore < 100:
        print('Your grade is D')
else:
        print('Your grade is F')
def test(testScore): 
    if testScore < 1:
        print('Please input the correct data. you cannot have less that 0%')
        print()
        
