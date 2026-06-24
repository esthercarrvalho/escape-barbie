from util.excecoes import RespostaErrada


def fase3(inventario):

    print("\n═══════════════════════════════")
    print("👗 FASE 3 - CÓDIGO DOS VESTIDOS")
    print("═══════════════════════════════")

    print("\nA Barbie encontrou três vestidos mágicos.")
    print("Cada vestido possui um número:\n")

    print("💗 Vestido Rosa = 6")
    print("💙 Vestido Azul = 3")
    print("💜 Vestido Lilás = 4")

    print("\nDescubra o código correto para abrir a gaveta secreta!")

    while True:

        try:

            resposta = input("\nDigite o código: ")

            if resposta == "634":

                print("\n✨ Parabéns!")
                print("Você descobriu o código secreto!")

                inventario.append("👗 Código dos Vestidos")

                break

            raise RespostaErrada("Código incorreto!")

        except RespostaErrada as erro:

            print(f"\n❌ {erro}")
            print("Tente novamente.")