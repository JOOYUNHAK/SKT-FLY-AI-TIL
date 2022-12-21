# Seaborn
## Seaborn이란
+ **matplotlib** 기반의 시각화 라이브러리
+ 그래픽을 그리기 위한 고급 인터페이스 제공
## figure-level과 axes-level
+ `figure-level`: matplotlib와 별개로 seaborn의 figure를 만들어서 plotting
    - figure-level 함수를 사용한 경우 facetgrid(seaborn의 figure)를 통해 레이아웃 변경
+ `axes-level`: axes 수준에서 plotting, plt.figure()와 같은 함수로 레이아웃 변경
## 막대그래프
+ 라이브러리 import: `import seaborn as sns` ( sns는 seaborn 모듈의 별칭 ) 
+ `countplot()`
    - 범주형 데이터를 입력하면, 항목별로 개수를 세어서 막대그래프 그려줌
    - matplotlib의 bar() 함수와는 다름
    <img src = "https://user-images.githubusercontent.com/99117410/208940335-37a6bbe8-7613-4f3f-a3ce-cb5133a821c3.png">
+ `barplot()`
    - y축으로 설정된 값의 평균을 막대의 높이로 표현
    - estimator 인수: y축에 표시될 값을 계산하는 방법 지정
    - hue 인수: hue의 종류별로 분리해서 그래프를 그림
    <img src = "https://user-images.githubusercontent.com/99117410/208940190-e52e0fad-b34b-46d8-8f4e-3ae46e629a4d.png">
## 히스토그램 
+ 데이터의 분포를 시각화
+ 연속형 데이터를 일정한 범위의 구간으로 나누고, 각 구간에 포함된 값의 개수 표시
+ **histplot()** 함수로 히스토그램을 그릴 수 있음
    - `bins` 인수: 구간의 개수 지정
    - `kde` 인수: 데이터의 분포를 확인할 수 있는 라인을 그림
    <img src = "https://user-images.githubusercontent.com/99117410/208942120-dba7e7ed-ea92-4905-affc-8557cd7bdbd0.png">
+ **displot()** 함수로도 히스토그램을 그리지만, displot()이 더 많은 기능 제공
    - `col` 인수: col 인수를 사용해서 여러 개의 그래프를 동시에 그리는 것이 가능
    <img src = "https://user-images.githubusercontent.com/99117410/208942810-effd7202-782a-4b2b-ad11-8477b2c28cfe.png">
## 박스플롯
+ 사분위수를 표현하는 그래프
+ 데이터의 분포와 특이치 확인 가능
+ 그룹별 박스플롯
    - x축에 범주형 데이터를 설정하면, 그룹별로 박스플롯을 그림
    <img src = "https://user-images.githubusercontent.com/99117410/208943356-25a096bf-8e66-4cf5-8cc7-db6f53a5fd84.png">
## 바이올린플롯
+ 박스플롯과 비슷한 정보를 표현하지만, 그래픅의 폭의 넓이로 데이터의 분포를 확인 가능
+ `hue` 인수: 그룹을 묶어서 표시
    <img src = "https://user-images.githubusercontent.com/99117410/208944038-9b5d3ac6-eb72-46c7-b0a2-4b7dbfed5760.png">
## 히트맵
+ 2차원 행렬 데이터를 색상과 숫자로 표현
+ `annot` 인수: 각 셀의 값을 나타냄
+ `cmap` 인수: 컬러맵 설정
    <img src = "https://user-images.githubusercontent.com/99117410/208944833-5978b33a-977a-49f3-8462-13f90ff0352c.png">
    <img src = "https://user-images.githubusercontent.com/99117410/208945068-ffaf988c-8bfb-4447-b14b-4fea2e5fb4a6.png">
    <img src = "https://user-images.githubusercontent.com/99117410/208946082-d1f476ad-307a-44e0-a49d-001e784337d0.png">

## 패싯그리드(FacetGrid)
+ `cos` 인수와 `row` 인수를 설정하여 하나의 그림에 그룹별로 여러 개의 그래프를 그림
    <img src = "https://user-images.githubusercontent.com/99117410/208947065-44e3d604-e155-409f-bfd1-84de96535755.png">
## 페어플롯
+ 그리드 형태로 각 컬럼의 조합에 대해 히스토그램과 분포도를 그림
+ 수치형 컬럼에 대해서만 그래프를 그림  
    <img src = "https://user-images.githubusercontent.com/99117410/208948137-5e997815-a428-423c-a544-6ee3cda067ec.png">
    <img src = "https://user-images.githubusercontent.com/99117410/208948300-0bc1d725-051e-4a28-b192-d7e9f01b3501.png">

