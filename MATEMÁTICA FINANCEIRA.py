print("\033[31m BOLSA DE VALORES DE LIPE RICO \033[m")
print(35*"=")
print(" ")
capital = float(input("QUAL É O \033[32mCAPITAL INICIAL\033[m? :______"))
monthly: float = float(input("QUAL É O VALOR A SER APLICADO \033[32mMENSALMENTE\033[m?: _____"))
rate = float(input("QUAL É A \033[32mTAXA\033[m A SER APLICADA (em % a.m.) ? :______"))
time = int(input("QUANTOS \033[32mANOS\033[m O DINHEIRO FICARÁ RENDENDO? :_____"))

rate /= 100
time *= 12  # transfom years in months
time2 = int(1)
amount = 0
while time2 <= time:

    amount = capital * (1 + rate) ** time2
    juros = amount - capital
    capital = capital + monthly
    total = capital + juros
    print(f"\033[31mMÊS\033[m \033[33m{time2}\033[m - - \033[34mMONTANTE\033[m:\033[33m R${total:.3f}\033[m")
    if time2 % 12 == 0:
        time3 = time2 // 12
        print(f"\033[35mANO\033[m \033[33m{time3}\033[m - - \033[34mMONTANTE\033[m: \033[33mR${total:.3f}\033[m")
    time2 += 1
