def title_to_number(s)
    
    alpha = ("A".."Z").to_a
    
    column = 0
    
    letter = s.length-1
    i = 0
    
    while letter >= 0
        
        index = alpha.index(s[letter]) + 1
        column += index * 26**i
        
        letter -= 1
        i += 1
    end
    
    return column
    
end