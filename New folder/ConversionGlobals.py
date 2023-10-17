class Globals:

    @staticmethod
    def promising(s, satr, n):
        if satr == 0:
            return True
        i = 0
        while i <= satr - 1:
            for j in range(i + 1, satr + 1):
                if (s[i] >= n) or (s[j] >= n) or (s[i] == s[j] or i - j == s[i] - s[j] or i - j == s[j] - s[i]):
                    return False
            i += 1
        return True


    #C++ TO PYTHON CONVERTER NOTE: This was formerly a static local variable declaration (not allowed in Python):
    print_queen_counter = 0

    @staticmethod
    def print_queen(s, satr, n):
        #C++ TO PYTHON CONVERTER NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static int counter = 0
        if Globals.promising(s, satr, n):
            if satr == n-1:
                row = 0
                if row != 0:
                    print_queen_counter += 1
                print("{0:>3d}".format(print_queen_counter), end = '')
                print("{0:d}".format(": "), end = '')
                for i in range(0, n):
                    print("{0:>2d}".format("("), end = '')
                    print("{0:d}".format(row), end = '')
                    print("{0:d}".format(","), end = '')
                    print("{0:d}".format(s[i]), end = '')
                    print("{0:d}".format(")"), end = '')
                    row += 1
                print("{0:d}".format("\n"), end = '')
            else:
                for j in range(0, n):
                    s[satr + 1] = j
                    Globals.print_queen(s, satr+1, n)

    @staticmethod
    def queen(n):
        s = [0 for _ in range(n)]
        for i in range(0, n):
            s[0] = i
            Globals.print_queen(s, 0, n)