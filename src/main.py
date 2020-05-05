import pandas
with open("../english/adjectives/500_adjectives") as common:
    with open("text.txt", 'r') as dummy:
        for words in common:
            stripped = words.rstrip('\n')
            for line in dummy:
                # reading word
                for word in line.split():
                    if word == stripped:
                        print(word)


