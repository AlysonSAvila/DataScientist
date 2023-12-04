# -*- coding: utf-8 -*-
"""Desafio DIO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11z6SXGqE2JGIU0PeQ_yz21dITk1M5JGV
"""

#Desafio de Projeto:
#Criar um sistema bancário que compute as operações de depósito, saque e extrato
#Como é um projeto inicial, o intuito é desenvolver a lógica utilizando apenas condicionais e repetidores, além de listas, strings e etc.
#Funções serão utilizadas em uma segunda versão.

#Definindo operação e variáveis iniciais
menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

  op = input(menu)

  if op == "d":
    print("Depósito")
    deposito = int(input("Digite o valor que deseja depositar:"))
    extrato = extrato + "Depósito: R$"+ str(deposito) + "\n"
    saldo = saldo + deposito

  elif op == "s":
    print("Saque")
    if numero_saques >= limite_saques:
      print("Transação negada, você ultrapassou seu limite de ", limite_saques," por dia.")
    else:
      saque = float(input("Qual valor deseja sacar?:"))
      if saldo < saque:
        print("Transação negada, você não possui saldo para este saque, seu saldo é de R$", saldo)
      elif saque > 500:
        print('Transação negada, seu limite é de R$500 por saque.')
      else:
        saldo = saldo - saque
        extrato = extrato + "Saque de R$" + str(saque) + "/n"
        numero_saques = numero_saques + 1

  elif op == "e":
    print("Extrato")
    if extrato == "":
      print("Não foram realizadas movimentações.")
    print(extrato)
    print("Seu saldo é de R$", saldo)

  elif op == "q":
    print("Sair")
    break



