import shared

def handle_common_bits(bits_list: list, most: bool):
    final_bits = []
    for i in range(shared.bit_length):
        common = 0
        for bits in bits_list:
            if (bits[i] == 1):
                common += 1
            else:
                common -= 1
        isZero = ((common <= 0) == most)
        if (isZero):
            final_bits.append(0)
        else:
            final_bits.append(1)
    ret = shared.bits_to_decimal(final_bits)
    return ret


gamma_rate = handle_common_bits(shared.bits_list, True)
epsilon = handle_common_bits(shared.bits_list, False)
print(gamma_rate*epsilon)

