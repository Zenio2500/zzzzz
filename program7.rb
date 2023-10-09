lista = [3,2,4,1]
lista.each {|i| puts i}

puts lista.sort() #ordena


puts lista.reduce(0) { |resultado, prox_valor| resultado+prox_valor } #soma todos os elementos

lista = lista.map { |numero| numero**2 }
puts lista