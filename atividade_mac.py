import random

def main():
    # Inicialização
    semente = int(input("Digite a semente do sorteio: "))
    random.seed(semente)

    populacao = 15
    energia = 150.0
    comida = 150.0
    escudo = False

    # Loop pelos dias
    dia = 1
    while dia <= 5:
        # Cabeçalho do dia
        print("----")
        print(f"Dia {dia} | Populacao: {populacao} | Escudo: {escudo}")
        print(f"Energia: {energia:.2f} | Comida: {comida:.2f}")

        # Leitura da ação
        acao = int(input("Digite o numero da acao do dia: "))

        # Executa a ação escolhida
        if acao == 1:      # Gerar Energia
            base = random.randint(30, 40)
            gerado = base * (1 - 0.05 * dia)
            energia += gerado
            print(f"Base: {base}")
            print(f"Geracao de energia: +{gerado:.2f}")

        elif acao == 2:    # Produzir Comida
            base = random.randint(30, 40)
            temperatura = random.randint(-20, 40)
            # Fator de temperatura
            fator = 1 - abs(temperatura - 22) / 100
            colhido = base * fator
            print(f"Base: {base} | Temperatura: {temperatura}")
            if temperatura < -10 or temperatura > 35:
                print("ALERTA: Choque termico! (- metade da colheita)")
                colhido /= 2
            print(f"Producao de comida: +{colhido:.2f}")
            comida += colhido

        elif acao == 3:    # Ativar Escudo
            if energia >= 20:
                energia -= 20
                escudo = True
                print("Escudo ativado (-20 de Energia)")
            else:
                print("Energia insuficiente para ativar o escudo.")

        else:
            # Ação inválida (não deve ocorrer conforme enunciado)
            print("Acao invalida. Tente novamente.")
            continue  # repete o mesmo dia

        # Consumo diário (2.1 * população)
        consumo = 2.1 * populacao
        energia -= consumo
        comida -= consumo
        print(f"Consumo de Energia e Comida: -{consumo:.2f}")

        # Eventos ocasionais (nascimento primeiro, depois meteoros)
        if random.randint(1, 100) <= 10:
            populacao += 1
            print("ALERTA: Nascimento! (+1 de Populacao)")

        if random.randint(1, 100) <= 30:
            if escudo:
                print("ALERTA: Meteoros! (Escudo foi descarregado)")
                escudo = False
            else:
                print("ALERTA: Meteoros! (-30 de Energia e de Comida)")
                energia -= 30
                comida -= 30

        # Alerta de recursos críticos
        if energia < 30 or comida < 30:
            print("ALERTA: Recursos em nivel critico!")

        # Verifica se algum recurso se esgotou
        if energia <= 0 or comida <= 0:
            break

        # Próximo dia
        dia += 1

    # Relatório final
    print("\n--- \n")
    print("RELATORIO FINAL")
    print(f"Dia {dia} | Populacao: {populacao} | Escudo: {escudo}")
    print(f"Energia: {energia:.2f} | Comida: {comida:.2f}")

    if energia <= 0 or comida <= 0:
        if comida <= 0:
            print("FALHA: Comida esgotada")
        else:
            print("FALHA: Energia esgotada")
    else:
        print("SUCESSO: Colonos salvos")

if __name__ == "__main__":
    main()
