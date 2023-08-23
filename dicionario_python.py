tabela = {}
                    
                    #pts, vitorias, gols pro, gols contra
tabela['botafogo'] = [16,6,34,10]
tabela['corinthias'] = [25, 8, 79, 1]
tabela['palmeiras'] = [12, 4, 1, 10]
tabela['santos'] = [5, 1, 4, 9]

print(tabela)

                #Aterando os valores da chave palmeiras dentro do dicionário
tabela['palmeiras'] = [12, 4, 10, 4]
print("******************************************************************************************")
print(tabela)

                #Aterando apenas alguns valores da chave palmeiras dentro do dicionário
reg = tabela['palmeiras']
reg[2] = 16
reg[3] = 8

print(tabela)