J = [4, 4, 4, 9, 10, 11, 12]

p = 3

def split_list(J, p):
    '''Split a list into sequences of length p

    list of 3 moving 1 indice up each time until
    indice + p == len(J)
    '''
    output = []

    for i in range(0, len(J) - p + 1):
        output.append(J[i:i+p])
    return output

print(split_list(J, p))
