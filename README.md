# Tennis Prediction
The project set out with a straightforward yet challenging aim: to build an algorithm that could predict tennis match results. This task was more than just about predictions; it was a chance for me to get hands-on with the pandas library in Python, learn how to clean and handle data effectively, and dip my toes into the practical uses of machine learning. Through a process of trial and error and continuous improvement, the project evolved from a simple concept to a tool that could make sense of detailed data and provide a glimpse into the outcomes of tennis matches.

## Data Source Used
For Version 1, I built a simple scraper to collect data from the ATP website
For subsequent versions, I used the following dataset from Jeff Sackmann https://github.com/JeffSackmann/tennis_atp

## Project Skills
- Use of the pandas library for data manipulation.
- Techniques for cleaning and managing datasets.
- Application of machine learning for predictive modeling.


## Test Results Version 1
|   Year |   Matches Analysed |   Number Correct |   Number Incorrect |   Percentage Correct |
|-------:|-------------------:|--------------:|----------------:|---------------------:|
|   2020 |                370 |           442 |              98 |             0.818519 |
|   2020 |                370 |           392 |             143 |             0.732710 |
|   2020 |                370 |           392 |             143 |             0.732710 |
|   2020 |                370 |           442 |              98 |             0.818519 |
|   2020 |                364 |           218 |              30 |             0.879032 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           205 |              23 |             0.899123 |
|   2020 |                364 |           205 |              23 |             0.899123 |
|   2020 |                364 |           205 |               0 |             1.000000 |
|   2020 |                364 |           218 |               0 |             1.000000 |
|   2020 |                364 |           218 |               0 |             1.000000 |
|   2020 |                364 |           218 |               0 |             1.000000 |
|   2020 |                364 |           218 |               0 |             1.000000 |
|   2020 |                364 |           218 |              95 |             0.696486 |
|   2020 |                364 |           218 |              30 |             0.879032 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           205 |              23 |             0.899123 |
|   2020 |                364 |           205 |              23 |             0.899123 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           164 |              18 |             0.901099 |
|   2020 |                364 |           218 |              30 |             0.879032 |
|   2020 |                364 |           164 |              18 |             0.901099 |

