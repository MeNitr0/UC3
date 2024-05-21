'''
construa um programa que fará o cálculo do salário líquido
de um professor. para fazer esse cálculo, é necessário que
sejam lidos o valor da hora aula, o número de horas dadas 
no mês e o valor total de descontos. 
'''
valorHora = float(input("informe o valor recebido por hora: "))
numeroHoras = float(input("informe o número de horas: "))
descontos = float(input("informe os descontos: "))

salarioLiquido = (valorHora * numeroHoras) - descontos

print(f"o valor do seu salário líquido é: {salarioLiquido}")