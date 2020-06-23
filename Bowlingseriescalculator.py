g1 = int(input('Please enter your game 1 score.  '))
g2 = int(input('Please enter your game 2 score.  '))
g3 = int(input('Please enter your game 3 score.  '))

total_series = g1+g2+g3
avg = (g1+g2+g3)/(3)

print('In this series, your total was', total_series, ', and your average score per game was', int(avg),'.')
