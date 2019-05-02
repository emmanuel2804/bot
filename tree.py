class Tree:
    def __init__(self, value, left = None, rigth = None):
        self.value = value
        self.left = left
        self.rigth = rigth

    def __eq__(self, another):
        if self.value != another.value:
            return False

        # return self.left == another.left and self.rigth == another.rigth
        left = False
        rigth = False

        if self.left is not None and another.left is not None:
            left = self.left == another.left
        elif self.left is None and another.left is None:
            left = True
        else: return False

        if self.rigth is not None and another.rigth is not None:
            rigth = self.rigth == another.rigth
        elif self.rigth is None and another.rigth is None:
            rigth = True
        else: return False

        return left and rigth

    # def count(self):
    #     result = 1

    #     if self.left is not None: result += self.left.count()
    #     if self.rigth is not None: result += self.rigth.count()

    #     return result