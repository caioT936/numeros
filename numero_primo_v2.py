 
def ePrimo(x):
  y = 2
  while 1==1:
    if x == 2 or x == 3:
      return True
      break 
    elif x==1:
      return False
      break
    elif x%y == 0:
      return False 
      break
    elif y==x-1:
      return True
      break
    y+=1

def main():
  x = int(input('Digite um valo:'))
  if (ePrimo(x)):
    print('e primo  porrrrr')
  else:
    print('nao e primo caralho')

if __name__ == '__main__':
    main()