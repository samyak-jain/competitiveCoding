T = input()
ls = []
while T:
    x = raw_input()
    y = raw_input()
    z = ''
    for i in range(len(x)):
      if x[i] == 'W' and y[i] == 'W':
        z += 'B'
      elif x[i] == 'B' and y[i] == 'B':
        z += 'W'
      else:
        z+= 'B'
    ls.append(z)
    T-=1

for i in ls:
  print i