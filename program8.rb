hash = {}
puts hash

hash = {nome: "Zenio", idade: 24}
puts hash

puts hash[:nome]
puts hash[:idade]
puts hash[:rua] #retorna nil, pois a chave não existe

hash[:rua] = "Rua Cento e Sete"
puts hash

hash.each do |chave, valor|
    puts "#{chave} -> #{valor}"
end

hash { |chave,valor| "#{valor}> #{chave}" }

hash[40] = "Angelo" #chave de qualquer tipo para valor de qualquer tipo
#normalmente, usa-se symbol para um melhor desempenho
puts hash
#puts :nome