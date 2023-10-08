def calcul(A, B, months):
    total_expenses = 0
    for month in range(months):
        total_expenses += B
        B *= 1.05
        total_expenses -= A

    required_amount = abs(total_expenses)
    return required_amount