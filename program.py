import json
from difflib import get_close_matches


data = json.load(open('data.json'))
#hihihi

def explain(word):

    word = word.lower()

    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        match = get_close_matches(word, data.keys())[0]
        response = input("did you mean "+match+". press Y if Yes")
        response = response.lower()
        if response == 'y' :
            return explain(get_close_matches(word, data.keys())[0])
        elif response == 'n':
            return "double check"
    else:
        return "doesnt exist"


word = input('Search: ')

output = explain(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)