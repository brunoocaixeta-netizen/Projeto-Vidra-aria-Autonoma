from datetime import datetime
import os

# ------------------------------------
#   ==== Calculadora Orçamentista ====
# ------------------------------------

preco = {
    "incolor 6mm temperado": 90.00,
    "incolor 8mm temperado": 150.00,
    "incolor 10mm temperado": 190.00,
    "fume 8mm temperado": 180.00,
    "fume 10mm temperado": 220.00,
    "verde 8mm temperado": 180.00,
    "verde 10mm temperado": 220.00,
    "espelho lapidado 4mm": 160.00,
    "espelho lapidado 5mm": 220.00,
    "espelho lapidado 6mm": 380.00,
    "espelho bisote 4mm": 190.00,
    "espelho bisote 5mm": 270.00,
    "laminado 6mm": 120.00,
    "laminado 8mm": 190.00,
    "laminado 10mm": 220.00,
    "laminado 12mm": 300.00,
    "nenhum": 0.00
}

kits = {
    "box quadrado": 180.00,
    "box redondo": 130.00,
    "elegance": 1100.00,
    "box bt3": 1200.00,
    "box flex": 1000.00,
    "kit pia": 250.00,
    "sacada": 2000.00,
    "manutencao": 700.00,
    "guarda corpo redondo": 700.00,
    "guarda corpo quadrado": 900.00,
    "guarda corpo reforcado": 2000.00,
    "nenhum": 0.00
}

acessorios = {
    "puxador h 30": 65.00,
    "puxador h 40": 85.00,
    "fita led": 500.00,
    "moldura espelho": 300.00,
    "nenhum": 0.00
}

servicos = {
    "chassi tubo reti": 500.00,
    "chassi tubo 2x1": 450.00,
    "jato de areia espelho": 600.00,
    "jato de areia janela": 350.00,
    "jato de areia porta": 420.00,
    "nenhum": 0.00
}

obra = {
    "mao de obra padrao": 950.00,
    "mao de obra alto padrao": 2500.00,
    "espelho 4mm": 700.00,
    "espelho 5mm": 1750.00,
    "nenhum": 0.00
}


# ---------------- FUNÇÕES ---------------- #

def mostrar_opcoes(dicionario, titulo):

    print(f"\n========== {titulo.upper()} ==========")

    for i, (item, valor) in enumerate(dicionario.items(), start=1):

        print(f"{i} - {item} --> R$ {valor:.2f}")


def gerar_numero_orcamento():

    try:

        arquivos = os.listdir("orcamentos")

        quantidade = len(arquivos)

        return quantidade + 1

    except FileNotFoundError:

        return 1


def salvar_orcamento(resultado, numero_orcamento):

    if not os.path.exists("orcamentos"):

        os.makedirs("orcamentos")

    nome_arquivo = (
        f"orcamentos/orcamento_{numero_orcamento:04d}.txt"
    )

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:

        arquivo.write(resultado)


def ver_orcamentos():

    try:

        arquivos = sorted(os.listdir("orcamentos"))

        if len(arquivos) == 0:

            print("\nNenhum orçamento salvo.")

            return

        print("\n========== ORÇAMENTOS SALVOS ==========\n")

        for nome_arquivo in arquivos:

            caminho_arquivo = f"orcamentos/{nome_arquivo}"

            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:

                conteudo = arquivo.read()

                print(conteudo)

                print("=" * 60)

    except FileNotFoundError:

        print("\nNenhum orçamento salvo ainda.")


def buscar_cliente():

    try:

        nome_busca = input(
            "\nDigite o nome do cliente: "
        ).lower()

        arquivos = sorted(os.listdir("orcamentos"))

        encontrado = False

        for nome_arquivo in arquivos:

            caminho_arquivo = (
                f"orcamentos/{nome_arquivo}"
            )

            with open(
                caminho_arquivo,
                "r",
                encoding="utf-8"
            ) as arquivo:

                conteudo = arquivo.read()

                if nome_busca in conteudo.lower():

                    print("\n" + "=" * 60)

                    print(conteudo)

                    encontrado = True

        if not encontrado:

            print("\nCliente não encontrado.")

    except FileNotFoundError:

        print("\nNenhum orçamento salvo.")


