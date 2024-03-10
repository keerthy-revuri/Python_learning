

SHOW ALL - returns data like description, name, parameter
SHOW TIMEZONE - displays current time zone
SELECT NOW() - displays time stamp with timezone
SELECT TIMEOFDAY() - displays timestamp with timezone as string
SELECT CURRENT_DATE , SELECT CURRENT_TIME - displays date and time

EXTRACT() - allows to extract or obtain sub component of a date value - 
year, month, day , week , quarter
ex - EXTRACT(YEAR FROM date_column)

AGE() - calculates and returns the current age along with timestamp
ex - AGE(date_column)

TO_CHAR() - general function used to convert data types to text
useful for timestamp formatting
ex - TO_CHAR(date_column, 'dd-mm-yyyy')

ex - SELECT EXTRACT(YEAR FROM payment_date) FROM payment;

Note - https://www.postgresql.org/docs/12/functions-formatting.html

- EXTRACT DOW FROM timestamp - gives DAY in a week - 0 to 6, Sunday takes 0 , Monday takes 1, ....


- Mathematical Operations - 
- https://www.postgresql.org/docs/current/functions-math.html

- String Functions and Operators - 
- https://www.postgresql.org/docs/current/functions-string.html
- String concatenation - string || string or string || non-string
- LENGTH( String) gives length of a string
- LEFT(first_name, 1) - gives first letter of first_name
- LOWER(name) - gives name in lower case letters
- 
