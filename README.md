# Tennis Prediction
The project set out with a straightforward yet challenging aim: to build an algorithm that could predict tennis match results. This task was more than just about predictions; it was a chance for me to get hands-on with the pandas library in Python, learn how to clean and handle data effectively, and dip my toes into the practical uses of machine learning. Through a process of trial and error and continuous improvement, the project evolved from a simple concept to a tool that could make sense of detailed data and provide a glimpse into the outcomes of tennis matches.

## Project Skills
- Use of the pandas library for data manipulation.
- Techniques for cleaning and managing datasets.
- Application of machine learning for predictive modeling.


## Test Results Version 1
## Test Results Version 2
## Test Results Version 3
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
