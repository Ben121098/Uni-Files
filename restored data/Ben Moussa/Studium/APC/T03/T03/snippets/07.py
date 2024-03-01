# Formulate the obsevability matrix and print its dimension
Observability_matrix = np.concatenate((C, C@A))
print(f'O = {Observability_matrix}')

# Rank of the system matrix
Rank = matrix_rank(Observability_matrix)
print(f'Rank = {Rank}')
print('As the rank of the observerabilty matrix is equal to the number of states, then the system is observable.')