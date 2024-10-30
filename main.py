def soma(a):
    a +=1
    return a
lista = list(i for i in range(10))
lista1 = map(soma,lista)

print(type(lista))
print(type(lista1))



numeros = [2,2,5,8] #O número 2 aparece duplicado
set_numeros = set(numeros) #Pode alterar a ordenação original.
print(set_numeros)
frutas = {"maca", "uva", "banana", "maca", "morango"}
print(frutas)

print(type(numeros))
print(type(set_numeros))

a = {2,2,5,8}
b = {2,2,3,9}
c = a.intersection(b)
d = {"a":2,"b":2,"c":5}
print(c)
print(a.symmetric_difference(b))
print(a.union(b))
print(a.intersection(b))
print(type(a))
print(type(c))
print(type(d))