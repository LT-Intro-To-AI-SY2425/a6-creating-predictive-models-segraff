import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

print(x)
print(y)

scaler = StandardScaler().fit(x)

x=scaler.transform(x)

# Step 4: Split the data into training and testing data
x_train,x_test,y_train,y_test = train_test_split(x,y)
# Step 5: Fit the data
print("Accuracy:", model.score(x_test)):
x = x_test[index]
x = x.reshape(-1,3)
print(x)
y_pred = int(model.)
# Step 6: Create a LogsiticRegression object and fit the data

# Step 7: Print the score to see the accuracy of the model

# Step 8: Print out the actual ytest values and predicted y values
# based on the xtest data