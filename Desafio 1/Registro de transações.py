def calcular_saldo(transacoes):
    saldo = 0

    # TODO: Itere sobre cada transação na lista:
    for transacao in transacoes:
        # TODO: Adicione o valor da transação ao saldo
        saldo += transacao
        
    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    return (f"R$ {saldo:.2f}")

entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print("Saldo: ",(resultado))