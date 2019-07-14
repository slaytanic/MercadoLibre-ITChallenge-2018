require 'byebug'

File.open('secreto.pdf', 'rb') do |f|
  content = f.read
  (0..255).each do |t|
    File.open("secretos/#{t}.pdf", 'wb') do |of|
      content.each_byte do |b|
        # begin
          of << (b ^ t).chr
        # rescue
        # end
        #byebug
        #of.write((b + t).chr)
      end
    end
  end
end