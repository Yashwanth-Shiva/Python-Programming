from itertools import groupby
for k, g in groupby(input()):
   print((len(list(g)),int(k)),end=" ")
