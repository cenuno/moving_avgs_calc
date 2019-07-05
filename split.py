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

result = split_list(J, p)

def get_minmax(J, p):
    '''Get minimum and maximum from list and return 
    a tuple
    '''

    results = split_list(J, p)
    min_avg = None
    max_avg = None

    means = []

    for result in results:
        means.append(sum(result)/(len(result)))
    min_avg = min(means)
    max_avg = max(means)

    return(min_avg, max_avg)


print(get_minmax(J, p))