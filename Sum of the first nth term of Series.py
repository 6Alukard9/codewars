def series_sum(n):
    answer = 1
    if n == 0:
        return '0.00'
    fraction = 4
    for i in range(n -1):
        answer += 1/fraction
        fraction += 3
    return f"{answer:.2f}"


"""
Task:
Your task is to write a function which returns the sum of following series
upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

Examples:(Input --> Output)
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
"""