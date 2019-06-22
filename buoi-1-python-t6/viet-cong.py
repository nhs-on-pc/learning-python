def cong(*args):
   temp = 0
   for num in args:
       temp += num
   return temp

def cong_simpler(*args):
   return sum(args)

print(cong(1, 2, 3, 4, 5, 6))