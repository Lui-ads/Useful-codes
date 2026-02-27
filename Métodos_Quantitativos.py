from scipy import stats
from math import erf, sqrt

# Bubble Sort
def ordenar(lista): # Working        
    n=len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Bubble Sort para lista de pares (do maior para o menor)
def ordenar_maior_menor(lista, indice):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][indice] < lista[j + 1][indice]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Media 
def media(): # Working
    entrada = input("Sua lista: ")
    lista = list(map(int, entrada.split()))
    divisor = len(lista)
    media = sum(lista)/divisor
    return media

# Mediana
def mediana(): # Working
    entrada = input("Sua lista: ")
    lista = list(map(int, entrada.split()))
    lista_orde = ordenar(lista)
    i_or_p = len(lista_orde)
    if i_or_p % 2 != 0:
        valor_da_posicao = i_or_p // 2
        mediana = (lista_orde[valor_da_posicao])
        return mediana
    elif i_or_p % 2 == 0:
        valor_da_posicao_1 = i_or_p // 2 - 1
        valor_da_posicao_2 = i_or_p // 2
        mediana = (lista_orde[valor_da_posicao_1] + lista_orde[valor_da_posicao_2]) / 2
        return mediana


# Moda
def moda(): # Working
    entrada = input("Digite os números: ")
    lista = list(map(int, entrada.split()))
    
    contagem = {}
    for m in range(len(lista)):
        numero = lista[m]
        if numero in contagem:
            contagem[numero] = contagem[numero] + 1
        else:
            contagem[numero] = 1
            maior_contagem = 0
    moda_valor = None
    
    for numero in contagem:
        if contagem[numero] > maior_contagem:
            maior_contagem = contagem[numero]
            moda_valor = numero
    
    return moda_valor

# SPEARMAN
def spearman(): # Working
    entrada1 = input("Digite os valores da primeira lista (interações): ")
    lista_1 = list(map(int, entrada1.split()))
    
    entrada2 = input("Digite os valores da segunda lista (notas): ")
    lista_2 = list(map(int, entrada2.split()))
    
    if len(lista_1) != len(lista_2):
        print("Erro: as listas precisam ter o mesmo tamanho!")
        return None
    
    pares = []
    for n in range(len(lista_1)):
        pares.append([lista_1[n], lista_2[n]])
    
    pares_orde = ordenar_maior_menor(pares, 0)
    
    inter_ordenado = ordenar(lista_1)
    nota_ordenado = ordenar(lista_2)
    
    rank_inter = []
    for valor in lista_1:
        rank_inter.append(inter_ordenado.index(valor) + 1)
    
    rank_nota = []
    for valor in lista_2:
        rank_nota.append(nota_ordenado.index(valor) + 1)
    
    diferenca = []
    for o in range(len(rank_inter)):
        diferenca.append(rank_inter[o] - rank_nota[o])
    
    diferenca_ao_quadrado = []
    for p in range(len(diferenca)):
        diferenca_ao_quadrado.append(diferenca[p] ** 2)
    
    soma = sum(diferenca_ao_quadrado)
    quant = len(pares_orde)
    spearman = 1 - (6 * soma) / (quant * (quant ** 2 - 1))
    
    return spearman

# WILCOXON
def wilcoxon(): # Working
    entrada1 = input("Digite os números do grupo: ")
    grupo_1 = list(map(int, entrada1.split()))
    
    entrada2 = input("Digite os números do grupo: ")
    grupo_2 = list(map(int, entrada2.split()))
    
    grupo_A_e_B = grupo_1 + grupo_2
    grupos_ordenados = ordenar(grupo_A_e_B)
    
    rankin = {}
    for q in range(len(grupos_ordenados)):
        valor = grupos_ordenados[q]
        rankin[valor] = q + 1    

    soma_1 = 0
    for valor in grupo_1:
        soma_1 = soma_1 + rankin[valor]
    
    soma_2 = 0
    for valor in grupo_2:
        soma_2 = soma_2 + rankin[valor]
    
    wilcoxon = min(soma_1, soma_2)
    return wilcoxon

