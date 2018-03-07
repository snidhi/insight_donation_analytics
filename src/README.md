Donation-analytics.py is the code to find contributions from repeated donors in that zipcode and year for a particular recipient.

Logic:

Keep two hashmaps. First hashmap "repeatedDonors" is to track the repeated donors.
A donor is repeated if the name and zipcode is the same. Keys in the map are: (name, zipcode)

If a key exists in the map, the donor is a repeated donor.

The second hashmap "recipientRecord" is to keep track of the transactions made by the repeated donors.

The transactions are gathered by recipient, zipcode and the year. So if same recipient,zipcode and year combination already exits in the map, modify the existing value.
Or add the values in the map.

When a donor is identified as a repeated donor, the earlier (first) entry for donor has to be added to recipient map. The first entry is looked up and added. It has to be added only once, so a boolian is added in the repeatedDonor map to check is the first entry has been seen or not. 

The dollor contributions are kept in a heap so that percentile calculation does not need sorting of the array each time. Other values in the hashmap are total sum of 
the dollar contribution and repetition count.

Once the above is known from a repeated donor, percentile, sum and repetetion count of the dollar amount is returned. 

