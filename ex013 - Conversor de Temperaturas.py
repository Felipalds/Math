#Cabeçalho:

print(30*"\033[31m=\033[m")
cvt = str = "CONVERTENDO TEMPERATURAS"
print(f"\033[1;34m{cvt:^30}\033[m")
print(30*"\033[31m=\033[m")

#Tela de escolhas:


v = int(input("""(1) \033[7mCelcius   \033[m \033[31m->>\033[m \033[7mKelvin    \033[m
(2) \033[7mCelcius   \033[m \033[31m->>\033[m \033[7mFarhenheit\033[m
(3) \033[7mKelvin    \033[m \033[31m->>\033[m \033[7mCelcius   \033[m
(4) \033[7mKelvin    \033[m \033[31m->>\033[m \033[7mFarhenheit\033[m
(5) \033[7mFarhenheit\033[m \033[31m->>\033[m \033[7mCelcius   \033[m
(6) \033[7mFarhenheit\033[m \033[31m->>\033[m \033[7mKelvin    \033[m"""))

#Condicionais e cálculos para cada uma das alternativas:

if v == 1:
    c = float(input("Digite o valor em graus celcius: "))
    k = c + 273.15
    print(f"Celcius: \033[1;31m{c}\033[m ->> Kelvin: \033[1;33m{k:.2f}\033[m")
elif v == 2:
    c = float(input("Digite o valor em graus celcius: "))
    f = 1.8*c + 32
    print(f"Celcius: \033[1;31m{c}\033[m ->> Farhenheit: \033[1;33m{f:.2f}\033[m")
elif v == 3:
    k = float(input("Digite o valor em kelvin: "))
    c = k - 273.15
    print(f"Kelvin: \033[1;31m{k}\033[m ->> Celcius: \033[1;33m{c:.2f}\033[m")
elif v == 4:
    k = float(input("Digite o valor em kelvin: "))
    f = 9*((k - 273.15) / 5) + 32
    print(f"Kelvin:\033[1;31m{k}\033[m ->> Fahrenheit:\033[1;33m{f:.2f}\033[m")
elif v == 5:
    f = float(input("Digite o valor em graus farhenheit: "))
    c = 5*((f-32) / 9)
    print(f"Farhenheit: \033[1;31m{f}\033[m ->> Celcius: \033[1;33m{c:.2f}\033[m")
elif v == 6:
    f = float(input("Digite o valor em graus farhenheit: "))
    k = 5*((f-32)/9) + 273.15
    print(f"Farhenheit: \033[1;31m{f}\033[m ->> Kelvin: \033[1;33m{k:.2f}\033[m")

