lista = [] #declaração
puts lista

lista = Array.new #declaração
puts lista

lista = [1,2,3,4] #lista de inteiros
puts lista

lista = lista = ["nome", :nome, 1, 2.5] #lista de vários tipos
puts lista

lista = %w(conversao de strings para array) #uma forma de declarar lista de strings
puts lista[0]
puts lista[-1] #lista[len(lista)-1]
puts lista[1]
puts lista[2]
puts lista[3]
puts lista[4]

lista[0] = "Zenio" #substituição de "conversão" por "Zenio"
puts lista[0]
puts lista

lista.push(36) #insere no final
puts lista

puts lista.join() #concatena todos os elementos(saída é uma string)
puts lista.join(",") #concatena com um separador(saída é uma string)