![image](https://github.com/SurvivingJ/TennisPrediction/assets/68141758/ba5f5ceb-7b53-40af-88cb-8138ca439b30)

The scatter plot and the correlation matrix reveal a negative correlation (−0.680) between the total number of bets (our proxy for restrictiveness) and the accuracy (percentage correct) of the model. This suggests that as the model becomes less restrictive (placing more bets), its accuracy tends to decrease. After completing Version 4, I believe that there was significant overfitting in this version
of the tennis prediction algorithm that led to unusually high accuracy. 
The model scored players by assigning weights to 50 data points, predicting the winner with the highest score. Different tests adjusted these weights and set confidence thresholds to enhance prediction reliability, steering clear of matches with minimal score differences.
The improvement in testing methodology in later versions was partly due to the fact that in Version 1, I built a webscraper to collect the data, however for later versions I found comprehensive datasets
dating back to 1968.

## Test Results Version 2
Version 2 was a playground for testing machine learning techniques and had a few fatal errors that led me to skip to a new version, thus the
test results in this version were invalid. 

## Test Results Version 3
| Test Title                                  | Total Matches | Matches Correct | Matches Simulated | Accuracy (%)       |
|---------------------------------------------|---------------|-----------------|-------------------|--------------------|
| Model Initial Test                          | -             | 257             | 1370              | 18.76              |
| Accuracy V1 Initial                         | -             | 867             | 1370              | 63.28              |
| Boundary: 2                                 | -             | 142             | 245               | 57.96              |
| Boundary: 1.5                               | -             | 970             | 1462              | 66.35              |
| No Boundary Specified                       | -             | 996             | 1462              | 68.13              |
| NEW MODEL Boundary: 1                       | -             | 309             | 1462              | 21.14              |
| Accuracy V1 for NEW MODEL Boundary: 1       | -             | 921             | 1462              | 63.00              |
| NEW MODEL Boundary: 1, Diff > 1.5           | -             | 331             | 1078              | 30.71              |
| Accuracy V1 for NEW MODEL Boundary: 1, Diff > 1.5 | -       | 755             | 1078              | 70.04              |
| NEW MODEL Boundary: 1.5, Diff > 2.5         | -             | 337             | 740               | 45.54              |
| Accuracy V1 for NEW MODEL Boundary: 1.5, Diff > 2.5 | -     | 539             | 740               | 72.84              |
| NEW MODEL Boundary: 1.75, Diff > 2.5        | -             | 340             | 738               | 46.07              |
| Accuracy V1 for NEW MODEL Boundary: 1.75, Diff > 2.5 | -   | 543             | 738               | 73.58              |
| NEW MODEL Boundary:1.75, Diff > 3           | -             | 344             | 701               | 49.07              |
| Accuracy V1 for NEW MODEL Boundary:1.75, Diff > 3 | -       | 528             | 701               | 75.32              |
| Mega Random Forest Model No checks          | 1462          | 968             | 1462              | 66.21              |
| Mega Random Forest If not both 0 or 1       | 1462          | 968             | 1457              | 66.44              |

## Test Results Version 4
| Test Title                                                               | Total Matches | Matches Correct | Matches Simulated | Accuracy (%)       |
|--------------------------------------------------------------------------|---------------|-----------------|-------------------|--------------------|
| Logistic Regression Test #1: Min. 10 matches, 2020 games                 | 1462          | 401             | 1178              | 34.04              |
| Logistic Regression Test #2: Min. 20 matches, 2020 games                 | 1462          | 355             | 1018              | 34.87              |
| Logistic Regression Test #3: Exclude even, Min. 20 matches, 2020 games   | 1462          | 355             | 1016              | 34.94              |
| Logistic Regression Test #4: Exclude even, Min. 50 matches, 2020 games   | 1462          | 237             | 700               | 33.86              |
| Logistic Regression Test #5: Exclude even, Min. 100 matches, 2020 games  | 1462          | 159             | 497               | 31.99              |
| Logistic Regression Test #6: Exclude even, Min. 200 matches, 2020 games  | 1462          | 77              | 244               | 31.56              |
| Logistic Regression Test #7: Exclude even, Min. 300 matches, 2020 games  | 1462          | 30              | 108               | 27.78              |
| Random Forest Test #8: Exclude even, Min. 20 matches, 2020 games         | 1462          | 316             | 919               | 34.39              |
| Random Forest Test #9: Exclude even, Min. 100 matches, 2020 games        | 1462          | 159             | 499               | 31.86              |
| Mega Random Forest Overall                                               | 1462          | 968             | 1457              | 66.44              |
| Mega Random Forest >0.6 Threshold                                        | 1462          | 554             | 801               | 69.16              |
| Mega Random Forest >0.65 Threshold                                       | 1462          | 13              | 23                | 56.52              |
| Mega Random Forest >0.62 Threshold                                       | 1462          | 305             | 468               | 65.17              |

## Differences between Version 3 and 4
The transition from Version 3 to Version 4 of our predictive algorithm represents a fundamental shift in our modeling approach. In Version 3, the methodology entailed the development of two separate models: one for determining individual player scores and another for calculating match scores. The latter model was particularly innovative, as it derived its predictions from the differential analysis of the competing players' scores.

Version 4 introduced a more tailored approach. Instead of a universal model for player scores, it trained distinct models for each player, using the full extent of their match history as input data. This approach was meticulous—every match a player engaged in became a unique data point for their personalized model. Consequently, a player with a history of 10 matches would have a model trained exclusively on those encounters.

Despite the ingenuity of this individualistic approach, testing revealed a critical drawback. Players with fewer matches provided a limited dataset, which in turn constrained the model's learning potential and the richness of its predictive insights. This scarcity of data points led to a discernible decline in the models' effectiveness, as evidenced by a comparative analysis with the previous version. The findings underscore the importance of a substantial data foundation to capture the complexities of player performance and the dynamic nature of the sport.
