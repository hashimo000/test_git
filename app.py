import pandas as pd  # まずはpandasモジュールを準備する．
from sklearn.linear_model import LinearRegression
import streamlit as st
# csvファイルからデータ読み込み
df = pd.read_csv("http://logopt.com/data/Advertising.csv", index_col=0) #0行目をインデックスにする
df.tail()
y = df["Sales"]
X = df[["TV", "Radio", "Newspaper"]]  # df.drop("Sales",axis=1) でも同じ
X.head()

reg = LinearRegression()  # 線形回帰クラスのインスタンス reg を生成
reg.fit(X, y)             # fitによる訓練
yhat = reg.predict(X)     # predictによる予測
st.write("y-切片= ", reg.intercept_)
st.write("係数 = ", reg.coef_)
st.write(reg.score(X, y))  # 決定係数の別計算
