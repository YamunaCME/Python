text1 = input("enter text:")
text2= input("enter second text:")
if sorted(text1) == sorted(text2):
    print("Anagrams")
else:
    print("not anagrams")    