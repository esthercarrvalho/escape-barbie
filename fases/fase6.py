from util.excecoes import RespostaErrada

def fase6(inventario):

    print("\n🌈 FASE 6 - O ARMÁRIO MÁGICO")

    print("""
Enigma:

Tenho portas mas não sou casa.
Guardo roupas mas não sou mala.
O que sou?
""")

    while True:

        try:

            resposta = input("\nResposta: ").strip().lower()

            if resposta == "armário" or resposta == "armario":

                print("\n✨ O armário foi aberto!")
                inventario.append("🔑 Chave Dourada")
                break

            raise RespostaErrada("Resposta errada!")

        except RespostaErrada as e:
            print(f"❌ {e}")