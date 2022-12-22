# Machine Learning Algorithm
## 분류 알고리즘
+ K-최근접 이웃  
    과거의 데이터를 학습하고, 새로운 데이터에 대해서 가장 가까운 유사도를 가진 기준 데이터에 따라서 분류  
    >   유사도는 두 점 사이의 거리가 아닌, 두 데이터간의 유사성
      
    Y가 범주형일 떄 분류, Y가 연속형일 때 회귀

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

# mode가 'bin'일 경우 2진 분류 iris 데이터 이용
def get_iris(mode=None):
    # 파일 읽기
    iris = pd.read_csv('iris.csv')
    # 필요 없는 열 삭제 후 복사
    df = iris.drop(['Id'], axis = 1).copy()
    # 컬럼 이름 변경
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'P-petal_width', 'species']

    # 2진 분류인 경우
    if( mode == 'bin'):
        df = df.loc[df['species'] != 'Iris-virginica']
    
    # 인코딩
    df['species'] = df['species'].map({
        'Iris-setosa': 0,
        'Iris-versicolor': 1,
        'Iris-virginica': 2
    })

    # 마지막 열은 제외한 전체 행
    x = df.loc[:, : -1]
    # 마지막 열만 전체 행
    y = df.loc[:, -1]

    x, y  = sklearn.utils.shuffle(x, y)

    # 학습 데이터는 전체 데이터의 80%, 테스트 데이터는 20%
    num = int(len(y) * 0.8)

    x_train = x.iloc[:num, ]
    x_test = x.iloc[num: , ]
    y_train = y.iloc[:num, ]
    y_test = y.iloc[num: ,]

    # 스케일링
    for col in x_train.columns:
        mu = x_train[col].mean() # 평균
        std = x_train[col].std() # 표준편차
        x_train[col] = ( x_train[col] - mu ) / std
        x_test[col] = ( x_test[col] - mu ) / std
    return x_train, x_test, y_train, y_test
```
```python
x_train, x_test, y_train, y_test = get_iris('bin')
# 반환 값은 dataframe 형태이므로 numpy array로 변경
x_train = x_train.values
x_test = x_test.values
y_train = y_train.values
y_test = y_test.values
```
```python
# 학습
from sklearn.neighbors import KNeighborsClassifier

# 객체 만들기
clf = KNeighborsClassifier()
# 학습 시작, y 데이터는 정답용 데이터
clf.fit(x_train, y_train)
# 테스트
clf.score(x_test, y_teset)
# 새로운 값 예측
clf.predict(x_test)
```
```python
# 평가지표 metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score

# y_true는 정답 값, y_pred는 예측 값
def print_score(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    pre = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)

#호출
print_score(y_test, y_pred)
```
```python
#혼동행렬 (Confusion Matrix)
from sklearn.metrics import confusion_matrix

cfm = confusion_matrix(y_test, y_pred)

plt.figure(figsize = (5, 5))
sns.heatmap(cfm, annot = True, cbar = False)
plt.xlabel('predicted Class')
plt.ylabel('True Class')
plt.show()
```
<img src = "https://user-images.githubusercontent.com/99117410/209181049-1730efd5-03e5-49b5-8569-f5035037742f.png">

> Positive로 예측했는데 정답이 Positive인 경우와 Negative로 예측했는데 정답이 Negative인 경우만 존재하므로 100%의 정확성을 가진다.

### 다른데이터로 학습하기
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

fruit = pd.read_csv('citrus.csv')
df = fruit.copy()
df['name'] = df['name'].map({
    'grapefruit': 0,
    'orange': 1
})
# 열 분리
x = df.drop('name', axis = 1)
y = df['name']

# random으로 80%의 학습 데이터를 추출 shuffle과 비슷한 명령어
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2022)

# 표준화
scaler = StandardScaler()
scaler.fit(x_train)

x_train_s = scaler.transform(x_train)
y_train = y_train.values # Series 타입은 numpy array로 변경

# 학습
x_test_s = scaler.transform(x_test)
y_test = y_test.values

scores = []
for i in range(3, 30):
    clf = KNeighborsClassifier(n_neighbors=i)
    clf.fit(x_train_s, y_train)
    s = clf.score(x_train, y_train)
    score.appends(s)

# 이후 적절한 k 값을 대입 이후 최종 테스트
clf = KNeighborsClassifier(n_neighbors = 5)
```

