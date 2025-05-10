def percentual(x):
    valor = x *100 / total
    return valor

def ideal(ideais, atuais):
    if atuais == ideais:
        return "Está balaneceado"
    elif atuais > ideais:
        return f"O valor está {atuais - ideais:.2f}% acima do ideal"
    else:
        return f"O valor está {ideais - atuais:.2f}% abaixo do ideal "
def balancear(total, y):
    porcento = y/100
    return total * y

total = float(input("Digite quanto você tem na carteira hoje: "))

while True:
    rendaFixa = float(input("Quanto desse valor está na renda fixa: "))
    acoes = float(input("Quanto desse valor está em ações: "))
    fii = float(input("Quanto desse valor está em FIIs: "))
    total = rendaFixa + acoes + fii
    if total != total:
        print("A soma dos valores não dá o valor total. Digite novamente")
    else:
        break

divisao = {"Renda fixa": percentual(rendaFixa), "Ações": percentual(acoes), "FIIs": percentual(fii)}
for chave, valor in divisao.items():
    print(f"{chave} : {valor:.2f}%")

while True:
    print("Qual a porcentagem da sua carteira que deve estar em")
    fixaIdeal = float(input("Renda fixa: "))
    acoesIdeal = float(input("Ações: "))
    fiiIdeal = float(input("FIIs: "))
    if fixaIdeal + acoesIdeal + fiiIdeal != 100:
        print("Percentuais incorretos")
    else:
        break



print(f"""Ideal renda fixa = {fixaIdeal:.2f}% | Atual: {divisao["Renda fixa"]:.2f}% -> {ideal(fixaIdeal, divisao["Renda fixa"])}
Ideal ações = {acoesIdeal:.2f}% | Atual: {divisao["Ações"]:.2f}% -> {ideal(acoesIdeal, divisao["Ações"])}
Ideal FIIs = {fiiIdeal:.2f}% | Atual: {divisao["FIIs"]:.2f}% -> {ideal(fiiIdeal, divisao["FIIs"])}""")

aporte = float(input("Digite o valor que você irá aportar: "))
novoTotal = total + aporte

