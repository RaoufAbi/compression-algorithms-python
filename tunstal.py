import math

# convert i to binaire et complet par 0 7sb n
# slice 0b
def binary_fix(i, n):
    binary = bin(i)
    return binary[2:].zfill(n)


# alpha => list char
# prob => probability
# k = ms1ol 3la 9dah mn char fe group
# N  = len(alphabet)
# n = nbr bit
# string
def tunstall_encode(alpha, prob, k, N, n, string):

    final = []
    # add in final list alpha and prob 
    for i in range(N):
        final.append([alpha[i], prob[i]])

    # twsi3 group des symbols
    # jm3 mabin l7rof li 3ndhom proba kbira
    # wtn7i l9dima
    for i in range(k):
        last = max(final, key = lambda x:x[1])
        for i in range(N):
            # add last alph + new alpha , last prob * new proba
            final.append([last[0] + alpha[i], last[1] * prob[i]])
            # remove last mn final
        final.pop(final.index(last))


    # tglb kol group in binar
    for i in range(len(final)):
        final[i][1] = binary_fix(i, n)

    # affichage
    print("The set of alphabets and codes are: ")
    print("Alphabet\tCode")
    print("-------------------------")
    for i in range(len(final)):
        print(final[i][0], end = "\t")
        print(final[i][1])


    stri = list(string)
    encode = ""
    count = 0
    flag = 0
    for i in range(len(stri)):
        for j in range(len(final)):
            # virfi char si exist in final si exist yajoutih ll code
            if stri[i] == final[j][0]:
                encode = encode + str(final[j][1])
                flag = 1
        # flag ==> char daro wla nn
        if flag == 1:
            flag = 0
        else:

            count = count + 1
            if count == len(stri):
                break
            else:
                # dmj charc m3a b3dahom
                stri.insert(i + 1,str(stri[i]+stri[i + 1]))
                # yn7i l7rf l9dif
                stri.pop(i + 2)
    print("coded is :" + string + " is: " + encode)
    return[encode, final, n]


def tunstall_decode(master_directory):
    # code
    encode = master_directory[0]
    # lise de code
    final = master_directory[1]
    # nbr bit
    n = master_directory[2]    

    decode = []
    while encode:
        # add number bit first
        decode.append(encode[:n])
        # remove nbr bit decoder
        encode = encode[n:]
    string = ""

    for i in range(len(decode)):
        for j in range(len(final)):
            # si decode exist in in final code alors string = final[string]
            if decode[i] == str(final[j][1]):
                string = string + final[j][0]
    print("---------------------------------------------------------------")
    print("Decoded string is:", end = " ")
    return string


n = int(input("Enter number of bits: " ))
string = input("Enter the string to be encoded: ")
len_str = len(string)

# creat dict pour la repition
dictionary = dict()

for i in string:
    if i in dictionary:
        dictionary[i] = dictionary[i] + 1
    else:
        dictionary[i] = 1


alphabet = []
probability = []

# item (character, count) in dict
for i in dictionary.items():

    alphabet.append(i[0])       #add char
    probability.append(i[1])    #add count

# Probability Normalization
for i in range(len(probability)):
    probability[i] = probability[i] / len_str

# numbr des symbols
N = len(alphabet)

# ms1ol 3la 9dah mn char fe group
k = math.floor(((2 ** n) - N)/ (N - 1))


master_directory = tunstall_encode(alphabet, probability, k, N, n, string)
print(tunstall_decode(master_directory))