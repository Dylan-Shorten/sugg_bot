'''sugg bot program'''

import shlex

class SuggBot:
    def process_input(string):
        words = shlex.split(string)
        prefix = words[0] if len(words) > 0 else ''
        if prefix == '':
            return
        name = words[1] if len(words) > 1 else ''
        if name == '':
            return 'no command'
        if name == 'ping' and len(words) == 2:
            return 'pong'
        return ''
