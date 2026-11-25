from sklearn.tree import DecisionTreeClassifier
x_train = [[15], [30], [50], [200], [5000], [10000]]
y_train = [0, 0, 0, 1, 1, 1]
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
hi = input("金额:")
prediction_1 = model.predict([[hi]])
if prediction_1 == 0:
    print("支出")
else:
    print("收入")
print("\n")