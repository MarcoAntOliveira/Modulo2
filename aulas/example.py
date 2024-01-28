i = int(input("digite o termo que vc quer"))
var1 = 1
var2 = 0
var3 = 0

for n in range(1, i):
    var3 = var1 + var2
    var1 = var2
    var2 = var3
    
    print(var2)