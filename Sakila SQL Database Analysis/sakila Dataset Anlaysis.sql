## Sakile Database Anaysis

# Revenue by different Store ID's

SELECT
	i.store_id as "Store ID", SUM(p.amount) as Revenue
FROM
	inventory i, payment p, rental r
WHERE
	p.rental_id = r.rental_id
	AND
	r.inventory_id = i.inventory_id
GROUP BY
	1
ORDER BY
	2 desc
;

# How many times each movie has been rented out

SELECT
	f.title, count(r.rental_id)
FROM
	film f, rental r, inventory i
WHERE
	f.film_id = i.film_id
	AND
	i.inventory_id = r.inventory_id
GROUP BY
	1
;


## Using Left, Min, Max functions
# How many rentals we had each month

SELECT
	left(r.rental_date,7), count(r.rental_id)
FROM
	rental r
GROUP BY
	1
ORDER BY
	2 desc
;
#OR
SELECT
	f.title as "Film Title", max(r.rental_date) as "Last rental date", min(r.rental_date) as "First rental date"
FROM
	rental r, inventory i, film f
WHERE
	r.inventory_id = i.inventory_id
	AND
	i.film_id = f.film_id
GROUP BY
	f.film_id
;

#  Every customer's last rental date

SELECT
	concat(c.first_name, " ",c.last_name) as "Name",c.email as Email, max(r.rental_date) as "Last Rental Date"
FROM
	rental r, customer c
WHERE
	r.customer_id = c.customer_id
GROUP BY
	c.customer_id
;

# Revenue by each month

SELECT
	left(r.rental_date,7) as "Month", sum(p.amount) as "Revenue"
FROM
	rental r, payment p
WHERE
	r.rental_id = p.rental_id
GROUP BY
	1
ORDER BY
	2 desc
;

## DISTINCT: How much percent of users account for how much percent of the revenue OR Unique purchases by an individual customer ID

# How many unique renters per month

SELECT
	left(r.rental_date,7) as Month, count(r.rental_id) as "Total count of rental",count(DISTINCT r.customer_id) as "Unique Renters", count(r.rental_id) / count(DISTINCT r.customer_id) as "Average no of Rentals per renter"
FROM
	rental r
GROUP BY
	1
;

# How many unique movies are rented out each month

SELECT
	left(r.rental_date,7) as Month, count(DISTINCT i.film_id) as "Number of Unique movies rented out each month"
FROM
	rental r, inventory i
WHERE
	r.inventory_id = i.inventory_id
GROUP BY
	1
;


## IN function
# Finding number of rentals in certain categories

SELECT
	c.name as Categgory, count(r.rental_id) as "Number of rentals"
FROM
	rental r, inventory i, film f, film_category fc, category c
WHERE
	r.inventory_id = i.inventory_id
	AND
	i.film_id = f.film_id
	AND
	f.film_id = fc.film_id
	AND
	fc.category_id = c.category_id
	AND
	c.name in ("Comedy", "Sports", "Family")
GROUP BY
	1
;

## Comparisons
# Users who have rented out at least 3 times

SELECT
	r.customer_id as customer, count(r.rental_id) as "Number of Rentals"
FROM
	rental r
GROUP BY
	1
HAVING
	count(r.rental_id) >= 3
;


## Revenue made by a single store on titles rated PG-13 and R

SELECT
	i.store_id as Store, f.rating as "Movie Rating", sum(p.amount) as Revenue
FROM
	film f, payment p, inventory i, rental r
WHERE
	p.rental_id = r.rental_id
	AND
	r.inventory_id = i.inventory_id
	AND
	i.film_id = f.film_id
	AND
	i.store_id = 1
	AND
	f.rating in ('R', 'PG-13')
GROUP BY
	1, 2
ORDER BY
	3
;