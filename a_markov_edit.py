
"""
m = Markov('ab')
m.predict('a')   #look at the predict method
'b'

get_table('ab')
{'a' :{'b':1}}

"""
import random
##import urllib.request as req
##
##def fetch_url(url):
##    fin = req.urlopen(url)
##    return fin.read()
##
##def write_text(txt, filename, enc='utf8'):
##    with open(filename, 'w', encoding=enc) as fout:
##        fout.write(txt)
##    #done, fout will be closed
##
##def get_markov(filename, enc='utf8'):
##    with open(filename, encoding=enc) as fin:
##        txt = fin.read()
##    return Markov(txt)
    

class Markov:
    def __init__(self, data):
        ''' This is the constructor docstring'''
        self.table = get_table(data)

    ## m.predict('a')   #look at the predict method    
    def predict(self, data_in):
        options = self.table.get(data_in, {})  ## options is a dictionary
        if not options:
            raise KeyError(f'{data_in} not found')
        possibles = []  ## is a list
        for char, count in options.items():  ##items is a way to loop over a list
            for i in range(count):
                possibles.append(char)
        return random.choice(possibles)


def get_table(data):
    results = {}
    for i in range(len(data)):
        char = data[i]
        try:
            out = data[i+1]
        except IndexError:
            break
        if char in results:
            c_dict = results[char]
        else:
            c_dict = {}
        print(c_dict)
        if out in c_dict:
            c_dict[out] += 1
            print(c_dict)
        else:
            c_dict[out] = 1
            print(c_dict)
        results[char] = c_dict
    return results


