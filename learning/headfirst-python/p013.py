__author__ = 'pwust'

"""Kapitel 1, Seite 13"""

filme = ["Die Ritter der Kokosnuss", "Das Leben des Brian", "Der Sinn des Lebens"]

print(filme)

filme.insert(1, 1975)
filme.insert(3, 1979)
filme.append(1983)

print(filme)

filme2 = ['Die Ritter der Kokosnuss', 1975,
          'Das Leben des Brian', 1979,
          'Der Sinn des Lebens', 1983]

print(filme2)


for film in filme:
    print(film)

filme3 = [['Die Ritter der Kokosnuss', 1975],
          ['Das Leben des Brian', 1979],
          ['Der Sinn des Lebens', 1983]]

print(filme3)

for film in filme3:
    print(film)

test = ['Tes"t', "tes't", "te\"st"]
print(test)