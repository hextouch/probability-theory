import math

def combinations(n, k):
    return math.comb(n, k)

def permutations(n, k):
    return math.perm(n, k)

def main():
    print(f"C(5,2) = {combinations(5,2)}")
    print(f"P(5,2) = {permutations(5,2)}")

if __name__ == "__main__":
    main()
