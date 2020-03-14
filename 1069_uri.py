'''
1069 Data structures and libraries 
John is working in a diamond mine, trying to extract the highest number of diamond "<>". He must exclude all sand particles found "." in this process and after a diamond can be extracted, new diamonds can be formed. If he has as an input. <... << .. >> ....> .... >>>. three diamonds are formed. The first is taken from <..> resulting. <... <> ....> .... >>>. The second diamond is then removed, leaving. <.......> .... >>>. The third diamond is then removed, leaving at the end ..... >>>. without the possibility of extracting new diamonds.

Input
Read an integer N that is the number of test cases. Then follows N lines each up to 1000 characters, including "<" ,">" and "."

Output
You must print the amount of diamonds that can be extrated in each test case.
'''

number_of_cases = int(input())
lista = []
n_diamond = []

for case in range(number_of_cases):
   x = input()
   lista.append(x)

for case in lista:
   n = 0

   while '<' in case:

      x = case.find('<')
      y = case.find('>')
      if x < y:
         n += 1
         case = case[x + 1: y] + case[y + 1 :]
      elif '>' in case[x:]:
         case = case[x:]
      else:
         break

   n_diamond.append(n)

for number in n_diamond:
   print(number)
