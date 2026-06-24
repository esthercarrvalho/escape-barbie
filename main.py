from fases.fase1 import fase1
from fases.fase2 import fase2
from fases.fase3 import fase3
from fases.fase4 import fase4
from fases.fase5 import fase5
from fases.fase6 import fase6

# Lista que guarda os itens encontrados
inventario = []

# =========================
# TELA INICIAL
# =========================
print("=" * 50)
print("🎀 ESCAPE DO ARMÁRIO DA BARBIE 🎀")
print("=" * 50)

print("\nBem-vindo(a)!")
print("Hoje é o grande dia do Desfile dos Sonhos da Barbie.")
print("Uma fada atrapalhada lançou um feitiço")
print("e trancou o armário mágico.")
print("Sua missão é encontrar a chave antes")
print("que o desfile comece!")

input("\nPressione ENTER para continuar...")

# =========================
# NOME DO JOGADOR
# =========================
nome = input("\nDigite seu nome: ")

print(f"\nBoa sorte, {nome}! 💖")
print("A Barbie está contando com você!")

# =========================
# MENU
# =========================
while True:

    print("\n" + "=" * 50)
    print("🎀 MENU 🎀")
    print("=" * 50)
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        print("\n🌸 A aventura vai começar!")
        input("Pressione ENTER para iniciar...")

        # Executa todas as fases
        fase1(inventario)
        fase2(inventario)
        fase3(inventario)
        fase4(inventario)
        fase5(inventario)
        fase6(inventario)

        print("\n" + "=" * 50)
        print("🎉 PARABÉNS! 🎉")
        print("=" * 50)
        print(f"\n{nome}, você conseguiu salvar a Barbie!")
        print("Ela chegou a tempo para o Desfile dos Sonhos! 👑")

        print("\n🎒 INVENTÁRIO:")

        if len(inventario) == 0:
            print("Nenhum item encontrado.")
        else:
            for item in inventario:
                print(f"• {item}")

        print("\nObrigada por jogar! 💖")
        break

    elif opcao == "2":

        print("\n" + "=" * 50)
        print("📜 REGRAS")
        print("=" * 50)

        print("• Resolva todos os enigmas.")
        print("• Cada resposta correta libera uma nova fase.")
        print("• Encontre a chave escondida.")
        print("• Salve a Barbie antes do desfile começar!")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "3":

        print("\nAté a próxima! 💖")
        break

    else:

        print("\n❌ Opção inválida! Tente novamente.")