*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions
The programs broad purpose is to obtain command line input that instructs which files to read and transform.
The program will not transform the designated files but instead print created output.

A driver is provided as well as usage statements to help identify and report errors. 


# 1.  System Analysis
- User, using CLI, specifies text tool
- User adds extra arguments (if necessary) and specifies files/redirection
- This constitutes all of user **input**
- Arguments are sent to sys.argv and are evaulated in driver for input error(tt.py)
- **Output** is created in designated src files and either printed or redirected to file

# 2.  Functional Examples
*pseudocode*
- Optain input from CLI
- Input stored in sys.argv and evaluated by driver (tt.py)
- Driver protects from invalid input
- When invalid input is found, usage statements are printed as output
- If input is interpreted as valid, input sent to designated src file
- Create output by reading file(s) and performing text transormation/replication
- If '>' operator is included, redirect output to file
- Else, form output and printe


# 3.  Function Template
`
```
```
User creates input from CLI, sent to driver
```
# Seperate sys.argv input to identify each component
# Verify each component is in valid order/contains valid elements
# If valid, send to designated module
# If invald, print usage() statement

```
Output formed in designated module
```

# Read file(s), open file(s)
# Read line(s) from file(s)
# Evaluate line(s), perform transformation, perform replication
# Print/redirect output
`
```



# 4.  Implementation


# 5.  Testing
Through testing, I discovered that
- cat was printing everything but the last line
- tac was also printing everything but the last line
- paste was reading files in the incorrect order, reversed output
- wordcount formatting was incorrect
All of the tests I used were created using auto-input features in PyCharm configurations and the tests supplied in the 'example' directory
