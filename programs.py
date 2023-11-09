# create a class which acts as an iterable

l = [1, 2, 3, 4]

class Sample:

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return iter(self.iterable)


s = Sample(l)
# print(dir(s))
#
# for item in s:
#     print(item)

#################################################################################################
# custom iterator to generate the numbers from 1 to 10

class Numbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        a = self.start
        self.start += 1
        return a


n = Numbers(1, 5)

# for item in n:
#     print(item)

# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))

#################################################################################################
# from 10 to 1

class CountDown:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            raise StopIteration

        a = self.start
        self.start -= 1
        return a

#####################################################################################################
# to return all the even numbers from 1 to 50

class Even:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        a = self.start
        self.start += 1

        if a % 2 == 0:
            return a

####################################################################################################
# custom iterators to return prime numbers from 1 to 50

class Prime:

    def __init__(self, end, start=0):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        num = self.start
        self.start += 1

        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break

            else:
                return num

p = Prime(10)

for i in p:
    if i:
        print(i)

#############################################################################################

# return even indexed elements in the list
# return the elements in the list in reversed order


















































