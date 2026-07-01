def verify_trapdoor(counts, expected):

    zero = 0
    one = 0

    for state, shots in counts.items():

        # Extract trapdoor bit
        trap_bit = state.split()[0][0]

        if trap_bit == '0':
            zero += shots
        else:
            one += shots

    total = zero + one

    probability_zero = zero / total

    # =====================================
    # SECURITY DECISION
    # =====================================

    secure = probability_zero > 0.9

    imbalance = probability_zero

    return secure, imbalance