bits_list = []
st = input()
bit_length = len(st)
while (st != ""):
    bits = []
    for b in st:
        bits.append(int(b))
    try:
        st = input()
    except EOFError:
        break


    bits_list.append(bits)
def bits_to_decimal(b: list):
    bits = b
    bits.reverse()
    ret = 0
    for i in range(len(bits)):
        ret += (2**i)*bits[i]

    return ret
