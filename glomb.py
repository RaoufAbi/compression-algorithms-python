import math

# dir unary code 0 or 1
def unary(q):
    code1 = []
    for i in range(q):
        code1.append(1)
    # append 0 ==> llichra ll fin
    code1.append(0)
    # convert to str
    code2 = [str(i) for i in code1]
    # convert list to str
    code = "".join(code2)
    return code


def rem_trun(r, k):
    # convert to binaire
    rem = bin(r)
    # slice 0b li tji mn bin() 
    # zfill() tzid les zeros 7sb ll k
    return rem[2:].zfill(k)


def encode_golomb(n, m):
    # calcule q
    # floor ==> tjib parte li 9bl fasla
    q1 = (n / m)
    q = math.floor(q1)

    # creat code unary ll q
    unary_code = unary(q)

    # calcule k = log2 (m)
    k1 = math.log(m, 2)
    # tjib akbr numero s7i7 ll k ==> 2.3 -> 3
    k = math.ceil(k1)
    # Calculate the parameter c
    c = ((2 ** k) - m)

    # r = ba9i l9sma
    r = n % m


    if (r >= 0 and r < c):
        r1 = rem_trun(r, k - 1)
        return [unary_code + r1, m]
    else:
        r1 = rem_trun(r + c, k)
        return [unary_code + r1, m]

    
def decode_golomb(master_directory):
    m = master_directory[1]
    code = list(master_directory[0])
    k1 = math.log(m, 2)
    k = math.ceil(k1)
    c = ((2 ** k) - m)
    q = 0
    # get q => kol 1 in code q=q+1 jusqa 0
    for i in range(len(code)):
        if int(code[i]) == 1:
            q = q + 1
        else:
            break

    # Remove the unary part
    for i in range(q + 1):
        code.pop(0)

    # convert to str
    code1 = [str(i) for i in code]
    code2 = "".join(code1)


    n = 0
    r1 = []


    for i in range(k - 1):
        r1.append(code[i])


    r2 = [str(i) for i in r1]
    r3 = "".join(r2)
    r = int(r3, 2)
    rc = 0


    if r < c:
        n = q * m + r

        print(f"n : {n}")
        print(f"m : {m}")

    else:
        r1 = []
        for i in range(k):
            r1.append(code[i])
        r2 = [str(i) for i in r1]
        r3 = "".join(r2)
        rc = int(r3, 2)
        n = q * m + rc - c

        print(f"n : {n}")
        print(f"m : {m}")

    
    
n = int(input("Enter value of n: "))
m = int(input("Enter value of m: "))
master_directory = encode_golomb(n, m)
print()
print()
print("Golomb Code is: ", master_directory[0])
print()
print("decode golomb")
decode_golomb(master_directory)