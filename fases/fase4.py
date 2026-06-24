from util.excecoes import RespostaErrada


def fase4(inventario):

    print("\n═══════════════════════════════")
    print("👠 FASE 4 - SAPATO ENCANTADO")
    print("═══════════════════════════════")

    print("\nUm sapato mágico está escondido.")
    print("Onde você deseja procurar?\n")

    print("1️⃣ Bolsa")
    print("2️⃣ Sapato")
    print("3️⃣ Coroa")
    print("4️⃣ Vestido")

    while True:

        try:

            resposta = int(input("\nDigite sua escolha: "))

            if resposta == 2:

                print("\n✨ Excelente!")
                print("Você encontrou o Sapato Encantado!")

                inventario.append("👠 Sapato Encantado")

                break

            raise RespostaErrada("Você procurou no lugar errado!")

        except ValueError:

            print("\n❌ Digite apenas números.")

        except RespostaErrada as erro:

            print(f"\n❌ {erro}")
            print("Tente novamente.")