class Test:
    c="abc"  #class variable

    @classmethod
    def show(cls):
        print("message:",cls.c)
    
Test.show()
