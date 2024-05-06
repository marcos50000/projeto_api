# Solicitar informações ao usuário
d = float(input("Insira a distância em quilômetros: "))
v = float(input("Insira a velocidade em quilômetros por hora: "))
m = input("Digite o nome do motorista: ")
# Calcular o tempo
t = d / v

# Exibir o resultado
print(f"O tempo necessário para fazer o percurso é de {t:.2f} horas. com o motorista {m}")