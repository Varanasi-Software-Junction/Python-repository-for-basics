def f1(n,direction):
      r=range(1,n+1)
      if direction==False:
          r=reversed(r)
      for row in r:
        for col in range(1,row+1):
            print("0",end="")
        print()
n=7
mid=(n+1)/2
def f2(n,direction):

   for row in range(1,n+1):
        for col in range(1,n+1):
            condition=(row+col)==(mid+1) or(row-col)==(-mid+1) or(row-col)==(mid-1) or(row+col)==(n+mid)
            if condition:
                print(0,end=" ")
            else:
                print(" ",end=" ")
        print()

f2(7,False)
f1(5,False)



