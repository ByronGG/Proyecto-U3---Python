import statistics

def iqr(valores):
    q1 = statistics.quantiles(valores, n=4, method='inclusive')[0]
    q3 = statistics.quantiles(valores, n=4, method='inclusive')[2]
    return q3 - q1
