def word_break(s, word_dict)
    
    bools = Array.new(s.length+1, false)
    bools[0] = true
    
    (0...bools.length).each do |i|
        next if bools[i] == false
        
        (i...bools.length).each do |j|
            test_word = s[i...j]
            if word_dict.include?(test_word)
                bools[j] = true
            end
        end
    end
    
    return bools[-1]
    
end