# import modules

import calculator as c


ch = int(input("Enter your choice 1. add 2. sub 3. multiply 4. divide"))

if ch == 1:
    print(c.add(10,20))
elif ch==2:
    print(c.sub(10,2))
elif ch==3:
    print(c.multiply(10,5))
elif ch==4:
    print(c.divide(100,4))
else:
    print("Invalid choice ")