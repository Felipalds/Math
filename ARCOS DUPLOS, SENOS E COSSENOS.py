from math import sqrt
from sys import exit
cond = int(input("QUAL VALOR VOCÊ TEM?\n"
                 "[1] SENO \n"
                 "[2] COSSENO\n"))
if cond == 1:
    sen = float(input("SENO: __(MÓDULO)"))
    cos = sqrt(1 - (sen) ** 2)
elif cond == 2:
    cos = float(input("COSSENO: __(MÓDULO)"))
    sen = sqrt(1 - (cos) ** 2)
else:
    print("VALOR ERRADO")
    exit()
quadrante = int(input("QUAL É O QUADRANTE DO ÂNGULO? "))

#Lei fundamental da trigonometria:


if quadrante == 2:
    cos *= -1
elif quadrante == 3:
    sen *= -1
    cos *= -1
elif quadrante == 4:
    sen *= -1

tg = sen / cos
sen2x = 2*sen*cos
cos2x = cos**2 - sen**2
tg2x = 2*tg / (1 - tg ** 2)

print (f"SEN: {sen:.2f}\n"
       f"COS: {cos:.2f}\n"
       f"TG : {tg:.2f}\n"
       f"SEN2x: {sen2x :.2f}\n"
       f"COS2x: {cos2x:.2f}\n"
       f"TG2X: {tg2x:.2f}\n")