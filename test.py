import time
import numpy as np

start = time.time()

# vectorized sum - using numpy for vectorization
# np.arange create the sequence of numbers from 0 to 1499999
print(np.sum(np.arange(1500000000)))

end = time.time()

print(end - start)
print("--------------------------")
total = 0
# iterating through 1.5 Million numbers
for item in range(0, 1500000000):
    total = total + item


print('sum is:' + str(total))
end = time.time()

print(end - start)