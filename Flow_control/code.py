# --------------
#Code starts here

#Function to read file
def read_file(path):
    file=open(path,'r')
    sentence=file.readline()
    file.close()
    return sentence
    
    #Opening of the file located in the path in 'read' mode
    
    #Reading of the first line of the file and storing it in a variable
    
    #Closing of the file
    
    #Returning the first line of the file
    
sample_message=read_file(file_path)   

#Calling the function to read file

#Printing the line of the file
message_1=read_file(file_path_1)
print(message_1)
message_2=read_file(file_path_2)
print(message_2)

#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quotient=int(message_b)//int(message_a)
    return str(quotient)
    #Returning the quotient in string format
secret_msg_1=fuse_msg('2222','2477')
#Calling the function to read file  

#Calling the function to read file

message_3=read_file(file_path_3)
print(message_3)#Calling the function 'fuse_msg'


#Printing the secret message 



#Function to substitute the message
def substitute_msg(message_c):
    sub=''
    if message_c=='Red':
        sub="Army General"
    elif message_c=='Green':
        sub='Data Scientist'
    elif message_c=='Blue':
        sub='Marine Biologist'
    return sub

    #If-else to compare the contents of the file
    
    
    #Returning the substitute of the message
    
secret_msg_2=substitute_msg('Green')   

#Calling the function to read file


#Calling the function 'substitute_msg'


#Printing the secret message
message_4=read_file(file_path_4)
message_5=read_file(file_path_5)


#Function to compare message
def compare_msg(message_d,message_e):
    final_msg=' '
    a_list=message_d.split()
    b_list=message_e.split()
    c_list=[i for i in a_list if i not in b_list]
    final_msg=final_msg.join(c_list)
    return final_msg
secret_msg_3=compare_msg(message_4,message_5)
message_6=read_file(file_path_6)
print(message_6)


    #Splitting the message into a list
    
    
    #Splitting the message into a list
    
    
    #Comparing the elements from both the lists
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    

#Calling the function to read file


#Calling the function to read file


#Calling the function 'compare messages'


#Printing the secret message


#Function to filter message
def extract_msg(message_f):
    a_list=message_f.split()
    even_word=lambda x:len(x)%2==0
    #Splitting the message into a list
    b_list=list(filter(even_word,a_list))
    final_msg=' '.join(b_list)
    return final_msg
secret_msg_4=extract_msg(message_6)
 
    #Creating the lambda function to identify even length words
    
    
    #Splitting the message into a list
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    
#Calling the function to read file


#Calling the function 'filter_msg'


#Printing the secret message


#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1,secret_msg_4, secret_msg_2]
secret_msg=secret_msg_3+' '+secret_msg_1+' '+secret_msg_4+' '+secret_msg_2
print(secret_msg)# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message


#Function to write inside a file
def write_file(secret_msg,path):
       
    #Opening a file named 'secret_message' in 'write' mode

    f=open(path,'a+')
    f.write(secret_msg)
    f.close()
    #Writing to the file


    #Closing the file
write_file(secret_msg,final_path)
print(secret_msg)
#Calling the function to write inside the file    


#Printing the entire secret message


#Code ends here


