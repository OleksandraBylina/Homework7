class Segment:
    def __init__(self, start1, end1, start2, end2):
        self.start1 = start1
        self.end1 = end1
        self.start2 = start2
        self.end2 = end2
    def is_empty(self):
        if (self.start1 < self.start2) or (self.start1 == self.start2 and ((self.start2 or self.end2 == True)) or  (self.start2 and self.end2 == True)):
            return True
        else:
            return False
    def __add__(self, other):
        if self.start1 <= other.end1 or other.start1 <= self.end1:
            min_start = min(self.start1, other.start1)
            max_end = max(self.end1, other.end1)
        else:
            raise AssertionError
        if self.start1 >= other.start1:
            new_start_point = other.start2
        else:
            new_start_point = self.start2
        if self.end1 >= other.end1:
            new_end_point = self.end2
        else:
            new_end_point = other.end2
    def __mul__(self, other):

    def __str__(self):
        if self.start2 == True and self.end2 == True:
            return f"[{self.start1}, {self.end1}]"
        elif self.start2 == True and self.end2 == False:
            return f"[{self.start1}, {self.end1})"
        elif self.start2 == False and self.end2 == True:
            return f"({self.start1}, {self.end1}]"
        elif self.start2 == False and self.end2 == False:
            return f"({self.start1}, {self.end1})"
if __name__ == "__main__":
    seg = Segment(2, 3, True,  False)
    print (seg)




