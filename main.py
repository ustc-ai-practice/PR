print("I'm happy to edit this file, it's a test file!")
print("i am also happy to edit this file!")

print("I'm happy to edit this file too (huaji.jpg)")
print("1231231231321123123131321321321321321321231321321321321313132132131313131313")
import time
sentence = "Dear, I love you forever!"
for char in sentence.split():
   allChar = []
   for y in range(12, -12, -1):
       lst = []
       lst_con = ''
       for x in range(-30, 30):
            formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if formula <= 0:
                lst_con += char[(x) % len(char)]
            else:
                lst_con += ' '
       lst.append(lst_con)
       allChar += lst
   print('\n'.join(allChar))
   time.sleep(1)
