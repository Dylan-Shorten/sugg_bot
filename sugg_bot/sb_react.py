'''sugg bot reacts'''

def load_reacts():
    '''load reacts from file'''
    reacts.clear()
    with open('../data/reacts.txt') as reacts_file:
        for line in reacts_file:
            split = line.replace('\n', '').split('=')
            reacts[split[0]] = split[1]

def save_reacts():
    '''save reacts to file'''
    string = ''
    for i in reacts:
        string += i + '=' + reacts[i] + '\n'
    string = string[:-1]
    with open('../data/reacts.txt', 'w') as reacts_file:
        reacts_file.write(string)

async def parse_react(string, channel):
    '''respond if the string is a react'''
    if string in reacts:
        await channel.send(reacts[string])
        return True
    return False

reacts = {}
