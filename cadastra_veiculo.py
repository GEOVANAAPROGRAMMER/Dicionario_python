def menu():
    print("Oficina mecânica")
    print("1 - Cadastra")
    print("2 - Altera")
    print("3 - Consulta")
    print("4 - Apaga")
    print("5 - Sair")
    return int(input("Opção:  "))

lista = []
ap = menu()
while op != 5:
    if op ==1:
        veiculo = {}
        marca = input("Marca: ")
