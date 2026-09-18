numn = int(input("Enter a number (Numerator):  "))
numd = int(input("Enter a number (Denominator):  "))
if numn%numd == 0:
    print("\n" +str(numn)+ " is divisible by " +str(numd))
else:
    print("\n" +str(numn)+ " is not divisible by " +str(numd))