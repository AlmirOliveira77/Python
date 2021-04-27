cateto1 = float(input())
cateto2 = float(input())
import math
a = (cateto1 ** 2) + (cateto2 ** 2)
hipotenusa = math.sqrt(a)

#if cateto1 - cateto2 < hipotenusa and hipotenusa - cateto1 < cateto2 and hipotenusa - cateto2 < cateto1:
print(round(hipotenusa, 2))
