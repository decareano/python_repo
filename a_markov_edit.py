import random

def fetch_url(url):
    fin = req.urlopen(url)
    return fin.read()

def write_text(txt, filename, enc='utf8'):
    with open(filename, 'w', encoding=enc) as fout:
        fout.write(txt)

def get_markov(filename, enc='utf8'):
    with open(filename, encoding=enc) as fin:
        txt = fin.read()
    return Markov(txt)


class Markov:
    def __init__(self, data):
        self.table = get_table(data)

    def predict(self, data_in):
        options = self.table.get(data_in, {}) ## a is in predict, if not empty{}
        if not options:
            raise KeyError(f'{data_in} not found')
        possibles = []
        for char, count in options.items():
            for i in range(count):
                possibles.append(char)
        return random.choice(possibles)
    
def get_table(data):
    results = {}
    for i in range(len(data)):
        char = data[i]
        try:    
            next_char = data[i+1] # out char data plus one or b?
        except IndexError:
            break
        if char in results:
            char_dict = results[char] #char_dict is the {b : 1} dict
        else:
            char_dict = {}
        if next_char in char_dict:
            char_dict[next_char] += 1
        else:
            char_dict[next_char] = 1
        results[char] = char_dict
    return results


