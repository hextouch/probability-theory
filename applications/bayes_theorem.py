def bayes_theorem(P_A, P_B_given_A, P_B):
    if P_B == 0:
        return None
    return (P_B_given_A * P_A) / P_B

def main():
    P_A = 0.01
    P_B_given_A = 0.9
    P_B = 0.05
    print(f"P(A|B) = {bayes_theorem(P_A, P_B_given_A, P_B):.3f}")

if __name__ == "__main__":
    main()
