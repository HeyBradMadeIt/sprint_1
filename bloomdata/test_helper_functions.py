import bloomdata.helper_functions as hf

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

list01 = [1,2,3]
list02 = [4,5,6]

def test_random_phrase():
    assert type(hf.random_phrase(adjectives, nouns)) == str
    assert type(hf.random_phrase(list01, list02)) == str