def eve_attack(qc):

    print("[EVE] Intercepting quantum channel!")

    qc.measure(1, 1)

    return qc, True