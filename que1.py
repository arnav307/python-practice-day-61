from collections import Counter
def counts():
   word='hello world'
   replace=word.replace(" ","")
   count_word=Counter(replace)
   for char,count in count_word.items():
       print(f"{char}:{count}")
counts()