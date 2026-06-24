from util.excecoes import RespostaErrada


def fase1(inventario):

    print("\n═══════════════════════════════")
    print("🎀 FASE 1 - O CONVITE MISTERIOSO")
    print("═══════════════════════════════")

    print("""
Olá! Sou a Barbie e preciso da sua ajuda!

Minha chave desapareceu!

Sua primeira missão é descobrir qual acessório
uso para arrumar meu cabelo.
""")

    while True:

        print("\n🌸 Onde você deseja procurar?")
        print("1️⃣ Sapato")
        print("2️⃣ Pente")
        print("3️⃣ Bolsa")
        print("4️⃣ Vestido")

        try:

            escolha = int(input("\nDigite sua escolha: "))

            if escolha == 2:

                print("\n✨ Excelente!")
                print("Você encontrou o Pente Mágico!")

                inventario.append("🪮 Pente")

                break

            raise RespostaErrada("A Barbie ainda continua presa!")

        except ValueError:

            print("\n❌ Digite apenas números.")

        except RespostaErrada as erro:

            print(f"\n❌ {erro}")
            print("Tente novamente.")