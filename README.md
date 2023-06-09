# **프로젝트 소개**

### **# 주제**
- 음원 스트리밍 서비스 이탈 유저 예측

### **# 참여인원**
- 박무연, 박지호, 안태진, 천정은

### **# 기간**
- 23.04.03 ~ 23.04.19

### **# 프로젝트 설명**
- 매월 요금을 지불하는 구독 서비스에서 고객의 이탈은 수익의 감소로 연결
- 이탈 고객의 특징 찾고 예측할 수 있는 머신러닝 모델 구현

### **# 데이터**
- Kaggle WSDM - KKBox's Churn Predicition Challenge [(LINK)](https://www.kaggle.com/c/kkbox-churn-prediction-challenge)

### **# 파일설명**
- Sampling.py : 전체데이터를 spark 로 읽어와 SQL 구문으로 샘플링 후 .parquet 파일로 내보내는 모듈
- EDA.ipynb : EDA 진행 결과 주피터
- Preprocessing.py : 전처리 진행 모듈
  - EDA 진행결과를 바탕으로 변수를 전처리 및 파생변수 생성을 위해 Class로 작성

- Modeling.py : 학습 모델 모듈
  - 다양한 모델을 실험하기 위해 Class로 작성

- Final.ipynb : 모듈 호출 및 데이터 학습 주피터


### **# 모델 Flow**
![모델플로우](https://github.com/andushub/churn_prediction_ML/assets/99305268/15a26998-7e9a-4715-a240-4c7a6bb747bc)

### **프로젝트 상세 내용**
