#type casting is used to change from one data type to another
#this has its issues when dealing with str ->strings to integer

#ex-1
variable =10.9
print(int(variable))

#ex-2
#variable = "Aswin"
#print(int(variable))
#error will occur

#ex-3
variable = "10" #when the string is a number
variable = int(variable)
print(type(variable))
#changed from str to int