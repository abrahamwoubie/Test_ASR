#splits each lable file into two files: word file and phone file
import os
import sys
array_list=open(sys.argv[1],'r')
for file_name_word in array_list:
	show=file_name_word[:-1]
	read_file_word=open("/home/abraham/work/SoapBox/Exams/data/train/"+show+".LBL",'r')#reading the label file
        write_file_word=open("/home/abraham/work/SoapBox/Words/"+show+".word",'w')#for writing the word file
	write_file_phone=open("/home/abraham/work/SoapBox/Phones/"+show+".phone",'w')#for writing the phone file
	for each_row_word in read_file_word:#iterate throguh each line
		data=each_row_word.split()
      		data2=data[0].split(':')#look for the symobol:
		if data2[1][:-1]=='word':#checks whether it is word or phone
			speaker=data[0]
			word=data[1]#word 
                        start_time_word=float(data[2]) # current word start time
                        end_time_word=float(data[3])# current word end time
			t_id=data[4]
			write_file_word.write(str('%s %s %.2f %.2f %s\n'% (speaker,word,start_time_word,end_time_word,t_id)))
		else:   #for the phone part
			speaker=data[0]
                        phone=data[1]
                        start_time_phone=float(data[2]) # current phone start time
                        end_time_phone=float(data[3])  # current phone end time
                        t_id=data[4]
			write_file_phone.write(str('%s %s %.2f %.2f %s\n'% (speaker,phone,start_time_phone,end_time_phone,t_id)))
	read_file_word.close()
        write_file_word.close()
	write_file_phone.close()
