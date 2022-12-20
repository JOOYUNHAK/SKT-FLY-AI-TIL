# Pandas
## Pandas란
+ 데이터 조작 및 분석을 위한 파이썬 프로그래밍 라이브러리
+ 넘파이를 기반으로하며 처리 속도가 빠름

## 데이터구조
### Series 객체
+ 1차원 배열 구조를 가지며, 인덱스를 가짐
+ dtype 속성과 shape 속성 등을 가짐
### DataFrame
+ 2차원 배열 구조를 가지며, 인덱스를 가짐
+ 행과 열로 구성되고, 각 열을 이름을 가짐
+ 각 열은 각각의 데이터 타입을 가지며, Series 객체로 표현할 수 있음
+ dtype 속성과 shape 속성 등을 가짐

## Series 생성
+ pd.Series([1, 2, 3, 4 ], name = '이름명')
+ 인덱스 지정해서 생성 (지정하지 않을 경우 0부터 인덱스 시작)
    - pd.Series([1, 2, 3, 4], index = ['A', 'B', 'C', 'D'])

## DataFrame 생성
```python
# 일반 배열로 생성
x = [['Jackson', 68, True, 1.5, 'A'],
 ['Liam', 74, True, 1.1, 'A'], 
 ['Emma', 20, False, 0.89, 'C']] 
df = pd.DataFrame(x, 
 columns=['Name', 'Weight', "Option", 'Etc', 'Type'])

# 딕셔너리를 사용해서 생성
data = {
'Name':['Jackson', 'Emma', 'Noah', 'James'], 
'Wight':[68, 74, 77, 78], 
'Option':[True, True, False, False], 
'Rate':[0.21, 1.1, 0.89, 0.91],
'Type':['A','A','C','C']
}
df = pd.DataFrame(data)

# csv 파일을 읽어서 생성
df = pd.read_csv('파일상대경로.csv')
```

## DataFrame 정보 확인
+ DataFrame 속성
    - shape: 데이터의 행과 열의 수를 튜플 자료형으로 정의
    - dtypes: 각 열의 데이터 타입
    - columns: 컬럼명
    - index: 행의 인덱스
+ DataFrame 함수
    - head(): 데이터 프레임의 처음부터 설정한 개수만큼 표시
    - tail(): 데이터 프레임의 끝에서 설정한 개수만큼 표시
    - info(): 데이터 프레임의 정보를 표시
    - describe(): 각 열의 통계 정보를 표시

## 결측치
데이터가 없다는 것을 다른 기호로 표시해 놓은 값
+ isna(), isnull(): 결측치인지 아닌지를 True, False로 표현 
+ dropna(): 결측치가 포함된 행을 삭제
+ fillna(): 결측치를 특정 값으로 변경 ( 인자로 inplace값을 줄 수 있는데 inplace가 True면 원본을 변경 )

## 슬라이싱
특정 부분의 데이터들을 추출하는 것을 말함
+ ioc: ioc[슬라이싱 범위, 컬럼명]으로 사용되는데 컬럼명을 여러 개 지정하고 싶은 경우 배열로 줌, 슬라이싱 범위에 조건이 들어가는 것도 가능
+ iloc: ioc와 사용법이 비슷하지만 컬럼명을 직접 적는 대신 추출할 컬럼을 숫자로 지정
+ select_dtypes(include = ['데이터형']): 주어진 데이터형으로만 이루어진 컬럼을 추출, number일 경우 숫자 

## 컬럼다루기
+ df.rename(columns={'기존 컬럼명': '변경 후 컬럼명'})

## 파일 읽기
+ pd.read_csv('파일명', index_col = 0, na_values['null value로 판단할 문자 입력'])

## 통계데이터 연산
+ mean(): 평균값을 계산
+ var(): 분산 계산
+ count(): 전체의 개수
+ values_count(): 범주형 데이터의 종류별 데이터의 개수
+ unique(): 범주형 데이터 종류의 개수

## 그룹핑 함수
+ groupby(): 특정 컬럼의 값을 기준으로 그룹핑해서 함수를 실행
+ apply(): 데이터 프레임에 함수를 적용. 함수에 전달되는 객체는 Series 형식
+ map(): 단일 컬럼에서는 apply() 함수와 같은 기능이며, 다중 컬럼의 경우네는 map() 함수 사용 불가
``` python

df = pd.DataFrame({
'city': ['Busan', 'Busan', 'Busan', 'Busan',
 'Seoul', 'Seoul', 'Seoul'],
'fruits': ['Apple', 'Orange', 'Banana', 
 'Banana', 'Apple', 'Apple', 'Banana'],
'price': [100, 200, 250, 300, 150, 200, 400],
'quantity': [1, 2, 3, 4, 5, 6, 7]
})

z = df['city'].map(lambda x: 'SED' if x == 'Seoul' else 'BUS')
df['TAG'] = z
df['TAG'] = df['TAG'].map({'BUS': 0, 'SED': 1})
```
