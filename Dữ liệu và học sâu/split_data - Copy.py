import pandas as pd

df = pd.read_csv('titanic.csv')
train = df.sample(frac=0.8, random_state=42)
test  = df.drop(train.index).drop(columns=['Survived'])

train.to_csv('train.csv', index=False)
test.to_csv('test.csv', index=False)

print("Đã tạo train.csv và test.csv")