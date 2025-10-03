def real_world_problem():
    print("Example: Reliability of a system with two independent components, each with failure probability 0.1.")
    p_fail = 0.1
    p_system_fail = 1 - (1-p_fail)**2
    print(f"System failure probability: {p_system_fail:.2f}")

if __name__ == "__main__":
    real_world_problem()
