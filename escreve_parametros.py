nome_arquivo = input("Digite o nome do arquivo para escrever: ")
parametros = input("Digite os parâmetros separados por espaço: ").split()

with open(nome_arquivo, "w", encoding="utf-8") as f:
    for parametro in parametros:
        f.write(parametro + "\n")

print(f"Parâmetros escritos no arquivo {nome_arquivo} com sucesso!")
