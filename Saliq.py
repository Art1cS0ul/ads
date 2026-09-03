Horas=float(input("Digite a quantidade de horas trabalhadas: "))
Valor=float(input("Digite o valor por hora: "))
Desconto=float(input("Digite o percentual de desconto: "))
Dependentes=int(input("Digite a quantidade de dependentes: "))

Bruto=Horas*Valor
Desc=Bruto*(Desconto/100)
Liquido=Bruto-Desc
Adicional=Dependentes*100
Total=Liquido+Adicional

print("O salário bruto é:", Bruto)
print("O salário a receber é:", Total)
