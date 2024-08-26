def separate_commands(command_input):
    command = []
    word = ""
    i = 0
    in_quotes = False

    while i < len(command_input):
        if command_input[i] == '"':
            if in_quotes:
                in_quotes = False
                command.append(word)  # Add the word without the quotes
                word = ""
            else:
                in_quotes = True
        elif command_input[i] == " " and not in_quotes:
            if word:
                command.append(word)
                word = ""
        else:
            word += command_input[i]
        i += 1

    # Append the last word after the loop
    if word:
        command.append(word)
    
    return command