# KRUSKAL-WALLIS
def kruskal_wallis(): # Working
    grupos = []
    loop = int(input('São quantos grupos: '))
    for s in range(loop):
        grupo = list(map(int, input(f'{s+1}º Grupo: ').split()))
        grupos.append(grupo)
    
    todos_os_valores = []
    for grupo in grupos:
        for valor in grupo:
            todos_os_valores.append(valor)
    
    grupos_arrumados = ordenar(todos_os_valores)   
    
    rankin = {}
    for t in range(len(grupos_arrumados)):
        valor = grupos_arrumados[t]
        rankin[valor] = t + 1

    somas = []
    for grupo in grupos:
        soma = 0
        for valor in grupo:  
            soma = soma + rankin[valor]
        somas.append(soma)
    
    esperando = []
    for v in range(len(somas)):
        n=len(grupos[v])
        acao = ((somas[v]**2)/n)                
        esperando.append(acao)
    
    pronto = sum(esperando)
    n_grande = len(todos_os_valores)
    # H = (12 / (N × (N + 1))) × (soma_dos_termos) - 3 × (N + 1)
    h = (12 / (n_grande * (n_grande + 1))) * pronto - 3 * (n_grande + 1)
    
    return h
    
# SHAPIRO-WILK
def shapiro_wilk(): # Working
    
    entrada = input("Sua lista: ")
    lista = list(map(int, entrada.split()))
    
    estatistica_w, valor_p = stats.shapiro(lista)
    reposta = (f"W = {estatistica_w} e p-value = {valor_p}")
    return reposta
   
   
# KOLMOGOROV-SMIRNOV
def kolmogorov_smirnov(): # Working
    
    entrada = input("Sua lista: ")
    lista = list(map(int, entrada.split()))
    
    lista_ordenada = ordenar(lista)
    n = len(lista_ordenada)
    media = sum(lista_ordenada) / n
    
    soma_quadrados = 0
    for valor in lista_ordenada:
        soma_quadrados += (valor - media) ** 2
    desvio = (soma_quadrados / (n - 1)) ** 0.5
    
    diferencas = []
    for i in range(n):
        freq_obs = (i + 1) / n
    
        z = (lista_ordenada[i] - media) / desvio
    
        freq_teorica = 0.5 * (1 + erf(z / sqrt(2)))
        
        diferencas.append(abs(freq_obs - freq_teorica))
        
    d = max(diferencas)
        
    return d

print("1 - Média\n2 - Mediana\n3 - Moda\n4 - Spearman\n5 - Wilcoxon\n6 - Kruskal-Wallis\n7 - Shapiro-Wilk\n8 - Kolmogorov-Smirnov\n0 - Sair")
opcao = input("O que você quer usar? Digite o número: ")

if opcao == "1":
    print("\nMÉDIA")
    print("Resultado:", media())
elif opcao == "2":
    print("\nMEDIANA")
    print("Resultado:", mediana())
elif opcao == "3":
    print("\nMODA")
    print("Resultado:", moda())
elif opcao == "4":
    print("\nSPEARMAN")
    print("Resultado:", spearman())
elif opcao == "5":
    print("\nWILCOXON")
    print("Resultado:", wilcoxon())
elif opcao == "6":
    print("\nKRUSKAL-WALLIS")
    print("Resultado H:", kruskal_wallis())
elif opcao == "7":
    print("\nSHAPIRO-WILK")
    print("Resultado:", shapiro_wilk())
elif opcao == "8":
    print("\nKOLMOGOROV-SMIRNOV")
    print("Resultado D:", kolmogorov_smirnov())
elif opcao == "0":
    print("Código finalizado")
else:
    print("Opção inválida!")


