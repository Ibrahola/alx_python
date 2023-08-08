def multiple_returns(sentence):
    if sentence[0] == (" "):
        return "The first string is empty"
    else:
        return sentence
    

go = "At Holberton school, I learnt C!"

length = len(go)
first = go[0]

all = multiple_returns(go)
print("Length: {:d} - First character: {}".format(length, first))

    
