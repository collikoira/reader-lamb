import pandas

def search_from_text(item):
    with open("text.txt", 'r') as dummy:
        for line in dummy:
            # reading word
            for word in line.split():
                if word == item:
                    return True


with open("../english/adjectives/500_adjectives") as common:
    for words in common:
        stripped = words.rstrip('\n')
        if search_from_text(stripped):
            print(stripped)

