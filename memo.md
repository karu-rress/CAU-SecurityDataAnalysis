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


decision tree: if~else question이라 다른 language로 convert되기 매우 쉬움. SQL이라든지.
explainable AI중 하나의 방법임.

실제로 사용되는 feature은 일부. 여기도 자동적으로 feature selection이 이루어짐.

IG는 최종 계산 결과만.
그게 가장 큰 게 root node.

노드를 지나면 도착한 데이터들만 가지고 또 다시 IG를 다시 계산. 그리고 IG가 제일 큰 놈을 node로 결정.

지니 인덱스: 불순도


***

교수님: NLP, 시계열 하지 말기. NLP는 txt lib을 더 많이 알아야 함.
시계열은 과거를 가지고 현재, 미래를 맞추는 거. feature가 딱 하나만 있기도 함.

시계열 데이터 예측? random walk. 술 취한 사람이 걷는 걸 생각해보기.
주가를 예측하는 것... 그만큼 어려운 일.
시계열 데이터 예측도 다른 기법이 필요함.

아리마, 아로마 등등.
아리마.. 아리마?

아리마 카나? B코마치?
아 최애의 아이는 못ㅊ


데이터 언더스탠딩.
도메인.
컬럼을 늘리거나. 컬럼을 추가로.