'''sugg bot reactions'''

class Reactor:
    '''reaction handler'''
    file_path = ''
    reacts = {}

    def __init__(self, file_path):
        '''constructor'''
        self.file_path = file_path
        self.load_reacts()

    def react(self, string):
        '''returns a reaction or an empty string'''
        if string in self.reacts:
            return self.reacts[string]
        return ''

    def load_reacts(self):
        '''load reacts from file'''
        self.reacts.clear()
        with open(self.file_path) as reacts_file:
            for line in reacts_file:
                i = line.index('=')
                name = line[:i]
                value = line[i + 1:].replace('\n', '')
                self.reacts[name] = value

    def save_reacts(self):
        '''save reacts to file'''
        string = ''
        for i in self.reacts:
            string += i + '=' + self.reacts[i] + '\n'
        string = string[:-1]
        with open(self.file_path, 'w') as reacts_file:
            reacts_file.write(string)
