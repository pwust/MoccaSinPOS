__author__ = 'pwust'

g = open("output.txt", "wb")

with open("input.txt", "rb") as f:
    for line in f:
        g.write(line[::-1])

f.close()
g.close()
