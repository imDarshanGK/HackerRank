# HackerRank Find a string
Find a string.

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints

1 < len(string) < 200

Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

    ABCDCDC
    CDC
    
Sample Output

    2
    
Concept

Some string processing examples, such as these, might be useful.

There are a couple of new concepts:

In Python, the length of a string is found by the function len(s), where  is the string.

To traverse through the length of a string, use a for loop:

        for i in range(0, len(s)):
            print (s[i])
            
A range function is used to loop over some length:

        range (0, 5)
        
Here, the range loops over 0 to 4.5  is excluded.

# HackerRank Finding the percentage
Finding the percentage 

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example

marks key:value pairs are

'alpha': [20,30,40]

'beta': [30,50,70]

query_name='beta'

The query_name is 'beta'. beta's average score is (30+50+70)/3 = 50.0 .

Input Format

The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints
* 2 < n 10
* 0 < marks[i] < 100
* length of marks arrays = 3

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

        3
        Krishna 67 68 69
        Arjun 70 98 63
        Malika 52 56 60
        Malika
Sample Output 0

      56.00
Explanation 0

Marks for Malika are {52,56,60} whose average is 52+56+60/3 => 56

Sample Input 1

      2
      Harsh 25 26.5 28
      Anurag 26 28 30
      Harsh
Sample Output 1

        26.50
# HackerRank write a function
HackerRank write a function

Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format

Read year, the year to test.

Constraints

1900 < year < 10^5

Output Format

The function must return a Boolean value (True/False). Output is handled by the provided code stub.

Sample Input 0

      1990
Sample Output 0

      False
Explanation 0

1990 is not a multiple of 4 hence it's not a leap year.
# HackerRank If Else
If Else

Task

Given an integer, , perform the following conditional actions:

* If n is odd, print Weird
* If n is even and in the inclusive range of 2 to 5, print Not Weird
* If n is even and in the inclusive range of 6 to 20, print Weird
* If n is even and greater than 20, print Not Weird

Input Format

A single line containing a positive integer,n .

Constraints
 * 1 < n < 100
 
Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

     3
Sample Output 0

    Weird
Explanation 0

n=3

n is odd and odd numbers are weird, so print Weird.

Sample Input 1

    24
Sample Output 1

     Not Weird
Explanation 1

n=24

 n>20 and nis even, so it is not weird.
