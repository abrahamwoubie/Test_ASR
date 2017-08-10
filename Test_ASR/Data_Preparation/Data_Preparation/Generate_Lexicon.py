#create the dictionary files using word and phone files generated using the phython script Generate_Word_and_Phone_Files.py
# the start and end time stamps of the word and phone are compared to create the dictionary file
import os
import sys
array_list=open(sys.argv[1],'r')
for file_name_word in array_list:
	show=file_name_word[:-1]
	read_file_word=open("/home/abraham/work/SoapBox/Words/"+show+".word",'r')#read the word list 
        write_file=open("/home/abraham/work/SoapBox/Lexicon/"+show+".dict",'w')
	for each_row_word in read_file_word:
		data_word=each_row_word.split(' ') #splits each row using space
		word=data_word[1]
		start_time_word=float(data_word[2]) # current word start time
		end_time_word=float(data_word[3])   # current end start time
		write_file.write(str('%s\t'% (word.lower())))
		read_file_phone=open("/home/abraham/work/SoapBox/Phones/"+show+".phone",'r')# read the phone list
		for each_row_phone in read_file_phone:#read line by line each row of the phone file
			data_phone=each_row_phone.split(' ') #splits each row using space
			phone=data_phone[1]
                        start_time_phone=float(data_phone[2]) # current phone start time
                        end_time_phone=float(data_phone[3]) # current phone end time
			if(start_time_word<=start_time_phone and end_time_word>=end_time_phone):#compare the start and end time of words and phones
	                	write_file.write(str('%s\t'% (phone.lower())))
		write_file.write('\n')
	read_file_word.close()
        write_file.close()
