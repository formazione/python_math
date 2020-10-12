from random import randrange
import os


class Exercize:
    def __init__(self, amount, quotes):
        self.amount = amount
        self.quotes = quotes

    def solution(self):
        self.cdr = round(self.amount / sum(self.quotes), 0)
        self.workersums = []
        for hours in self.quotes:
            self.workersums.append(hours * self.cdr)
        return self.workersums

    def print_solution(self):
        print(self.amount, self.quotes)
        print(self.workersums)

    def create_exercise(self):
        self.amount = randrange(1000, 10000, 100)
        self.number = randrange(3, 6)
        self.quotes = [randrange(5, 100, 5) for x in range(self.number)]

    def full_work(self, num, solution=1):
        self.doc = []
        for x in range(num):
            self.create_exercise()

            self.doc.append([
                self.amount,
                self.quotes,
                self.solution()])
        print(self.doc)
        
        for ex in self.doc:
            print(f"Divide this price of {ex[0]} among different employees in proportion to the hours they worked to the project that are listed below:")
            cnt = 0
            for x in ex[1]:
                cnt += 1
                print(f"Worker n. {cnt}:", x)
            
            if solution:
                print("Solutions: ", [str(n + 1) + ". " + str(x) for n, x in enumerate(ex[2])])
            else:
                with open("solution.txt", "w") as file:
                    text = ""
                    for ex in self.doc:
                        text += "".join(str(ex)) + "\n"
                    file.write(text)
            print()
        if solution == 0:
            os.startfile("solution.txt")



ex1 = Exercize(1000, [20, 30, 50])
# sol = ex1.solution()
# ex1.print_solution()

# ex1.create_exercise()
# ex1.solution()
# ex1.print_solution()
ex1.full_work(10, solution=0)
