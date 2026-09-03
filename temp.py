A=int(input("Insira o valor de A: "))
if A==0:
    print("A operação não será de segundo grau")
else:
    B=int(input("Insira o valor de B: "))
    C=int(input("Insira o valor de C: "))

#Nessa parte do delta eu rachei a cabeça que só, fui em fórum e td, estava fazendo no PY online inclusive então la dava uma ajudada

delt=((B**2)-4*A*C)
if delt<=0:
    print("Não há 2 raízes da seguinte equação")
else:
    X1=(-B+delt)//2*A
    X2=(-B-delt)//2*A
    print("As raízes da seguinte equação serão:", X1, "e", X2)
