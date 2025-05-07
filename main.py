def percentual(x):
    valor = x *100 / total
    return valor



total = float(input("Digite quanto você tem na carteira hoje: "))

while True:
    rendaFixa = float(input("Quanto desse valor está na renda fixa: "))
    acoes = float(input("Quanto desse valor está em ações: "))
    fii = float(input("Quanto desse valor está em FIIs: "))
    if acoes + rendaFixa + fii != total:
        print("Valores excedem o valor total. Digite novamente")
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

def ideal(ideais, atuais):
    if atuais == ideais:
        return "Está balaneceado"
    elif atuais > ideais:
        return f"O valor está {atuais - ideais}% acima do ideal"
    else:
        return f"O valor está {ideais - atuais}% abaixo do ideal "

print(f"""Ideal renda fixa = {fixaIdeal} | Atual: {divisao["Renda fixa"]} -> {ideal(fixaIdeal, divisao["Renda fixa"])}
Ideal ações = {acoesIdeal} | Atual: {divisao["Ações"]} -> {ideal(acoesIdeal, divisao["Ações"])}
Ideal FIIs = {fiiIdeal} | Atual: {divisao["FIIs"]} -> {ideal(fiiIdeal, divisao["FIIs"])}""")

aporte = float(input("Digite o valor que você irá aportar: "))
novoTotal = total + aporte

