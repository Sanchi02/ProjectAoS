import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

train_data = pd.read_csv("sample.csv")
y = train_data.LinkWeight
X = train_data.loc[:, train_data.columns != 'LinkWeight']
X['DayOfTheWeek'] = X['DayOfTheWeek'].map({'Monday':2,'Tuesday':2,'Wednesday':2,'Thrusday':2, 'Friday':2, 'Saturday':1, 'Sunday':1 })
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(X,y)
for tmp in range(5):
    stringy = "TestSnapshotForWeek" + str(tmp) + ".csv"
    test_data_ori = pd.read_csv(stringy)
    test_data = pd.read_csv(stringy)
    test_data['DayOfTheWeek'] = test_data['DayOfTheWeek'].map({'Monday':2,'Tuesday':2,'Wednesday':2,'Thrusday':2, 'Friday':2, 'Saturday':1, 'Sunday':1 })
    # train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
    # rf_model.fit(train_X, train_y)
    # rf_val_predictions = rf_model.predict(val_X)
    # rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

    # print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))
    predictions = rf_model.predict(test_data)

    weights = pd.DataFrame({'ID': test_data.ID, 'Weight': predictions})
    output = pd.merge(test_data_ori, weights,left_on='ID', right_on='ID')
    stringy2 = "SnapshotForWeek" + str(tmp) + "Output.csv"
    output.to_csv(stringy2, index=True)