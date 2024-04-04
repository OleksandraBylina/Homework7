from Rational import Integer
from Rational import Rational
from fractions import Fraction
class Reader:
    def __init__(self, file_name):
        self.file_name = file_name
    def read(self):
        total_results = []
        with open(self.file_name) as f:
            for line in f:

                data = line.split()
                while data:
                    if len(data) == 1:
                        break
                    if data[1] == "*":
                        try:
                            if "/" in data[0] and "/" in data[2]:
                                new = Rational(data[0]) * Rational(data[2])
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                            elif "/" not in data[0] and not "/" in data[2]:
                                new = Integer(data[0]) * Integer(data[2])
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                            elif "/" in data[0] and "/" not in data[2]:
                                new = Rational(data[0]) * Integer(data[2])
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                            elif "/" not in data[0] and "/" in data[2]:
                                new = Rational(data[2]) * Integer(data[0])
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                        except IndexError:
                            break
                    elif data[1] == "+":
                        try:
                            if "/" in data[0] and "/" in data[2]:
                                new = Rational(data[0]) + Rational(data[2])
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                            elif "/" not in data[0] and not "/" in data[2]:
                                new = Integer(data[0]) + Integer(data[2])
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                            elif "/" in data[0] and "/" not in data[2]:
                                new = Rational(data[0]) + Integer(data[2])
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                            elif "/" not in data[0] and "/" in data[2]:
                                new = Rational(data[2]) + Integer(data[0])
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                        except IndexError:
                            break
                    elif data[1] == "-":
                        try:
                            if "/" in data[0] and "/" in data[2]:
                                new = Rational(data[0]) - Rational(data[2])
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                            elif "/" not in data[0] and not "/" in data[2]:
                                new = Integer(data[0]) - Integer(data[2])
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                            elif "/" in data[0] and "/" not in data[2]:
                                new = Rational(data[0]) - Integer(data[2])
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                            elif "/" not in data[0] and "/" in data[2]:
                                new = ( Rational(data[2]) - Integer(data[0]))
                                data[0] = f"{new}"
                                del data[1]
                                del data[1]
                        except IndexError:
                            break
        #return (data)
                total_results.append(data)
        return total_results
if __name__ == "__main__":
    reader = Reader("input01.txt")
    results = reader.read()
    #results = reader.normal_result_maker()
    print (*results)
