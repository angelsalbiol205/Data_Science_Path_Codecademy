-- 1
-- What are the column names?
SELECT *
FROM transaction_data
LIMIT 10;

-- 2
-- Find the full_names and emails of the transactions listing 20252 as the zip code.
SELECT full_name, email
FROM transaction_data
WHERE zip = 20252;

-- 3
-- Use a query to find the names and emails associated with accounts using 'Art Vandelay' as their full name or 'der' as their middle name.
SELECT full_name, email
FROM transaction_data
WHERE full_name = 'Art Vandelay'
  OR full_name LIKE '% der %';

- 4
-- Find the ip_addresses and emails beginning with "10.".
SELECT ip_address, email
FROM transaction_data
WHERE ip_address LIKE '10.%';

-- 5
-- Find the emails in transaction_data with ‘temp_email.com’ as a domain.
SELECT email
FROM transaction_data
WHERE email LIKE '%temp_email.com';

-- 6
-- The finance department is looking for a specific transaction. 
-- They know that the transaction occurred from an ip address starting with ‘120.’ and their full name starts with ‘John’.
-- Can you find the transaction?
SELECT *
FROM transaction_data
WHERE ip_address LIKE '120.%'
  AND full_name LIKE 'John%';

-- 7
-- Challenge
-- Return only those customers residing in GA. Use the list of ZIP CODE prefixes (https://en.wikipedia.org/wiki/List_of_ZIP_Code_prefixes) to determine 
-- the best query for zip codes belonging to Georgia(GA).
SELECT full_name, zip
FROM transaction_data
WHERE zip BETWEEN 30000 AND 31999;