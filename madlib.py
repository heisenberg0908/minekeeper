# this ia a simple madlib program to complete the paragraphs or strings using the input by the user
# it is basically using "fstrings".
name=input("enter your name: ")
country=input("enter your country: ")
state=input("enter your state: ")
city=input("enter your city: ")
age=int(input("enter your age: "))
color=input("enter your favourite color: ")
profession=input("enter your profession: ")
company=input("enter the company in which u are currently working: ")

info=f"hiii, my name is {name}, I am from country {country}, state {state} and city {city}. I am {age} years old and my favourite color is {color}. I am a {profession} and currently working in {company}."
print(info)