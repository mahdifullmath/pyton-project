print_queen_counter = 0

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


    
    

    @staticmethod
    def print_queen(s, satr, n):
        global print_queen_counter
        if Globals.promising(s, satr, n):
            
            if satr == n-1:
                row = 0
                
                for i in range(0, n):
                    print("{0:>2s}".format("("), end = '')
                    print("{0:d}".format(row), end = '')
                    print("{0:s}".format(","), end = '')
                    print("{0:d}".format(s[i]), end = '')
                    print("{0:s}".format(")"), end = '')
                    row += 1
                print("{0:s}".format("\n"), end = '')
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

n=int(input("Enter n:"))
Globals.queen(n)