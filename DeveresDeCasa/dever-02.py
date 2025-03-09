def frase():
    """Solicita ao usuário que insira uma frase e valida a entrada."""
    while True:
        frase = input("Digite uma frase: ").strip()
        if frase:
            return frase
        else:
            print("A entrada não pode estar vazia. Tente novamente.")

def analisafrase(frase):
    """Realiza a análise da frase fornecida."""
    num_caracteres = len(frase)
    palavras = frase.split()
    num_palavras = len(palavras)
    maior_palavra = max(palavras, key=len) if palavras else ""
    
    return num_caracteres, num_palavras, maior_palavra

def manipulafrase(frase):
    """Realiza manipulações e formatações na frase."""
    frase_invertida = frase[::-1]
    palavras_invertidas = " ".join(frase.split()[::-1])
    frase_maiuscula = frase.upper()
    frase_minuscula = frase.lower()
    tupla_palavras = tuple(frase.split())
    
    return frase_invertida, palavras_invertidas, frase_maiuscula, frase_minuscula, tupla_palavras


frase_usuario = frase()
num_caracteres, num_palavras, maior_palavra = analisafrase(frase_usuario)
frase_invertida, palavras_invertidas, frase_maiuscula, frase_minuscula, tupla_palavras = manipulafrase(frase_usuario)

print("\n=== Análise da Frase ===")
print(f"Frase digitada: {frase_usuario}")
print(f"Número total de caracteres: {num_caracteres}")
print(f"Número total de palavras: {num_palavras}")
print(f"Maior palavra: {maior_palavra}")
print("\n=== Manipulação da Frase ===")
print(f"Frase invertida (caracteres): {frase_invertida}")
print(f"Frase invertida (palavras): {palavras_invertidas}")
print(f"Frase em maiúsculas: {frase_maiuscula}")
print(f"Frase em minúsculas: {frase_minuscula}")
print(f"Tupla de palavras: {tupla_palavras}")