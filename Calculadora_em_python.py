#!/usr/bin/env python
# coding: utf-8

# Premissas para desenvolvimento da calculadora em python:
# 1º: Quais opções de cálculo estarão inclusas?
#     R: Soma, subtração, multiplicação, divisão, resto da divisão e potenciação. Obs.: não é permitido usar as funções que já são nativas da linguagem.
# 2º: O usuário deve digitar o número correspondente a cada função para iniciar a execução
# 3º: Se o usuário digitar um valor invalido o programa deve imprimir na tela uma mensagem de valor invalido e solicitar que o usuário digite novamente o valor correspondente a função
# 4º: Após digitar o valor correspondente a função, o programa deve solicitar que o usuário informe n valores para as funções de soma, subtração e multiplicação e 2 valores para divisão, resto da divisão e potenciação
# 5º: Ao final da operação o programa deve questionar se o usuário deseja continuar, caso sim ele volta a informar a função e os valores e caso não o programa é encerrado com uma mensagem de agradecimento.

# In[13]:


print('************* Calculadora em Python *************')
funcoes = (1,2,3,4,5)
user = input('Olá qual o seu nome? ')
func = int(input(f'Bem vindo(a) {user}!\nQual função deseja utilizar?\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n'))
while func not in funcoes:
    func = int(input('O valor digitado não é valido, por favor escolha uma das opções abaixo:                     \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n'))


# In[ ]:




