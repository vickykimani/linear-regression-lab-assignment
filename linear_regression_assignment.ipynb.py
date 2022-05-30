from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import random
from random import randint

##random_n_digits is used to generate a random integer of length n
def random_n_digits(n): 
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

##ensure that a generated identifier is unique
def unique_rand(rands, n):
    new_int = random_n_digits(n)
    if new_int not in rands:
        rands.append(new_int)
    else:
        unique_rand(rands, n)
    return new_int, rands

##generate office price
def generate_price():
    price = ''
    digits = randint(1, 4)
    price += str(random_n_digits(digits))
    price += '.' + str(random_n_digits(2))
    return price


##create office data set
office = {}
office_sizes = []

for i in range(0, 100):
    office[i]={}
    office[i]['office_price'] = generate_price()
    office[i]['office_size'], office_sizes = unique_rand(office_sizes, 4)

office_df = pd.DataFrame(office).T
print(office_df)

office_df.to_csv('office.csv', index=False)



##gradient descent is an optimization algorithm that is mainly used to find the minimum of a function

##find slopes for each column

slopes = df.apply(lambda x: np.polyfit(df.index, x, 1)[0])

for i in df.columns:
    plt.scatter(df.index, df[i], label=i)
    plt.plot(np.polyval(np.polyfit(df.index, df[i], 1), df.index))

plt.legend()
plt.show()

















    
