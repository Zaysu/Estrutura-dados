from vetores import vetor

print(30 * "-", "MENU", 30 * "-")
print("1. Vetores")
print("2. Lista")

menu = int(input("Digite a Opção desejada"))

if menu == 1:
    vetor_test = vetor.Vetor(3)
    ##vetor_test.inserir_elemento_posicao(1, 0)
    #vetor_test.inserir_elemento_posicao(3, 1)
    vetor_test.inserir_elememento_final(1)
    vetor_test.inserir_elememento_final(2)
    vetor_test.inserir_elememento_final(3)
    vetor_test.inserir_elememento_final(4)
    print(vetor_test.listar_elemtento(0))
    print(vetor_test.listar_elemtento(1))
    print(vetor_test.listar_elemtento(2))
    print(vetor_test.listar_elemtento(3))