def buscar_numero_orcamento():

    try:

        numero = int(input("\nDigite o número do orçamento: "))

        nome_arquivo = (
            f"orcamentos/orcamento_{numero:04d}.txt"
        )

        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

            conteudo = arquivo.read()

            print("\n" + "=" * 60)

            print(conteudo)

    except FileNotFoundError:

        print("\nOrçamento não encontrado.")

    except ValueError:

        print("\nDigite apenas números.")


def calcular():

    try:

        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

        numero_orcamento = gerar_numero_orcamento()

        print("\n" + "=" * 40)
        print("ATENDIMENTO AUTOMÁTICO VIDRAÇARIA")
        print("=" * 40)

        nome_cliente = input("\nNome do cliente: ")
        telefone_cliente = input("Telefone do cliente: ")

        print("\nTipos de vidro:")
        print("1 - Vidro comum")
        print("2 - Vidro temperado")
        print("3 - Espelho")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            tipo_vidro = "Vidro comum"
            valor_m2 = 120

        elif opcao == "2":

            tipo_vidro = "Vidro temperado"
            valor_m2 = 250

        elif opcao == "3":

            tipo_vidro = "Espelho"
            valor_m2 = 180

        else:

            print("Opção inválida!")
            return

        largura = float(input("Largura (m): "))
        altura = float(input("Altura (m): "))

        metragem = largura * altura

        total = metragem * valor_m2

        # ===== KITS =====

        mostrar_opcoes(kits, "Tabela de Kits")

        nome_kit = input(
            "\nDigite o nome do kit: "
        ).lower()

        valor_kit = kits.get(nome_kit, 0)

        total += valor_kit

        # ===== ACESSÓRIOS =====

        mostrar_opcoes(
            acessorios,
            "Tabela de Acessórios"
        )

        nome_acessorio = input(
            "\nDigite o nome do acessório: "
        ).lower()

        valor_acessorio = acessorios.get(
            nome_acessorio,
            0
        )

        total += valor_acessorio

        resultado = f"""
================ ORÇAMENTO ================

ORÇAMENTO Nº {numero_orcamento:04d}

Data:
{data_atual}

------------------------------------------

Cliente:
{nome_cliente}

Telefone:
{telefone_cliente}

------------------------------------------

Serviço realizado:
{tipo_vidro}

------------------------------------------

Metragem:
{metragem:.2f} m²

Valor do m²:
R$ {valor_m2:.2f}

------------------------------------------

Kit:
{nome_kit} - R$ {valor_kit:.2f}

------------------------------------------

Acessório:
{nome_acessorio} - R$ {valor_acessorio:.2f}

------------------------------------------

TOTAL FINAL:
R$ {total:.2f}

==========================================
"""

        print(resultado)

        salvar = input(
            "\nDeseja salvar orçamento? (s/n): "
        ).strip().lower()

        if salvar == "s":

            salvar_orcamento(
                resultado,
                numero_orcamento
            )

            print("\nOrçamento salvo com sucesso!")

    except ValueError:

        print("\nErro: digite apenas números válidos.")


# ---------------- MENU ---------------- #

while True:

    print("""
============================= Art&Design ===============================
====================== Vidraçaria Inteligente ==========================

1 - Novo orçamento
2 - Ver tabela de vidros
3 - Ver tabela de kits
4 - Ver tabela de acessórios
5 - Ver tabela de serviços
6 - Ver tabela de mão de obra
7 - Ver orçamentos salvos
8 - Buscar orçamento por cliente
9 - Buscar orçamento por número
10 - Sair

========================================================================
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        calcular()

    elif opcao == "2":

        mostrar_opcoes(preco, "Tabela de Vidros")

    elif opcao == "3":

        mostrar_opcoes(kits, "Tabela de Kits")

    elif opcao == "4":

        mostrar_opcoes(acessorios, "Tabela de Acessórios")

    elif opcao == "5":

        mostrar_opcoes(servicos, "Tabela de Serviços")

    elif opcao == "6":

        mostrar_opcoes(obra, "Tabela de Mão de Obra")

    elif opcao == "7":

        ver_orcamentos()

    elif opcao == "8":

        buscar_cliente()

    elif opcao == "9":

        buscar_numero_orcamento()

    elif opcao == "10":

        print("\nSistema encerrado.")
        break

    else:

        print("\nOpção inválida.")