def are_independent(P_A_and_B, P_A, P_B):
    return abs(P_A_and_B - P_A*P_B) < 1e-8

def main():
    P_A = 0.5
    P_B = 0.4
    P_A_and_B = 0.2
    print(f"A and B independent? {are_independent(P_A_and_B, P_A, P_B)}")

if __name__ == "__main__":
    main()
