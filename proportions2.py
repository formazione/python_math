# python_math 1
# proportions
import random
import os
import pdfkit

'''
to install pdfkit


'''


class Prop:
    def __init__(self, prop):
        '''This is how you put the argument e1 : e2 = m1 : m2 
        ie: 12 : 3 = 36:9
        '''
        print(prop)
        self.proportion = prop
        # replace = with :
        prop = prop.replace("=", ":")
        # create a list with the numbers, splitting by the ':'
        self.prop = prop.split(":")
        # converts strings into integers and x to None
        for n, x in enumerate(self.prop):
            if x.strip() == "x":
                self.prop[n] = None
            else:
                self.prop[n] = int(x)
        # memorize in memorable names the extrem and medium terms
        e1, m1, m2, e2 = self.prop
        self.e1 = e1
        self.e2 = e2
        self.m1 = m1
        self.m2 = m2
        self.cnt = 1
        self.excnt = 1
        self.calculate_x()

    def calculate_x(self):
        "Call this from the istance to find the incognito"
        # Depending on what is None (incognito), it finds it with the other 3
        if self.e1 is None:
            res = self.m1 * self.m2 / self.e2
        elif self.e2 is None:
            res = self.m1 * self.m2 / self.e1
        elif self.m1 is None:
            res = self.e1 * self.e2 / self.m2
        elif self.m2 is None:
            res = self.e1 * self.e2 / self.m1
        print(f"x = {res}\n")
        return res

    def exercize(self, number, solution=1):
        self.text = ""
        self.text_sol = ""
        for i in range(number):
            print("Exercize n." + str(self.cnt))
            self.ratio = random.randrange(2, 8)
            self.rm1 = random.randrange(100, 1000)
            self.re1 = self.rm1 * self.ratio
            self.rel = random.randrange(9, 14)
            self.re2 = self.rm1 * self.rel
            self.rm2 = self.re2 * self.ratio
            self.list = [self.re1, self.rm1, self.rm2, self.re2]
            print(self.list)
            index = random.randrange(0, 3)
            self.sol = self.list[index]
            self.list[index] = "x"
            a, b, c, d = [str(x) for x in self.list]
            pstring = "".join([a, " : ", b, " = ", c, " : ", d])
            print(pstring)
            if solution:
                print(self.sol)
            else:
                print("Solution: __________________ = _____")
            print("======================")
            self.cnt += 1
            self.text += str(self.cnt - 1) + ") " + pstring
            self.text += "   Sol.: ______________________ = __________\n"
            self.text_sol += str(self.cnt - 1) + ") " + pstring + " - Sol:" + str(self.sol) + "\n"
        return self.text, self.text_sol

    def print_exercizes(self):
        with open(f"ex\\esercizi{self.excnt}.txt", "w") as file:
            file.write(self.text)
        # os.startfile(f"esercizi{self.excnt}.txt")
        with open(f"ex\\esercizi_sol{self.excnt}.txt", "w") as file:
            file.write(self.text_sol)
        # os.startfile(f"esercizi_sol{excnt}.txt")
        self.excnt += 1



if __name__ == "__main__":

    p1 = Prop("12 : 3 = 36 : x")
    full = ""
    full_sol = ""
    for n in range(15):
        text, text_sol = p1.exercize(10, solution=1)
        p1.print_exercizes()
        full += text
        full_sol += text_sol
    # Contains all the exercises in one file
    with open("ex\\full.txt", "w") as file:
        file.write(full)
    pdfkit.from_file("ex\\full.txt", "ex\\full.pdf")
    os.startfile("ex\\full.txt")
    with open("ex\\full_sol.txt", "w") as file:
        file.write(full_sol)
    pdfkit.from_file("ex\\full_sol.txt", "ex\\full_sol.pdf")
    os.startfile("ex\\full_sol.txt")
    # convert to pdf


