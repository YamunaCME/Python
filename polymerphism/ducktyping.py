class PDFile:
    def read(self):
        print("pdf file is readed")

class Wordfile:
    def read(self):
        print("word file is readed")

def select_file(obj):
    obj.read()
pdf=PDFile()
word=Wordfile()

select_file(pdf)   