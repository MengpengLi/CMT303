
class cmtOptions:
    def __init__(self, option= "", correctness = False):
        self.option = option
        self.correctness = correctness

    def checkCorrectness(self):
        return self.correctness

    def getOption(self):
        return self.option

    def __str__(self):
        return self.option

    def __getitem__(self, item):
        return self.option