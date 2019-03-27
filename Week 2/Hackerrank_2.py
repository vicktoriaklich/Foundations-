# Challenges and Task of Week 2 on Hackerrank

"""
Designer Door Mat
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""
height, length = map(int, input().split())
for i in range(0, height // 2):
    s = '.|.' * (i * 2 + 1)
    print(s.center(length,'-'))
print('WELCOME'.center(length, '-'))
for i in range(height // 2 - 1, -1, -1):
    s = '.|.' * (i * 2 + 1)
    print(s.center(length,'-'))



# Find the Torsional Angle


