
"""
m = Markov('ab')
m.predict('a')
'b'

get_table('ab')
{'a' :{'b':1}}

"""
import random
import urllib.request as req

def fetch_url(url):
    fin = req.urlopen(url)
    return fin.read()

def write_text(txt, filename, enc='utf8'):
    with open(filename, 'w', encoding=enc) as fout:
        fout.write(txt)
    #done, fout will be closed

def get_markov(filename, enc='utf8'):
    with open(filename, encoding=enc) as fin:
        txt = fin.read()
    return Markov(txt)
    

class Markov:
    def __init__(self, data):
        ''' This is the constructor docstring'''
        self.table = get_table(data)

        
    def predict(self, data_in):
        options = self.table.get(data_in, {})
        if not options:
            raise KeyError('{data_in} not found')
        possibles = []
        for dataA, count in options.items():
            for i in range(count):
                possibles.append(dataA)
        #import pdb;pdb.set_trace()
        return random.choice(possibles)


def get_table(data):
    results = {}
    for i , dataA in enumerate(data):
        try:
            dataB = data[i+1]
        except IndexError:
            break
        char_dict = results.get(dataA, {})
        char_dict.setdefault(dataB, 0)
        char_dict[dataB] += 1
        results[dataA] = char_dict
    return results


"""
results is an empty diction

"""
