class Student(object):
    name ="zhangsan"
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.__score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
if __name__ == '__main__':
    bart = Student('Bart Simpson', 59)
    bart.print_score()
    print(bart._Student__score)
    print(bart.name)
    # st1 = Student()
    print(Student.name)