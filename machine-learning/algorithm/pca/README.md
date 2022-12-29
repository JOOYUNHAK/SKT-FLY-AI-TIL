# Machine Learning Algorithm
## PCA (주성분 분석)
#### 차원이 증가하면 정보의 밀도가 감소하고 정보의 감소로 과적합 문제가 발생하는데 이를 **차원의 저주**라고 한다.  
이를 해결할 수 있는 방법 중 하나로 데이터셋의 차원을 축소해 새로운 차원의 데이터로 만들어 처리해 주는 **차원축소**가 있고, 그 중 `PCA`는 **차원축소** 알고리즘의 한 종류
+ 단점
    - 데이터 분포에 선형성이 없다면 적용 불가
    - 데이터의 클래스를 고려하지 않기 때문에 최대 분산 방향이 특징 구분을 좋게 한다고 보장 못함

## Iris 데이터를 이용한 PCA
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import myutils as my
from sklearn import datasets

iris = datasets.load_iris()
df = pd.DataFrame(
    iris.data,
    columns = iris.feature_names
)
df['target'] = iris.target
```
```python
# 테스트 셋 분리
from sklearn.model_selection import train_test_split

# stratify는 test 비율 한 쪽으로 쏠리는 것을 방지
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size = 0.2,
    stratify = y,
    random_state = 2022
)
```
```python
# 표준화
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_train[:5]
```
```python
# 차원축소
from sklearn.decomposition import PCA

pca = PCA(n_components = 2)
x_train = pca.fit_transform(x_train)

x_train[:5]
```
```python
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators = 5, max_depth = 5)
clf.fit(x_train, y_train)
```
```python
x_test = scaler.transform(x_test)
x_test = pca.transform(x_test)
y_test = y.values
y_pred = clf.predict(x_test)
```
```python
my.print_score(y_test, y_pred, 'macro')
```