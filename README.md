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
![슬라이드1](https://github.com/andushub/churn_prediction_ML/assets/99305268/46774261-3b57-48d1-9479-7823fd2760ae)
![슬라이드2](https://github.com/andushub/churn_prediction_ML/assets/99305268/793f3cd5-4faa-4e25-99e5-684e59259c56)
![슬라이드3](https://github.com/andushub/churn_prediction_ML/assets/99305268/24d6d9c0-5e5e-4bc4-ad51-d5b0310a00a0)
![슬라이드4](https://github.com/andushub/churn_prediction_ML/assets/99305268/5ecbbd20-c55d-4542-a21b-9e2f9e802257)
![슬라이드5](https://github.com/andushub/churn_prediction_ML/assets/99305268/0e06e8df-28ed-4b35-a53f-cd7c3be7292a)
![슬라이드6](https://github.com/andushub/churn_prediction_ML/assets/99305268/cb1fc6b2-761e-4567-961d-7015a7bc63e5)
![슬라이드7](https://github.com/andushub/churn_prediction_ML/assets/99305268/1e6c461d-3de9-4a35-9f8e-99f3d461ba1d)
![슬라이드8](https://github.com/andushub/churn_prediction_ML/assets/99305268/1f486915-cdf8-46fb-a875-704aeb38ec79)
![슬라이드9](https://github.com/andushub/churn_prediction_ML/assets/99305268/caa1109e-8fab-49a0-9ec5-f536a0489b15)
![슬라이드10](https://github.com/andushub/churn_prediction_ML/assets/99305268/c34bec32-15cb-48c6-85b0-2150791bf6bc)
![슬라이드11](https://github.com/andushub/churn_prediction_ML/assets/99305268/04def8ac-cbc5-4179-86bb-0ef2788e9fdc)
![슬라이드12](https://github.com/andushub/churn_prediction_ML/assets/99305268/d6e62159-3cb7-4c4c-8473-1b763ba0214e)
![슬라이드13](https://github.com/andushub/churn_prediction_ML/assets/99305268/e45a4e6f-db59-4f97-bb9b-13c69a8a9ebc)
![슬라이드14](https://github.com/andushub/churn_prediction_ML/assets/99305268/5d0b7e87-f488-4ac5-aa4e-3470cd1403e8)
![슬라이드15](https://github.com/andushub/churn_prediction_ML/assets/99305268/2bbe01c2-39f5-4d6c-875a-1de32e2591ca)
![슬라이드16](https://github.com/andushub/churn_prediction_ML/assets/99305268/306066c0-1cd1-4e37-9a56-5c91cb61b97c)
![슬라이드17](https://github.com/andushub/churn_prediction_ML/assets/99305268/6fdfe989-6590-43bb-941c-b3142416fa8c)
![슬라이드18](https://github.com/andushub/churn_prediction_ML/assets/99305268/5c853d6d-90b1-4630-9625-04644ad8a2a1)
![슬라이드19](https://github.com/andushub/churn_prediction_ML/assets/99305268/3cf14b0b-0c42-4301-a2d2-9e89f96630ab)
![슬라이드20](https://github.com/andushub/churn_prediction_ML/assets/99305268/b140dba6-b413-4411-975d-f84860aac5ef)
![슬라이드21](https://github.com/andushub/churn_prediction_ML/assets/99305268/e1f980f0-041e-4dbf-908b-c516930476d2)
![슬라이드22](https://github.com/andushub/churn_prediction_ML/assets/99305268/4538f190-6c14-4c0e-a1c7-32ea52cee109)
![슬라이드23](https://github.com/andushub/churn_prediction_ML/assets/99305268/da37a6d3-8068-429e-9f78-21f4ecfe3476)
![슬라이드24](https://github.com/andushub/churn_prediction_ML/assets/99305268/a5501795-8c1a-40de-8257-5bd5aa888b5e)
![슬라이드25](https://github.com/andushub/churn_prediction_ML/assets/99305268/c56748b6-6233-4411-8d1b-25b2adaeb4fd)
![슬라이드26](https://github.com/andushub/churn_prediction_ML/assets/99305268/24d9e64f-b7ca-4123-a533-c18133563f63)
![슬라이드27](https://github.com/andushub/churn_prediction_ML/assets/99305268/5725ff4a-9f27-4952-b16b-5251879a973e)
![슬라이드28](https://github.com/andushub/churn_prediction_ML/assets/99305268/f161b79c-4ee4-40d6-b345-18216ce33766)
![슬라이드29](https://github.com/andushub/churn_prediction_ML/assets/99305268/0b2307e7-8641-42f9-a9d1-85de86eafae5)
![슬라이드30](https://github.com/andushub/churn_prediction_ML/assets/99305268/c1ff38ef-7089-45b0-91b7-9d251406c115)
