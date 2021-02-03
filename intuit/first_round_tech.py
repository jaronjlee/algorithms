"""
The people who buy ads on our network don't have enough data about how ads are working for their business. They've asked us to find out which ads produce the most purchases on their website.

Our client provided us with a list of user IDs of customers who bought something on a landing page after clicking one of their ads:

# Each user completed 1 purchase.
completed_purchase_user_ids = [
	"3123122444","234111110", "8321125440", "99911063"]

And our ops team provided us with some raw log data from our ad server showing every time a user clicked on one of our ads:

ad_clicks = [
	#"IP_Address,Time,Ad_Text",
	"122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
	"96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
	"122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
	"82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
	"92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
      "122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
	"92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

The client also sent over the IP addresses of all their users.

all_user_ips = [
	#"User_ID,IP_Address",
 	"2339985511,122.121.0.155",
	"234111110,122.121.0.1",
	"3123122444,92.130.6.145",
	"39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
	"8321125440,82.1.106.8",
	"99911063,92.130.6.144"
]

Write a function to parse this data, determine how many times each ad was clicked, then return the ad text, that ad's number of clicks, and how many of those ad clicks were from users who made a purchase.


Expected output:

1 of 2	 2017 Pet Mittens
0 of 1	 The Best Hollywood Coats
3 of 4	 Buy wool coats for your pets

purchases: number of purchase IDs
clicks: number of ad clicks
ips: number of IP addresses


"""

from collections import defaultdict


def parseAdData(completed_purchase_user_ids, ad_clicks, all_user_ips):
    purchasingCustomers = set()

    for id in completed_purchase_user_ids:
        purchasingCustomers.add(id)

    for IP, time, adText in ad_clicks:


def findContiguousHistory(history1, history2):
    dp = [[[] for x in range(len(history1) + 1)]
          for y in range(len(history2)+1)]
    longest = 0
    result = []

    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            url2 = history2[row-1]
            url1 = history1[col-1]
            upLeft = dp[row-1][col-1]
            if url2 == url1:
                # => [] + ["/start"] => ["/start"]
                dp[row][col] = upLeft + [url2]
                if len(dp[row][col]) > longest:
                    longest = len(dp[row][col])
                    result = dp[row][col]
    print(result)
    return result


#store result in a counter hash
#iterate through input array
#split each element by comma to get count and fulldomain
#convert count to int
#for full domain, iterate through each char until '.'
#once a '.' is reached, the subdomain is everything to the right of the '.'
#add subdomain to hash and increment count by the count


def countDomain(counts):
    result = defaultdict(int)

    for domain in counts:
        count, fullDomain = domain.split(",")
        count = int(count)
        result[fullDomain] += count

        for i in range(0, len(fullDomain)):
            if fullDomain[i] == '.':
                result[fullDomain[i+1:]] += count

    return result
