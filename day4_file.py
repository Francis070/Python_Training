#txt,json, word, csv, pdf
#json, csv or pandas, mypdf

# file_obj=open("garima.txt","w")
# file_obj.write("welcome to india")
# file_obj.close()


#context Manager-better way to do write operation
# with open("garima.txt","w") as file_obj:
#     file_obj.write("welcome to australia")#here data is overridden
#bcoz of pointer-pointer is going to first position
#so use add method using a .to append in the file
# with open("garima.txt","a") as file_obj:
#     file_obj.write("welcome to tokyo2021")


#An edit made
#input file name from user and add .txt as extension
# file_name=input("Enter your filename:")
# if file_name.strip().endswith(".txt"):
#     pass
# else:
#     file_name=file_name+".txt"
#     file_name=file_name.strip() #to remove extra spaces
# file_mode=input("Enter the mode of operation")
# file_mode=file_mode.lower().strip()
# if file_mode in ["a","w","a+","w+","r"]:
#     pass
# else:
#     file_mode="w"
# with open(file_name,file_mode) as file_obj:
#     file_content=input("Enter your file content:")
#     file_obj.write(file_content.strip())


# with open("garima.txt","a") as file_obj:
#     file_obj.write("india")
#     file_obj.write("\n")
# with open("garima.txt","r") as file_obj:
#     file_content=file_obj
#     #print(file_content)
#     file_content_1=file_obj.read()
#     print(file_content_1)#gives empty output bcoz cursor is at end
# with open("garima.txt","r") as file_obj:
#     file_content=file_obj.read(3)#only read first three characters
#     #print(file_content)
#     file_content_1=file_obj.read()
#     print(file_content_1)
#
# with open("garima.txt","r") as file_obj:
#     file_content=file_obj.readline()# reads line by line
#     print(file_content)
#     file_content_1=file_obj.readline()
#     print(file_content_1)
# with open("garima.txt","r") as file_obj:
#     file_content=file_obj.readline(2)# reads line by line but only first two characters
#     print(file_content)
#     file_content_1=file_obj.readline()
#     print(file_content_1)


# with open("garima.txt","r") as file_obj:
#     file_content=file_obj.readlines()# readlines is most usable function bcoz it gives output in list with every data\n
#     print(file_content)
#     #now data without \n
#     output=[x.strip("\n") for x in file_content]
#     print(output)


# with open("garima.txt","a+") as file_obj:
#     file_obj.write("paris 2023 olympics")
#     file_obj.seek(0)#asking pointer to go at 0 position
#     file_content=file_obj.read()
#     print(file_content)
# with open("garima.txt","r+") as file_obj:
#     file_content=file_obj.read()
#     print(file_content)
#     file_obj.write("newyotk")
#     file_obj.seek(0)#asking pointer to go at 0 position


#creating new file every time by  default
# with open("garima.txt","r") as file_obj:
#     file_content=file_obj.readlines()
#     print(file_content)
#     new_contents=[x.strip("\n") for x in file_content]
#     print(new_contents)
#     for x in new_contents:
#         file_name=x.strip()+".txt"
#         with open(file_name,"w") as obj:
#             obj.write("hello welcome")


# from datetime import datetime
# current_time=datetime.now()
# print(current_time.replace(microsecond=0))
# print(type(current_time))
# #2021-08-19 11:26:11
# time_format="%Y_%m_%d_%H_%M_%S"
# format_time=datetime.strftime(current_time,time_format)
# print(format_time)
# print(type(format_time))

# from datetime import datetime
# import time
# with open("garima.txt","r") as file_obj:
#     file_content=file_obj.readlines()
#     print(file_content)
#     new_contents=[x.strip("\n") for x in file_content]
#     print(new_contents)
#     for x in new_contents:
#         file_name=x.strip()+".txt"
#         time.sleep(2)
#         with open(file_name,"w") as obj:
#             obj.write("hello welcome")
#
#Regular Expressions
#import re
# import re
# my_data="dhoni is greater than kholi"
# my_output=re.match("dhoni",my_data,re.I)
# print(my_output)
# print(my_output.group())

# import re
# my_data="dhoni is greater than kholi"
# my_output=re.search("is",my_data,re.I)
# print(my_output.group())
# print(my_output.span())#returns the index from where i is starting and s is ending

#
# import re
# my_data="<html><head><body>" #greedy statement
# my_output=re.match("<.*>",my_data,re.I)
# print(my_output.group())
# print(my_output.span())


# import re
# my_data="<html><head><body>" #Non-greedy statement
# my_output=re.match("<.*?>",my_data,re.I)
# print(my_output.group())
# print(my_output.span())

