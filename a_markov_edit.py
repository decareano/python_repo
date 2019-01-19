mport random
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
        import pdb;pdb.set_trace()
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
