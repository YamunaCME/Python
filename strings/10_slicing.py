#slicing examples

s1="123456789"
print(s1[:])
print(s1[:9])#omitting the start index
print(s1[0:])#omitting the end index

#  copying string using slicing
s2="yamuna"
s3=s2[:]
print("copied string:",s3)

#slicing using step vaule
s4="12434687"
print(s4[0::2])

#reversing a string using slicing
s4="134528"
print(s4[::-1])

#negative slicing
text = "Python Programming"
print(text[-11:])
