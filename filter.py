# return all the strings starting with vowels in the given sentence

s = 'apple orange mango grapes'
l = s.split()

def vowel(string):
    if string[0].lower() in 'aeiou':
        return string

print(list(filter(vowel,s.split())))

###################################################################
# print odd numbers in the range 1-50

l = list(range(1,51))
def odd_(num):
    if num%2!=0:
        return num

print(list(filter(odd_,l)))

######################################################################
# return a list of string with odd length

l = ["gmail", "google", "instagram", "facebook", "yahoo"]
def odd_(string):
    if len(string)%2==0:
        return string

print(list(filter(odd_,l)))

########################################################################
# return only +ve value in the list

l = [1, -2, -3, 4 , 5, 6]
def pos(num):
    if num<0:
        return num

print(list(filter(pos,l)))

#######################################################################
# print prime numbers from 1-50

l = list(range(1,51))
def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return num

print(list(filter(prime,l)))
