def is_fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if n in fib_seq:
        return f"{n} pertence à sequência de Fibonacci."
    else:
        return f"{n} não pertence à sequência de Fibonacci."

# Exemplo de uso:
n = int(input("Informe um número: "))
print(is_fibonacci(n))