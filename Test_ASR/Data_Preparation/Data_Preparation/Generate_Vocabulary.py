#reads the label files and number of times each word occurs, and sort by frequency of occurrence
import os
import sys

def DIC(Word,count,word):
     
  word_exceptions = False #to discard excpetions like [BEGIN_NOISE] in the sentence and word list

  for w in Word:
     if w==word:
       word_exceptions = True
       break

  if word_exceptions:
   pos=Word.index(word)
   count[pos]=int(count[pos]+1)
  else:
   Word.append(word)
   count.append(1)

  return Word,count

def SORT(Word,count):#to sort the words by their frequencey

  W_fin=[]
  C=[]
  while len(count)>0:
   
    value=max(count)
    pos=count.index(value)
    W_fin.append(Word[pos])
    C.append(value)
    count.remove(value)
    Word.remove(Word[pos])

  return W_fin,C

   
######## Main program ########

lst=open(sys.argv[1],'r')
Word=[] # list of words
count=[] # number of times a word occur
phone_list=[] # list of phones

fi=open('/home/abraham/work/SoapBox/Sentences/sentences.txt','w')

for line in lst:

   show=line[:-1]
   lbl=open("/home/abraham/work/SoapBox/Exams/data/train/"+show+".LBL",'r')
   l=lbl.readlines()
   lbl.close()
   sentence=[]

   for line2 in l:
      exception=0
      data=line2.split()
      data2=data[0].split(':')
      if data2[1][:-1]=='word':
          if '<' in data[1] or '[' in data[1] or 'SIL' in data[1] or '/' in data[1] or '(' in data[1]: # to discard this symbols in the word and sentence list to be generated
            exception=1
          if exception==0:
            Word,count=DIC(Word,count,data[1].lower()) ### We proceed to add and count the word respect the list
            sentence.append(data[1])
      else:
          phone_list.append(data[1].lower())
       
   space=' '
   sen=space.join(sentence)
   fi.write(str('%s\n'%sen))

#lst.close()
fi.close()

W_fin,C=SORT(Word,count)

fi=open('/home/abraham/work/SoapBox/Vocabulary/word_and_frequency.txt','w')

for a in range(len(W_fin)):

   fi.write(str('%s %s\n'%(W_fin[a],C[a])))

fi.close()

phone_list=list(set(phone_list))


