intervalo = 1..5
puts intervalo.class

puts (intervalo.include? 3)
puts (intervalo.include? 6)

intervalo.each { |i| puts i }

intervalo = intervalo.map { |i| i**2 }
puts intervalo

entrada = gets.to_i
case entrada
    when 1..4
        puts "Entre 1 e 4"
    when 5..8
        puts "Entre 5 e 8"
    else
        puts "Nenhuma opção válida"
end