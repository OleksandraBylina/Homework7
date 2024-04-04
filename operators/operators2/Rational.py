class Integer:
    def __init__(self, string):
        #assert "/" not in string
        self.a = int(string)

    #def string_to_int(self):
        #self.string = int(self.a)
    def __str__(self):
        return f"{self.a}"
    def __call__(self):
        return self.a
    def __getitem__(self, finder):
        if finder == "n":
            return self.a
        elif finder == "d":
            return self.b
    def __add__(self, other):
        return Integer(self.a + other.a)
    def __sub__(self, other):
        return Integer(self.a - other.a)
    def __mul__(self, other):
        return Integer(self.a * other.a)



class Rational(Integer):
    def __init__(self, string):
        num, den = map(int, string.split('/'))
        self.a = num
        self.b = den
    def __str__(self):
        return f"{self.a}/{self.b}"
    def __call__(self):
        return self.a / self.b

    def __add__(self, other):
        # if isinstance(other, Integer): - бо кіт це і кіт і тварина :)

        if type(other) == Integer:
            return Rational(f"{self.a + self.b * other.a}/{self.b}")

        elif type(other) == Rational:
            num = self.a * other.b + self.b * other.a
            den = self.b * other.b
            return Rational(f"{num}/{den}")


    def __sub__(self, other):

        if type(other) == Integer:
            return Rational(f"{self.a - self.b * other.a}/{self.b}")

        if type(other) == Rational:
            num = self.a * other.b - self.b * other.a
            den = self.b * other.b
            return Rational(f"{num}/{den}")

    def __mul__(self, other):
        if type(other) == Integer:
            return Rational(f"{self.a * other.a}/{self.b}")

        if type(other) == Rational:
            num = self.a * other.a
            den = self.b * other.b
            return Rational(f"{num}/{den}")

r1 = Rational("2/3")
r2 = Integer("3")
result = r1 + r2
#print(result)