# import re
# my_data="india is better than australia"
# my_output=re.search(".* is .*",my_data)
# print(my_output.group())
# print(my_output.group(1))#group which is before the word "is"
# print(my_output.group(2))#group which is after the word "is"
###so here i formed two groups and its getting reflected

# import re
# my_data="india is better than australia"
# my_output=re.search("(.* )is (.*) (.*)",my_data)
# print(my_output.group())
# print(my_output.group(1))#group which is before the word "is"
# print(my_output.group(2))
# print(my_output.group(3))
# import re
#
# my_data="!!! India won with 454439 balls remaining against SRILANKA on 2019 with 330 on score"
# my_output=re.findall("\d{1,3}",my_data) #all numbers grouping every first three elements it is just moving sequential not doing any mathematical operation
# print(my_output)
# import re
#
# my_data="!!! India won with 454439 balls remaining against SRILANKA on 2019 with 330 on score"
# my_output=re.findall("\D{1,3}",my_data) #return non numbers in 3 digit format
# print(my_output)



# import re
#
# my_data="!!! India won with 454439 balls remaining against SRILANKA on 2019 with 330 on score"
# my_output=re.findall("\w",my_data) #return every character
# print(my_output)



# import re
#
# my_data="!!! India won with 454439 balls remaining against SRILANKA on 2019 with 330 on score"
# my_output=re.findall("\w*",my_data) #return only words and insttead of words gives empty space
# print(my_output)

# import re
#
# my_data="!!! India won with 454439 balls remaining against SRILANKA on 2019 with 330 on score"
# my_output=re.findall("\w+",my_data) #return only words no extra sign will be counted
# print(my_output)


#subsititute function
# import re
#
# my_data="!!! India won with 454439 balls remaining against SRILANKA on 2019 with 330 on score"
# my_output=re.sub("\W","_",my_data) #where words are not there put _ there
# print(my_output)


# import re
#
# my_data="India Indian Indiana"
# my_output=re.match("^I...$",my_data)#error object has no attribute group
# print(my_output.group)

# import re
#
# my_data="!!! India won with 454439 balls remaining against SRILANKA on 2019 with 330 on score"
# my_output=re.split("\W",my_data) #where words are not there put _ there
# print(my_output)



#1.use sqlite3 db
#2.file operations

# def fun():
#     var=10
#     yield var
#     var =var+10
#     yield var
#     var=var+10
#     yield var
# f=fun()
# print(next(f))
# print(next(f))
# print(next(f))#yield stores the next state of function

#importing from csv files
# import csv
# filename="dhoni.csv"
# fields=[]
# rows=[]
# with open(filename,'w')as csvfile:
#     csvreader=csv.reader(csvfile)#creating a csv
#     fields=next(csvreader)#extracting field names through first row
#     for row in csvreader:
#         rows.append(row)#extracting each data row one by one
#     #get total number of rows
#     print("Total no.of rows: %d"%(csvreader.line_num))
# #printing the field names
# print('Field names are:' + ', '.join(field for field in fields))
#
# #print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#     #parsing each column of a row
#     for col in row:
#         print("%22s"%col)
#     print('\n')




# import csv
# fields=['Name','Branch','Year','CGPA']
# rows=[['Nikhil','COE','2','9.4']]
# filename="university_records.csv"
# with open(filename,'w',newline="") as csvfile:
#     #creating a csv writer object
#     csvwriter=csv.writer(csvfile)
#     #writing the fields
#     csvwriter.writerow(fields)
#     #writing the data rows
#     csvwriter.writerows(rows)


# import csv
# mydict=[{'branch':'COE','cgpa':'9.0','name':'Nikhil','year':'2'}]
# fields=['name','branch','year','cgpa']
# filename="university_records.csv"
# with open(filename,'w')as csvfile:
#     #creating a csv dict writer object
#     writer=csv.DictWriter(csvfile,fieldnames=fields)
#     #writing header(field names)
#     writer.writeheader()
#     #writing data rows
#     writer.writerows(mydict)

# import pandas
# #Series, DataFrame, Panels
# #1X,2X,3X
#
# var=["a","b","c"]
# output=pandas.Series(var)
# print(output)

# import pandas
# #Series, DataFrame, Panels
# #1X,2X,3X
#
# var=[1,3,4,5,6]
# output=pandas.Series(var)
# print(output.sum())


# import pandas
# #Series, DataFrame, Panels
# #1X,2X,3X
#
# var=[1,3,4,5,6]
# output=pandas.Series(var)
# print(output.cumsum())


import pandas
#Series, DataFrame, Panels
#1X,2X,3X

var=[[1,2,3,4],[4,5,3,2]]
output=pandas.DataFrame(var)
print(output)
data=output.to_csv("garima3.csv")
print(data)
