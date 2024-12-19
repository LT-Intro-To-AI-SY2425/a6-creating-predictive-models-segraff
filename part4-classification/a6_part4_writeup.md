# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

The model is not very accurate when I re-run my test without the StandardScaler because the components have vastly different scales, so the model focusses more on the feauture with the larger numerical range, which skews the data. The "EstimatedSalary" component has much higher values, which results in the model giving this feature too much importance over other features like age. 

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

The model with StandardScaler is 90% accurate. This model is accurate enough for deciding the gender of SUV buyers because it guessed correctly 45 out of 50 of the times. Since this situation is not a life or death scenario, a little inaccuracy is fine. However if the model was only 90% effective for predicting the correct dosage of a potentially fatal medication it would not be accurate enough. 

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

The model was overall accurate. I noticed that most of the errors were from the middle age range. 

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

According to the model, she would not buy an SUV. 