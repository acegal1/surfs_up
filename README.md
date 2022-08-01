# Surfs Up


# The purpose of this analysis

The purpose of this project was to collect data for a potential investment in a surf shop in Oahu, Hawaii.

   1. Explain the structures, interactions, and types of data of a provided dataset.
   2. Differentiate between SQLite and PostgreSQL databases.
   3. Use SQLAlchemy to connect to and query a SQLite database.
   4. Use statistics like minimum, maximum, and average to analyze data.
   5. Design a Flask application using data

# Overview
The business concept is a combination surf and ice cream shop and the potenetial investor wanted to know weather and precipitation data throughout the year on the island. For the challenge, the data was parsed from a SQLite file and analyzed for the months of June and December.

# Results
The weather in Oaho is pretty stable year round as per shown by the basic statistics complied for the two months that were compared: June (F°) December (F°) in Hawaii


![june_temp](https://github.com/acegal1/surfs_up/blob/main/images/june_temp.png)  ![dec_temp](https://github.com/acegal1/surfs_up/blob/main/images/dec_temp.png)


- Looking at either the averages or even the max temps above: Avgs: -June: 74.9° F -December: 71.0° F Max Temp: -June: 85.0° F -December: 83.0° F

- Also the max temps aren't excessive either, otherwise the heat would be a problem if it were consistently in the 90-100° F range.

- There is a difference in our basic stats in June (winter) where the minimum temperature is 64.0° F, almost 10°s more than the minimmum temp recorded in December at 56° F.

I created histograms for both the June and December results in order to provide a more user friendly statistical analysis. 

#### June Month Histograms

- June had 1700 counts of data with an average temperature of 75 degrees Farenheit.
- The minimum temperature was 65 degrees and the maximum was 85 degrees.


![june_temp_hist layout](https://github.com/acegal1/surfs_up/blob/main/images/june_temp_hist.png)


#### December Month Histograms

- December had just over 1500 counts of data with an average temperature of 71 degrees Farenheit.
- The minimum temperature was 56 dgrees and the maximum was 83 degrees.

![dec_temp_hist layout](https://github.com/acegal1/surfs_up/blob/main/images/dec_temp_hist.png)


Also, June and December histograms show that there are not many rainy days or "precipitation" for Oahu.
![june_prcp](https://github.com/acegal1/surfs_up/blob/main/images/june_prcp.png)  ![dec_prcp](https://github.com/acegal1/surfs_up/blob/main/images/dec_prcp.png)

# Summary
Oahu is the perfect place to surf. Supported by analyzing precipitation levels for the two months that were compared. The results showed that weather in Oahu is fairly stable year round with temperatures ranging from roughly 56 to 85 degrees Farenheit from June to December. 

It's clear from the analysis that Oahu is a great location for the new surf shop. The analysis helped with the decision-making.