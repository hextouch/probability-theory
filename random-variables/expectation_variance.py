def expectation_variance():
    # Example: fair die
    values = [1,2,3,4,5,6]
    probs = [1/6]*6
    E = sum(v*p for v,p in zip(values,probs))
    Var = sum(((v-E)**2)*p for v,p in zip(values,probs))
    print(f"E[X]={E}, Var[X]={Var}")

if __name__ == "__main__":
    expectation_variance()
