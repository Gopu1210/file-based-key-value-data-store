import code as x 
key_name=0
value=0
timeout=0


create("sastra",25)
#to create a key with no time-to-live property


create("src",70,3600) 
#to create a key with time-to-live property value given(number of seconds)


read("sastra")


read("src")
#since we gave time to live property it shud display the content or else will show an ERROR message.


create("sastra",50)
#it returns an ERROR since the key_name already exists in the database


 
delete("sastra")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
time.sleep(10)
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
time.sleep(10)
