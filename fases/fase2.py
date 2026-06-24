from util.excecoes import RespostaErrada


def fase2(inventario):

    print("\n═══════════════════════════════")
    print("💄 FASE 2 - O SEGREDO DA PENTEADEIRA")
    print("═══════════════════════════════")

    while True:

        print("""
Muito bem!

Agora procure o lugar onde me vejo
todos os dias antes de sair.
""")

        print("1️⃣ Espelho")
        print("2️⃣ Bolsa")
        print("3️⃣ Sapato")
        print("4️⃣ Coroa")

        try:

            escolha = int(input("\nDigite sua escolha: "))

            if escolha != 1:
                raise RespostaErrada("Esse não é o lugar certo!")

            print("\n✨ Você encontrou o Espelho!")

            inventario.append("🪞 Espelho")

            while True:

                try:

                    vestidos = int(input("\nQuantos vestidos existem no armário? "))

                    if vestidos == 6:

                        print("\n✨ Correto!")
                        print("O primeiro número do código é 6!")

                        break

                    raise RespostaErrada("Quantidade incorreta!")

                except ValueError:

                    print("\n❌ Digite apenas números.")

                except RespostaErrada as erro:

                    print(f"\n❌ {erro}")

            break

        except ValueError:

            print("\n❌ Digite apenas números.")

        except RespostaErrada as erro:

            print(f"\n❌ {erro}")