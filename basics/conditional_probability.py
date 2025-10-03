def conditional_probability(P_A_and_B, P_B):
    if P_B == 0:
        return None
    return P_A_and_B / P_B

def main():
    P_A_and_B = 0.2
    P_B = 0.5
    print(f"P(A|B) = {conditional_probability(P_A_and_B, P_B)}")

if __name__ == "__main__":
    main()
