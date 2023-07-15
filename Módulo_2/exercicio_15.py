#Crie uma função chamada "calcular_retorno_percentual" 
# que recebe um valor inicial e um valor final e retorna 
# o retorno percentual do investimento. Teste a função 
# com um programa onde o usuário informa os valores iniciais e finais.
#retorno percentual = ((valor final - valor inicial)/valor inicial)* 100


def calc_retono_percentual(valor_inicial, valor_final):
    retorno_percentual = ((valor_final - valor_inicial)/valor_inicial)* 100
    return retorno_percentual

valor_inicial = float(input("Digite o valor inicial: \n"))
valor_final = float(input("Digite o valor final: \n"))


valor_print = calc_retono_percentual(valor_inicial, valor_final)
print(f"O valor percentual é {valor_print}%")




