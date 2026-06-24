from util.excecoes import RespostaErrada

def fase5(inventario):

    print("\n👜 FASE 5 - A BOLSA MÁGICA")

    print("\nA Barbie sempre usa algo quando vai às compras.")

    while True:

        try:

            resposta = input("\nO que é? ").strip().lower()

            if resposta == "bolsa":

                print("\n✨ Você encontrou a Bolsa Mágica!")
                inventario.append("👜 Bolsa Mágica")
                break

            raise RespostaErrada("Resposta incorreta!")

        except RespostaErrada as e:
            print(f"❌ {e}")