# EDA: Exploratory Data Analysis
(탐색적 데이터 분석)

- technical jobs
  - statiscis
  - visualization : 이 데이터는 ~ 특징이 있다. ~ 가설을 가지고, 이렇게 분석해보겠다.
  - 이런 특징을 가진 데이터에서 Fraud 데이터가 더 많이 나올 것 같다? 
  - 그럼 그쪽을 더 파고들어야겠다.
  - 마크다운을 많이 쓸 것.
- Data understanding
- Interpretation

이 데이터는 ~ 하다. ~ 하는 특징이 있다.

***

## Fraud Data Analysis
데이터가 어떤 특성을 가지고 있다면 Fraud 데이터일지.\
isFraud => 이거는 특별한 column임. 이게 타겟값이 됨. isFraud가 output 값이 되어야 함.

***

row = data point = case = example = sample
target = feature = variable

independent variable -> dependent variable 추론

타겟 변수가 값이 있다면 labled, 없다면 unlabeled
class.
0 -> non fraud
1 -> fraud
classification을 통해 class를 분류하자!
k-Neighbors



knn 과제 => TEXT를 int로 바꾸어서 돌릴 것.
apply() 함수 이용.


머신러닝 :: 지도학습, 비지도학습
- 지도학습 :: 분류, 회귀
  - 분류 = 범주형 자료 예측 :: 이진 분류(2개 클래스), 다중 분류(3+개 클래스)
  - 회귀 = 연속형 자료 예측

Lasso는 automatic feature selection이 될 수 있음.
- 만약 특정 feature가 제거됐다면, 왜 제거됐는지 생각해보자.


Threashold 를 직접 만들 수는 없음. 일일이 계산 후 배열로 만들어 이걸 test로 만듦.\
그레디언트 부스팅은 데이터가 크면.. 시간이 오래걸림(XGBOOST)\\=>  