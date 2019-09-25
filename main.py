import os

def search_words(available_letters, available_words):
    # TODO replace with your solution!
    found_words=[]
    for w in available_words:
        n1=len(w)
        slovo=[]
        g=[i.split() for i in w]
        y=[slovo.extend(i) for i in g]
        n2='0'
        l=[]
        for k in slovo:         
            if k in available_letters:                
                x=available_letters.index(k)
                n2+=str(k)
                h=available_letters.pop(x)
                l.append(h)            
            else:
                continue
            n3=len(n2)
        if n1!=(n3-1):
            available_letters.extend(l)
            continue
        else:
            found_words.append(w)
    return found_words

# This is input\output boilerplate, you can ignore it - focus on the search_words method
cases = ('a', 'b', 'c', 'd')
for case in cases:

    letter_file_path = os.path.join("input", case + "_letters.txt")
    with open(letter_file_path, "r") as letter_file:
        available_letters = letter_file.read().split("\n")
    letter_file.close()

    word_file_path = os.path.join("input", case + "_words.txt")
    with open(word_file_path, "r") as word_file:
        available_words=word_file.read().split("\n")
    word_file.close()

    found_words = search_words(available_letters, available_words)

    output_file_path = os.path.join("solutions", case + "_result.txt")
    with open(output_file_path, "w") as file_out:
        file_out.write("\n".join(found_words))
    file_out.close()