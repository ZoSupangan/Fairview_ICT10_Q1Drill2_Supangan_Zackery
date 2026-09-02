#working with input and output
from pyscript import display, document


#def greetings(e): # initializing a function
#    username = document.getElementById("input1").value # getting the data from a textbox

#    display(f"Hello {username}", target="result")




def multiply_numbers(e):
    document.getElementById("result").innerHTML = "" # clearing the previous result
    first_number = float(document.getElementById("num1").value) 
    second_number = float(document.getElementById("num2").value)
    product = first_number * second_number

    display(f'The product of {first_number} and {second_number} is: {product}', target="result")


def divide_numbers(e):
    document.getElementById("result").innerHTML = "" # clearing the previous result
    first_number = float(document.getElementById("num1").value) 
    second_number = float(document.getElementById("num2").value)
    
    if second_number == 0:
        display("Error: Incalculable", target="result")
    else:
        quotient = first_number / second_number
        display(f'The quotient of {first_number} and {second_number} is: {quotient}', target="result")

def add_numbers(e):
    document.getElementById("result").innerHTML = "" # clearing the previous result
    first_number = float(document.getElementById("num1").value) 
    second_number = float(document.getElementById("num2").value)
    sum = first_number + second_number

    display(f'The sum of {first_number} and {second_number} is: {sum}', target="result")


def subtract_numbers(e):
    document.getElementById("result").innerHTML = "" # clearing the previous result
    first_number = float(document.getElementById("num1").value) 
    second_number = float(document.getElementById("num2").value)
    difference = first_number - second_number

    display(f'The difference of {first_number} and {second_number} is: {difference}', target="result")
