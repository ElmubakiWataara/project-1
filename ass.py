
#def ismultiple(n,m):
 #   if m % n == 0:
  #      return True
   # else:
    #    return False
#print (ismultiple(n,m))


n=int(input("enter number"))
m=int(input("enter 2nd number"))
def ismultiple(n,m):
    if m % n > 0:
        return False
    elif m % n == 0:
        return True
print(ismultiple(n,m))
    