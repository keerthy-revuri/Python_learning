1. Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
The STATION table is described as follows:

id	city		State

1	"Banglore"	"Karnataka"
2	"Hyderabad"	"Telangana"
3	"Warangal"	"Telangana"
4	"Panaji"	"Goa"
5	"Kadapa"	"AP"


Sample Input
-------------
For example, CITY has four entries: DEF, ABC, PQRS and WXY.

Sample Output
--------------
ABC 3
PQRS 4
Explanation

When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with lengths  and . The longest name is PQRS, but there are  options for shortest named city. Choose ABC, because it comes first alphabetically.

--------------------------------
------>Solution using UNION ALL -
--------------------------------

Note - UNION removes duplicate records (where all columns in the results are the same), UNION ALL does not.

(Select city ,LENGTH(city)  from station where LENGTH(city)= (Select  Min(LENGTH(city)) from Station) 
ORDER BY City LIMIT 1)  
UNION ALL
(Select city ,LENGTH(city)  from station where LENGTH(city)= (Select  Max(LENGTH(city)) from Station) 
ORDER BY City DESC LIMIT 1);

-------------
Explaination - 
-------------
Here, Min, Max is used to find lengths of cities in 2 separate queries, those 2 are joined dusing UNION ALL.


--------------------------------------
----->Solution using window functions - 
--------------------------------------
with station_temp as (
select *, length(city) as city_length from station),

station_temp2 as (
select *,row_number() over (partition by city_length order by city asc) as rw  from station_temp),

station_temp3 as (
Select * from station_temp2 where city_length = (Select  Min(city_length) from station_temp2) 
OR city_length = (Select Max(city_length) from station_temp2))

select city, city_length from station_temp3 where rw = 1;

---------------
Explaination - 
--------------
Here, Min, Max , Length functions gives the shortest, longest , length of cities respectively, but the problem is if there are more than 1 largest or smallest city then only 1 i.e., 
first city has to be chosen when ordered alphabetically
So, for this breakdown the query and write in form of CTE's
1. station_temp CTE - length(city) is calculated and returned as city_length
2. station_temp2 CTE - window function - row_number() is used. So here Window functions applies aggregate and ranking functions over a particular window (set of rows). OVER clause is used with window functions to define that window. OVER clause does two things : 

Partitions rows into form set of rows. (PARTITION BY clause is used) 
Orders rows within those partitions into a particular order. (ORDER BY clause is used) 
Note: If partitions aren’t done, then ORDER BY orders all rows of table

----------------
ROW_NUMBER() – 
----------------
It assigns consecutive integers to all the rows within partition. Within a partition, no two rows can have same row number. 

So, partition is done on length of cities, then on those partitions Order by is applied, unique row numbers are given within partition ( here Kadapa, Panaji  have same length , so order by is used to order and Kadapa is returned)

3. station_temp3 - in this Min, Max is calculated

4. Now as the rows are partitioned using row number, final query is written to select the city which has  row_number = 1





 




