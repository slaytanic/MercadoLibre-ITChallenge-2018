adn = 'A'

n = 234612846789231
# n = 3
m = 123456789

n.times do |i|
  puts "Times #{i}, size: #{adn.size}"
  # puts adn.size
  adn.gsub!(/[ALPC]/, 'A' => 'AL', 'L' => 'PACA', 'P' => 'CP', 'C' => 'PC')
    # if m == 'A'
    #   'AL'
    # elsif m == 'L'
    #   'PACA'
    # elsif m == 'P'
    #   'CP'
    # elsif m == 'C'
    #   'PC'
    # end
  # end
end

d = adn.scan(/(?=ALPACA)/).count

puts adn
puts d
puts d % m
