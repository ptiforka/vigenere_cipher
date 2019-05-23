import string

symbols = string.printable


def encrypt(key, text):
    result = []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            mj = symbols.index(ch)
            kj = symbols.index(key[(index - space) % len(key)])
            cj = (mj + kj) % len(symbols)
            result.append(symbols[cj])
        else:
            space += 1
            result.append(' ')
    return ''.join(result)


def decrypt(key, text):
    result = []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            cj = symbols.index(ch)
            kj = symbols.index(key[(index - space) % len(key)])
            mj = (cj - kj) % len(symbols)
            result.append(symbols[mj])
        else:
            space += 1
            result.append(' ')
    return ''.join(result)


first = encrypt('klic', 'SUPER 123 tajnytext')
second = encrypt('klic', 'tajny text s mezerama')
third = encrypt('dlouhyklic', 'mega zasifrovany text')

print(f"""
        {first} = {decrypt('klic', first)} 
        {second} = {decrypt('klic', second)}
        {third} = {decrypt('dlouhyklic', third)}
     """)
