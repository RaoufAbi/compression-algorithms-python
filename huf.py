def huffman_encode(alpha, prob, s):
    final = []
    # in final add alph w proba
    for i in range(len(alpha)):
        final.append([alpha[i], prob[i]])

    # trtbhom mn sghir ll kbir
    final.sort(key = lambda x: x[1])

    tot = 0
    tree = []
    # build arbre
    for i in range(len(final) - 1):
        i = 0
        left = final[i]
        final.pop(i)
        right = final[i]
        final.pop(i)
        tot = left[1] + right[1]
        tree.append([left[0], right[0]])
        final.append([left[0] + right[0],tot])
        final.sort(key = lambda x: x[1])
    code = []
    tree.reverse()
    alpha.sort()
    for i in range(len(alpha)):
        cd = ""
        for j in range(len(tree)):
            # si exist in right tree ==> 0
            if alpha[i] in tree[j][0]:
                cd = cd + '0'
                if alpha[i] == tree[j][0]:
                    break
            # si exist in left tree ==> 0
            else:
                cd = cd + '1'
                if alpha[i] == tree[j][1]:
                    break
        code.append([alpha[i],cd])
    encode = ""
    print("Huffman Codes")
    print("---------------------------------")
    print("Alphabet", end = "\t")
    print("Codeword")
    # affichage
    for i in range(len(code)):
        print(code[i][0], end = "\t\t")
        print(code[i][1])

    for i in range(len(s)):
        for j in range(len(code)):
            if s[i] == alpha[j][0]:
               encode = encode + str(code[j][1])
    print("Huffman Code :" + s + " est " + encode)
    return [encode, code]

# decode
def huffman_decode(master_file):
    # alphbt
    encode = list(master_file[0])
    # prob
    code = master_file[1]
    s = ""
    count = 0
    flag = 0
    for i in range(len(encode)):
        for j in range(len(code)):
            if encode[i] == code[j][1]:
                s = s + str(code[j][0])
                flag = 1
        # flag ==> char daro wla nn
        if flag == 1:
            flag = 0
        else:
            count = count + 1
            if count == len(encode):
                break
            else:
                encode.insert(i + 1,str(encode[i] + encode[i + 1]))
                encode.pop(i + 2)
    print("Decoded string  " + str(master_file[0]) + " is " + s)

    
string = input("Enter the string : ")
len_str = len(string)
dictionary = dict()

# dictionary pour repition de chaque char
for i in string:
    if i in dictionary:
        dictionary[i] = dictionary[i] + 1
    else:
        dictionary[i] = 1


alphabet = []
probability = []

# creat 2 table for char et repit
for i in dictionary.items():
    alphabet.append(i[0])
    probability.append(i[1])

# normalization
for i in range(len(probability)):
    probability[i] = probability[i] / len_str


master_file = huffman_encode(alphabet, probability, string)
huffman_decode(master_file)