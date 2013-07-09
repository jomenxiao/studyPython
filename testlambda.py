g = lambda x:x**2

print g(12)

import re

print re.sub(r'\w+', lambda a: a.group().upper(), 'hello world')

def test(a, b):
    if a > b:
        for testNumber in range(b, 0, -1):
            if a % testNumber == 0 and b % testNumber == 0 :
                forTestNumber = testNumber
                print testNumber ,'is ok'
                break
    else:
        for testNumber in range(a, 0, -1):
            if a % testNumber == 0 and b % testNumber == 0 :
                forTestNumber = testNumber
                print testNumber ,'is ok'
                break
    leastCommonMultiple = a * b / forTestNumber
    print leastCommonMultiple
    
test(82, 92)
    