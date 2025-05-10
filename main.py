#Função para descobrir o percentual dos ativos dentro da carteira
def percentual(x, y):
    valor = x * 100 / y
    return valor


#Função para descobrir quanto do valor total deveria estar em cada ativo
def ideal(ideais, atuais):
    if atuais == ideais:
        return "Está balaneceado"
    elif atuais > ideais:
        return f"O valor está {atuais - ideais:.2f}% acima do ideal"
    else:
        return f"O valor está {ideais - atuais:.2f}% abaixo do ideal "

#Função para descobrir quanto deve estar em cada ativo depois de contabilizar o novo

def valoresNovoAporte(total, y):
    porcento = y/100
    return total * porcento

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
if total == 0:
    print("Você ainda não tem investimentos")
else:
    divisao = {"Renda fixa": percentual(rendaFixa, total), "Ações": percentual(acoes, total), "FIIs": percentual(fii, total)}
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
if total == 0:
    print(
        f"""Ideal renda fixa = {fixaIdeal:.2f}% | Atual: 0% 
Ideal ações = {acoesIdeal:.2f}% | Atual: 0% 
Ideal FIIs = {fiiIdeal:.2f}% | Atual: 0% """)

else:

    print(f"""Ideal renda fixa = {fixaIdeal:.2f}% | Atual: {divisao["Renda fixa"]:.2f}% -> {ideal(fixaIdeal, divisao["Renda fixa"])}
Ideal ações = {acoesIdeal:.2f}% | Atual: {divisao["Ações"]:.2f}% -> {ideal(acoesIdeal, divisao["Ações"])}
Ideal FIIs = {fiiIdeal:.2f}% | Atual: {divisao["FIIs"]:.2f}% -> {ideal(fiiIdeal, divisao["FIIs"])}""")

aporte = float(input("Digite o valor que você irá aportar: "))
novoTotal = total + aporte

valorFixa = valoresNovoAporte(novoTotal, fixaIdeal)
valorAcoes = valoresNovoAporte(novoTotal, acoesIdeal)
valorFii = valoresNovoAporte(novoTotal, fiiIdeal)


contador = 0

#Função para descobrir quantas classes de ativos precisam ser balanceadas pelo novo aporte
def divisorAporte(valorAntigo, novoIdeal):
    if valorAntigo >= novoIdeal:
        return False
    elif valorAntigo < novoIdeal:
        return True

valoresAportar = {}

if divisorAporte(rendaFixa, valorFixa) == True:
    contador += 1
    diferenca = valorFixa - rendaFixa
    valoresAportar["Renda fixa"] = diferenca
if divisorAporte(acoes, valorAcoes) == True:
    contador += 1
    diferenca = valorAcoes - acoes
    valoresAportar["Ações"] = diferenca

if divisorAporte(fii, valorFii) == True:
    contador +=1
    diferenca = valorFii - fii
    valoresAportar["FIIs"] = diferenca

#Função para ordenar os que precisam de aportes menores para estar balanceados
ordenado = dict(sorted(valoresAportar.items(), key=lambda item: item[1]))

print("Para balancear sua carteira indicamos você investir esse aporte da seguinte forma")
for chave, valor in ordenado.items():
    if valor >= aporte:
        print(f"{chave}: {aporte:.2f}R$")
        aporte = 0
    else:
        print(f"{chave}: {valor:.2f}R$")
        aporte -= valor
