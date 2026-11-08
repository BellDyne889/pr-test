class IPv4:
    # Octets should be inputted in binary notation in a tuple when creating object.
    def __init__(self, tuple):
        self.binary_address = str(tuple[0]) + "." + str(tuple[1]) + "." + str(tuple[2]) + "." + str(tuple[3])
        self.decimal_address = ""
        for octet in tuple:
            sum = 0
            sum += octet[0] * 128
            sum += octet[1] * 64
            sum += octet[2] * 32
            sum += octet[3] * 16
            sum += octet[4] * 8
            sum += octet[5] * 4
            sum += octet[6] * 2
            sum += octet[7] * 1

            self.decimal_address += str(sum)
            if item.index < 3:
                self.decimal_address += "."

    def __str__(self):