# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl' it outputs 5.

s = ''

counter = 0
for letter in s:
    if (letter == 'a' or letter == 'e' or letter == 'i'
            or letter == 'o' or letter == 'u'):
        counter += 1

print('Number of vowels: ' + str(counter))
