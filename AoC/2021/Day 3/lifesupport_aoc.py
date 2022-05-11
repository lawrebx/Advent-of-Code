def diagnostic_check(diag_input, tgt_system="o"):       
    tie_breaker = '1'
    tgt_value = '0'
    
    if tgt_system == "c":
        tie_breaker = '0'
        tgt_value = '1'

    while len(diag_input) > 2:
    #column loop
        for column in range(len(diag_input[0])):  
        #row comprehension
            if len(diag_input) > 1:
                entry_char = [row[column] for row in diag_input]
                filter_value = tie_breaker
                if entry_char.count('0') > len(diag_input)/2:
                    filter_value = tgt_value
                diag_input = [i for i in diag_input if i[column] == filter_value]

    diag_result = int(diag_input[0], base=2)

    return(diag_result)