*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions

The program's broad purpose is to decode 'DuckieCode' data. The user will point 
to the data that the program needs to decode by providing a relative file path.
The data has all sorts of flags and indicators to help translate and decode. 

DuckieCorp has provided a nice dictionary to help translate between normal characters
and DuckieCode. The output should be easily readable. The content I wrote from lsn 0-2
like sorting 'dirty' from 'clean' and converting from ASCII to normal characters
should help me immenseley.



# 1.  System Analysis

- The user is prompted to enter a "relative path" for which the program will decrypt.
- We can expect normal **input** to include a combination of one of three flags (`^`, `_`, or `+`), 
and then a number (1-32) representing a character
- If a single combination is invalid (unexpected symbol/out of range number), 
the data is passed over and the next combination is inspected
- `^` represents uppercase, `_` reperesents a lowercase character, `+` represents a special character
- The **output** consists of print statements that write the decrypted characters in order


# 2.  Functional Examples

**pseudocode**
- Obtain input of relative file path
- Read file content
- For each element seperated by a space, keep track of initial flag, and then 
read the following number
- Find associative character from dictionary of number-character provided
by DuckieCorp
- Combine character and flag to produce incremental output
- Repeat until no more bytes are provided from relative file path
- Combine output in normal readable text and print


# 3.  Function Template

**Combine the function stubs written in step #1 with pseudocode from step #2.
Comment out the pseudocode, leaving a valid program that compiles/runs without
errors.  At this stage your program doesn't quite work, but it also doesn't
crash.**

```

    ```
    The user is prompted to enter a "relative path" for which the program will decrypt
    ```
    # Obtain input of relative file path
    # Read file content

    ```
    If a single combination is invalid (unexpected symbol/out of range number), 
    the data is passed over and the next combination is inspected
    ```
    # For each element seperated by a space, keep track of initial flag, and then 
    read the following number
    # Find associative character from dictionary of number-character provided
    by DuckieCorp
    # Character modify by flag type
    # Add to arraylist
    # Repeat until no more bytes are provided from relative file path


    ```
    The **output** consists of print statements that write the decrypted characters in order
    ```
    # Take output item by item from arraylist, combining into single string and printing





```



# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.

One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.

If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.

When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #3 as tests and ensure that each
function passes all.  Doing so discovers mistakes.  Tests also supplement
examples in that they help others read and understand the definition when the
need arises—and it will arise for any serious program.

As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.

If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.

At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.  

The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
