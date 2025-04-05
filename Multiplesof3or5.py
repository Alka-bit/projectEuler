#Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

def num(n):
  list = []
  for i in range(1, n):
    if i%3==0 or i%5==0:
      list.append(i)
  return sum(list)
