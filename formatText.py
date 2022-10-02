import ast

x = ''
with open('wordleStolen.txt', 'r') as file:
    data = file.read()
    x = ast.literal_eval(data)

x = [n.strip() for n in x]

