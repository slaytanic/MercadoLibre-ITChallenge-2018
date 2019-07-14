require 'pp'
require 'pry'

class Node
  attr_reader :char
  attr_accessor :prevnode
  attr_accessor :nextnode

  def initialize(char, prevnode = nil, nextnode = nil)
    @char = char
    @prevnode = prevnode
    @nextnode = nextnode
  end

  def replace
    if @char == 'A'
      old_nextnode = @nextnode
      @nextnode = Node.new('L', self, old_nextnode)
      old_nextnode.prevnode = @nextnode if old_nextnode
      return old_nextnode
    elsif @char == 'L'
      # puts "prev:"
      # pp @prevnode
      # puts "next:"
      # pp @nextnode
      old_prevnode = @prevnode
      old_nextnode = @nextnode
      @prevnode = nil
      @nextnode = nil
      p1 = Node.new('P', old_prevnode)
      old_prevnode.nextnode = p1
      a1 = Node.new('A', p1)
      p1.nextnode = a1
      c1 = Node.new('C', a1)
      a1.nextnode = c1
      a2 = Node.new('A', c1, old_nextnode)
      c1.nextnode = a2
      old_nextnode.prevnode = a2 if old_nextnode
      return old_nextnode
    elsif @char == 'P'
      old_prevnode = @prevnode
      @prevnode = Node.new('C', old_prevnode, self)
      old_prevnode.nextnode = @prevnode
      return @nextnode
    elsif @char == 'C'
      old_prevnode = @prevnode
      @prevnode = Node.new('P', old_prevnode, self)
      old_prevnode.nextnode = @prevnode
      return @nextnode
    end
  end
end

head = Node.new('A')

# binding.pry

# tail = head

# n = 234612846789231
n = 2
m = 123456789

n.times do |i|
  adn = ''
  curr = head
  prevnode = nil
  puts "Times #{i}" #", size: #{adn.size}"
  while curr
    adn << curr.char

    # pp head
    curr = curr.replace
  end
  # puts adn
  puts adn.size
  d = adn.scan(/(?=ALPACA)/).count
  puts d
  puts (d % m)

  # GC.start
  # puts adn.size
  #adn.gsub!(/[ALPC]/, 'A' => 'AL', 'L' => 'PACA', 'P' => 'CP', 'C' => 'PC')
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

adn = ''

# pp head

curr = head
while curr
  adn << curr.char
  curr = curr.nextnode
end

# d = adn.scan(/(?=ALPACA)/).count

# puts adn
# puts d
# puts d % m
