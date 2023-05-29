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

color1 = RGB(0, 153, 255)
print(color1.getHexCode())
print(color1.getBits())
print(color1.getColorShade())

color2 = RGB(255, 153, 204)
print(color2.getHexCode())
print(color2.getBits())
print(color2.getColorShade())

color3 = RGB(0, 87, 0)
print(color3.getHexCode())
print(color3.getBits())
print(color3.getColorShade())

gray = RGB(123, 123, 123)
print(gray.getHexCode())
print(gray.getBits())
print(gray.getColorShade())


import math

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def getLength(self) -> int:
        lineX = math.fabs(self.point2.x - self.point1.x)
        lineY = math.fabs(self.point2.y - self.point1.y)
        return int(math.sqrt(lineX ** 2 + lineY ** 2))

a = Point(3, 1)
b = Point(3, 6)
lineAB = Line(a, b)
print(lineAB.getLength())

c = Point(1, 3)
d = Point(6, 15)
lineCD = Line(c, d)
print(lineCD.getLength())

class BankAccount:
    def __init__(self, bankName: str, ownerName: str, savings: int):
        self.bankName = bankName
        self.ownerName = ownerName
        self.savings = savings

    def withdrawMoney(self, withdrawAmount: int) -> int:
        if self.savings * 0.2 < withdrawAmount:
            self.savings = self.savings - self.savings * 0.2
        else:
            self.savings = self.savings - withdrawAmount
        return int(self.savings)

    def depositMoney(self, depositAmount) -> int:
        if self.savings <= 20000:
            self.savings = self.savings + depositAmount - 100
        else:
            self.savings = self.savings + depositAmount
        return int(self.savings)

    def pastime(self, days: int):
        while days > 0:
            self.savings += 0.25
            days -= 1
        return self.savings

user1 = BankAccount("Chase", "Claire Simmmons", 30000)
print(user1.withdrawMoney(2000))
print(user1.depositMoney(10000))
print(user1.pastime(93))

user2 = BankAccount("Bank Of America", "Remy Clay", 10000)

print(user2.withdrawMoney(5000))
print(user2.depositMoney(12000))
print(user2.pastime(505))


class Files:
    def __init__(self, fileName: str, fileExtension: str, content: str, parentFolder: str):
        self.fileName = fileName
        self.fileExtension = fileExtension
        self.content = content
        self.parentFolder = parentFolder

    def getLifetimeBandwidthSize(self) -> str:
        size = len(self.content) * 25
        return str(size / 1000) + 'GB' if size >= 1000 else str(size) + 'MB'

    def prependContent(self, data: str) -> str:
        self.content = data + self.content
        return self.content

    def addContent(self, data: str, position: int) -> str:
        if position == 0: return data + self.content
        return self.content[:position] + data + self.content[position:]

    def showFileLocation(self):
        fileLocation = self.parentFolder + ' > ' + self.fileName
        if self.fileExtension == '.word':
            return fileLocation + '.word'
        elif self.fileExtension == '.png':
            return fileLocation + '.png'
        elif self.fileExtension == '.mp4':
            return fileLocation + '.mp4'
        elif self.fileExtension == '.pdf':
            return fileLocation + '.pdf'
        else:
            return fileLocation + '.txt'

assignment = Files("assignment", ".word", "ABCDEFGH", "homework")
print(assignment.getLifetimeBandwidthSize())
print(assignment.prependContent("MMM"))
print(assignment.addContent("hello world", 5))
print(assignment.showFileLocation())

blade = Files("blade", ".php", "bg-primary text-white m-0 p-0 d-flex justify-content-center", "view")
print(blade.getLifetimeBandwidthSize())
print(blade.addContent("font-weight-bold ", 11))
print(blade.showFileLocation())
