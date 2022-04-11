Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#importing all the libraries that are required
import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
#reding the dat from URLlink
url = https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv
SyntaxError: invalid decimal literal
url = "https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv"
data1 = pl.read_csv(url)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    data1 = pl.read_csv(url)
AttributeError: module 'matplotlib.pyplot' has no attribute 'read_csv'
data1 = pd.read_csv (url)
print ("Data imported successfully")
Data imported successfully
data1.head(25)
    Hours  Scores
0     2.5      21
1     5.1      47
2     3.2      27
3     8.5      75
4     3.5      30
5     1.5      20
6     9.2      88
7     5.5      60
8     8.3      81
9     2.7      25
10    7.7      85
11    5.9      62
12    4.5      41
13    3.3      42
14    1.1      17
15    8.9      95
16    2.5      30
17    1.9      24
18    6.1      67
19    7.4      69
20    2.7      30
21    4.8      54
22    3.8      35
23    6.9      76
24    7.8      86
#plotting hours nd scores to determine a relationship
data1.plot (x= 'Hours', y= 'Scores'), style = 'o')
SyntaxError: unmatched ')'
data1.plot (x= 'Hours', y= 'Scores', style= 'o')
<AxesSubplot:xlabel='Hours'>
pl.title ('Hours Vs Scores')
Text(0.5, 1.0, 'Hours Vs Scores')
pl.xlabel ('Hours')
Text(0.5, 0, 'Hours')
pl.ylabel ('Scores')
Text(0, 0.5, 'Scores')
ml.show()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    ml.show()
NameError: name 'ml' is not defined. Did you mean: 'pl'?
pl.show()
#values of slope and intercept
#intercept
print("intercept:", regressor.intercept_)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print("intercept:", regressor.intercept_)
NameError: name 'regressor' is not defined
#positive relationship between hours and scores
#preparing data for regression
#dividing data into attributes and labels or input and output
x = datat1.iloc[:, :-1].values
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x = datat1.iloc[:, :-1].values
NameError: name 'datat1' is not defined. Did you mean: 'data1'?
x = data1.iloc[:, :-1].values
y = data1.iloc[:, 1].values
#splitting data into training and test sets using Scikit Learn's built-in train_test_split() method
from sklearn.model_selection import train_test_split
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    from sklearn.model_selection import train_test_split
ModuleNotFoundError: No module named 'sklearn'
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=0)
#training the algorithm for regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
LinearRegression()
print("Training Complete")
Training Complete
#plotting regression line
line = regressor.coef_*X+regressor.intercept_
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    line = regressor.coef_*X+regressor.intercept_
NameError: name 'X' is not defined. Did you mean: 'x'?
line = regressor.coef_*x+regressor.intercept_
#plotting test data
pl.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x00000222180C2770>
pl.plot(X, line);
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    pl.plot(X, line);
NameError: name 'X' is not defined. Did you mean: 'x'?
pl.plot(x, line);
[<matplotlib.lines.Line2D object at 0x00000222180C2D40>]
pl.show()
#values of slope and intercept
#slope
print("Slope:",regressor.coef_)
Slope: [9.91065648]
#intercept
print("Intercept:",regressor.intercept_)
Intercept: 2.0181600414346974
#prediction
#testing data in hours
print(x_test)
[[1.5]
 [3.2]
 [7.4]
 [2.5]
 [5.9]]
#predicting the scores
y_prd= regressor.predict(x_test)
#comparing actual values and predicted values
df= pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    df= pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
NameError: name 'y_pred' is not defined. Did you mean: 'y_prd'?
df= pd.DataFrame({'Actual': y_test, 'Predicted': y_prd})
df
   Actual  Predicted
0      20  16.884145
1      27  33.732261
2      69  75.357018
3      30  26.794801
4      62  60.491033
#importing Rsquare value
from sklearn.metrics import r2_score
#calculating rquare value
r_square = r2_score(y_test,y_prd)
print("Value of Rquare is", r_square)
Value of Rquare is 0.9454906892105355
#specific prediction
hours= x_test
hours.reshape(1,-1)
array([[1.5, 3.2, 7.4, 2.5, 5.9]])
predicted= regressor.predict(hours)
print('Predicted Value', predicted)
Predicted Value [16.88414476 33.73226078 75.357018   26.79480124 60.49103328]
hours= [[9.25]]
own_prd = regresor.predict(hours)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    own_prd = regresor.predict(hours)
NameError: name 'regresor' is not defined. Did you mean: 'regressor'?
own_prd = regressor.predict(hours)
print("Number of hours = {}".format(hours))
Number of hours = [[9.25]]
print("Predicted score = {}",format(own_prd[0]))
Predicted score = {} 93.69173248737535
