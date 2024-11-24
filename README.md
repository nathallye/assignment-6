# Assignment #6

Assignment Tasks:

## Create the User Input Form (Optional):

Write a PHP script named form.php that includes a form where users can input a list of integers.

The form should have:
- Input fields where users can input a series of integers separated by commas.
- A submit button labeled "Submit".
> Alternatively, users can send values directly via URL parameters.

## Create the Python Script:

Create a Python script bitwise_operations.py that processes a list of integers and performs the following operations:

- Input Validation: Retrieves the values from user input (either from the form or URL).
- Validate the input to ensure it contains only integers.
- Bitwise Operations:
  - Calculate the AND, OR, and XOR of all integers in the list.
  - Output the results of each operation.
- Filtering with Loops:
  - Use a loop to filter and display all numbers greater than a user-specified threshold.

## Create the PHP Script to Process Input:

- Write a PHP script named process.php that:
  - Receives the user input from form.php or URL parameters.
  - Calls bitwise_operations.py to process the input and capture the output.

### Example Input/Output:

```
Integers separated by commas: 3, 5, 7, 9  
Threshold: 4  

Bitwise AND: 1  
Bitwise OR: 15  
Bitwise XOR: 14  
Numbers greater than threshold: [5, 7, 9]
```
