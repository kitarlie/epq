def stringaction(action, *args, **kwargs):
    #Concatenates the inputs
    if action == 1:
        output = ''
        for word in kwargs:
            output += word.value()
    
    if action == 2:
        output = args.split()

    return output

print(stringaction(1, first = 'Hello', second = 'world'))