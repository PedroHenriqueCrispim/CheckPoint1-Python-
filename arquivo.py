#Pedro Henrique Crispim RM:99005

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Verifica se os números estão entre 0 e 99

if numero1 < 0 or numero1 > 99 or numero2 < 0 or numero2 > 99:

    print("Números inválidos.")

else:

    # Substitui o número 7 por 0

    if numero1 % 10 == 7:
        numero1 -= 7
    if numero2 % 10 == 7:
        numero2 -= 7
    if numero1 // 10 == 7:
        numero1 -= 70
    if numero2 // 10 == 7:
        numero2 -= 70

    # Calcula a soma dos números

    soma = numero1 + numero2

    # Substitui o número 7 por 0 na soma

    if soma % 10 == 7:
        soma -= 7
    if soma // 10 == 7:
        soma -= 70

    # Exibe o resultado

    print("O resultado da soma é:", soma)
