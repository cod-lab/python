'''

import math                     #python header file/inbuilt module, import entire file

print(math.factorial(5))

from math import factorial      #import only factorial fn from math module/header file

print(factorial(5))

from math import factorial as fact              #renaming factorial fn to 'fact' according to user and using it as fact

print(fact(5))

'''

# math fns

import math

print(math.floor(15/2))
print(math.gcd(12,6))
print(math.log(math.e))
print(math.log(16,2))                           #16-value,2-base,output-exponent
print(math.pi)
print(math.inf)                                 #+inf - +infinity
print(-math.inf)                                #-inf - -infinity
print(sum([1,2,3,4.5,5]))
print(max([1,2,3,4.5,5]))
print(min([1,2,3,4.5,5]))
