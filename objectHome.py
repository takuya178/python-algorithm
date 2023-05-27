class RGB:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def calcHexCode(self, color_num: int) -> str:
        hex_code_list = '0123456789abcdef'
        hex_code = ''
        if color_num < 10:
            hex_code += '0' + hex_code_list[color_num]
        else:
            while color_num > 0:
                hex_code = hex_code_list[color_num % 16] + hex_code
                color_num = color_num // 16
        return hex_code

    def getDecimalNumList(self, color_hex_num: str) -> list:
        hex_obj = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
        color_hex_num = color_hex_num[1:]
        while color_hex_num.startswith('0'):
            color_hex_num = color_hex_num[1:]

        decimal_list = []
        for char in color_hex_num:
            if char in hex_obj:
                decimal_list.append(hex_obj[char])
            else:
                decimal_list.append(int(char))

        return decimal_list

    def calcBit(self, decimal_list: list) -> str:
        bit_list = []
        for decimal in decimal_list:
            bit = ''
            while decimal >= 0:
                current_binary = str(decimal % 2)
                bit = current_binary + bit
                decimal = decimal // 2
                if decimal == 0: break
            bit_list.append(bit.zfill(4))

        bit = "".join(bit_list)
        while bit.startswith('0'):
            bit = bit[1:]

        return bit

    def colorShade(self, red, green, blue):
        color_num_list = [red, green, blue]
        if red == green == blue:
            return 'grayscale'
        elif max(color_num_list) == green:
            return 'green'
        elif max(color_num_list) == blue:
            return 'blue'
        elif max(color_num_list) == red:
            return 'red'

    def getHexCode(self) -> str:
        return '#' + self.calcHexCode(self.red) + self.calcHexCode(self.green) + self.calcHexCode(self.blue)

    def getBits(self) -> str:
        return self.calcBit(self.getDecimalNumList(self.getHexCode()))

    def getColorShade(self) -> str:
        return self.colorShade(self.red, self.green, self.blue)
