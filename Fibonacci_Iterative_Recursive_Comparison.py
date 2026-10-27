
# ITERATIVE FIBONACCI — O(n)

def fib_iterative(n, trace=False):
    if n <= 1:
        return n

    a, b = 0, 1

    for i in range(2, n + 1):
        if trace:
            print(f"Step {i-1}: fib({i}) = {a} + {b} = {a+b}")

        a, b = b, a + b

    return b


# RECURSIVE FIBONACCI — O(2^n)

def fib_recursive(n, counter, depth=0, trace=False):
    counter[0] += 1

    if trace:
        print("  " * depth + f"fib({n})")

    if n <= 1:
        return n

    return (fib_recursive(n-1, counter, depth+1, trace)
            + fib_recursive(n-2, counter, depth+1, trace))


# PART 1: TRACE BOTH ALGORITHMS

n = 6

print("=== ITERATIVE FIBONACCI ===")
print("Result:", fib_iterative(n, trace=True))

print("\n=== RECURSIVE FIBONACCI ===")
counter = [0]
print("Result:", fib_recursive(n, counter, trace=True))
print("Total function calls:", counter[0])


# PART 2: COMPARE THE GROWTH

print("\n=== COMPLEXITY COMPARISON ===")
print(f"{'n':>5} | {'Iterations':>12} | {'Recursive calls':>16}")
print("-" * 40)

for n in [6, 10, 20, 30]:
    iterations = n - 1

    counter = [0]
    fib_recursive(n, counter)

    print(f"{n:>5} | {iterations:>12} | {counter[0]:>16,}")
    
