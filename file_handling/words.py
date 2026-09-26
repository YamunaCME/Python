#searching for word in a file
search_word=input("enter word:")
with open("courses.txt","r") as file:
    content=file.read()
if search_word.lower() in content.lower(): 
    print("word found")
else:
    print("not found")       

#counting the word
count=content.count(search_word)
print(count)