def count_a(string):
    count = string.lower().count('a')
    return f"A letra 'a' ocorre {count} vezes na string."

# Exemplo de uso:
string = input("Informe uma string: ")
print(count_a(string))