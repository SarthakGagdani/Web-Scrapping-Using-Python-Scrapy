# Web-Scrapping-Using-Python-Scrapy
Scraped important data from all links: https://www.kupujemprodajem.com/238122-1-tseller-rpositive-ocene.htm Where: 
{238122} is changing from 0 to 1000000.
{1} is changing depending on number of reviews
{tseller} can be tseller or tbuyer
{rpositive} can be rpositive or rnegative

Note: all combinations of tseller / tbuyer, rpositive / rnegative need to be visited.

# Data scraped is following:

Database fields:
1.	review_id - review_id consists of user_id + dot + review_num. Examples: 93117.1, 93117.2, 93117.3
	- review_num is total count of reviews for that user. It should be incremented with each review. But restarted to 1 when new user page is visited.
2.	user_id - number from link
3.	page - pagination page on which review is
4.	reviewed - username that coresponds to user_id
5.	reviewer - username of person writing the review
6.	item  - title of item sold and reviewed
7.	comment - comment left by reviewer
8.	date - date of comment left, in format shown in picture ( Example. 2017-06-16 )
9.	positive - 1 or 0 depending if its positive or negative
10.	negative - 1 or 0 depending if its positive or negative
11.	buyer - 1 or 0 depending if reviewer is buyer or a seller
12.	seller - 1 or 0 depending if reviewer is a buyer or a seller
13.	review_num - coresponds to review_num mentioned above. Review count for that user.

# Note
It takes lot of time to scrape so many URL's so try out for limited combinations only!

