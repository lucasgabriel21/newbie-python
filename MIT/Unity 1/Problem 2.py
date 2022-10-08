# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl' it outputs 2.

s = 'azcbobobegghakl'

counter = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        counter += 1

print('Number of times bob occurs is: ' + str(counter))
