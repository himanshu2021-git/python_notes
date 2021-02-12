words=["orange","banana","apple","orange","papaya","apple","banana","orange","papaya","orange","banana","orange","apple","papaya"]
str="Hi my name is Himanshu"
str1=" "
from collections import Counter
word_counts =Counter(words)
top_three=word_counts.most_common(3)
print(top_three)
spaces=str.isspace()
space=str1.isspace()
print(spaces)
print(space)
