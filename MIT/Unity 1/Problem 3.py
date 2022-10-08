# Write a program that prints the longest substring of s
# in which the letters occur in alphabetical order. (a<b<c...)
# For example, if s = 'azcbobobegghakl',
# then your program should print 'beggh'.

s = 'azcbobobegghakl'  # main string

sub_string = ''  # longest substring
temp = ''  # temporary substring

for i in range(len(s) - 1):

    if s[i + 1] >= s[i]:  # check if a pair of characters are in order

        if len(temp) == 0:  # making a temporary string by concatenation
            temp = s[i] + s[i + 1]
        else:
            temp += s[i + 1]

        if len(temp) > len(sub_string):  # stores the longest substring
            sub_string = temp

    else:  # reinitiates the temporary string when test fails
        temp = ''

if sub_string == '':
    sub_string = s[0]

print('Longest substring in alphabetical order is: ' + sub_string)
