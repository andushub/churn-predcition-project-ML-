# 데이터 샘플링을 위한 모듈 입니다
print('필요한 Library 불러오는 중')
print('------Loading------')
import pyspark
from pyspark import SparkConf
from pyspark.sql import SparkSession
myconf = SparkConf()
spark = pyspark.sql.SparkSession.builder.getOrCreate()

id_url = r'C:\Users\82103\Documents\ds_study\datas\Churn_Prediction\sampling_data\id_sampling.csv' 
train_member_url = r'C:\Users\82103\Documents\ds_study\datas\Churn_Prediction\sampling_data\train_sampling.csv' 
transaction_v1_url = r'C:\Users\82103\Documents\ds_study\datas\Churn_Prediction\sampling_data\transaction_sampling.csv' 
transaction_v2_url = r'C:\Users\82103\Documents\ds_study\datas\Churn_Prediction\sampling_data\transaction_sampling.csv' 
user_logs_v1_url = r'C:\Users\82103\Documents\ds_study\datas\Churn_Prediction\sampling_data\user_logs_v1_sampling.csv' 
user_logs_v2_url = r'C:\Users\82103\Documents\ds_study\datas\Churn_Prediction\sampling_data\user_logs_v2_sampling.csv' 

print('------ Loading End ------')
print('데이터 불러오는 중')
print('------ Loading ------')
id_spark = spark.read.csv(id_url, header=True, inferSchema=True)
member_train_spark = spark.read.csv(train_member_url, header=True, inferSchema=True)
transaction_v1_spark = spark.read.csv(transaction_v1_url, header=True, inferSchema=True)
transaction_v2_spark = spark.read.csv(transaction_v2_url, header=True, inferSchema=True)
user_logs_v1_spark = spark.read.csv(user_logs_v1_url, header=True, inferSchema=True)
user_logs_v2_spark = spark.read.csv(user_logs_v2_url, header=True, inferSchema=True)
print('------ Loading End ------')
def inputSQL():
    member_train_spark.createOrReplaceTempView("train") 
    print('쿼리문은 train_member 데이터프레임과 연결되어있습니다.')
    print('예시 : SELECT * FROM train ORDER BY rand() LIMIT 15000')
    
    sql = input('SQL 구문을 입력해주세요 : ')
    print('------Extracting And Exporting Data------')
    sampling = spark.sql(sql)
    sampling_df = sampling.toPandas()
    sampling_df.to_csv('member_train_sampling.parquet',index=False) 
    print('------Train Sampling End------')
    print()
    print("------'msno' And 'id' Match------")
    print('------Extracting And Exporting Data------')
    id_sampling = sampling.join(id_spark, on='id', how='inner').select('id','msno')
    id_sampling_df = id_sampling.toPandas().to_parquet()
    id_sampling_df.to_csv('id_sampling.csv',index=False)   
    print('------Match End------')

    print("------Transaction Data------")
    transaction_inner = transaction_v1_spark.join(id_sampling.select('id'), on='id', how='inner')
    transaction_inner_df = transaction_inner.toPandas()
    transaction_inner_df.to_csv('transaction_v1_sampling.parquet',index=False) 
    print("------Transaction_v1 End------")
    print()
    transaction_inner2 = transaction_v2_spark.join(id_sampling.select('id'), on='id', how='inner')
    transaction_inner2_df = transaction_inner2.toPandas().to_parquet()
    transaction_inner2_df.to_csv('transaction_v2_sampling.parquet',index=False) 
    print("------Transaction_v2 End------")
    print('------Transaction End------')
    print()
    print("------user_log Data------")
    user_logs_1 = id_sampling.join(user_logs_v1_spark, on='msno', how='inner').drop('msno')
    user_logs_1_df = user_logs_1.toPandas().to_parquet()
    user_logs_1_df.to_csv('user_log_v1_sampling.parquet',index=False) 
    print("------user_log_v1 End------")
    user_logs_2 = id_sampling.join(user_logs_v2_spark, on='msno', how='inner').drop('msno')
    user_logs_2_df = user_logs_1.toPandas().to_parquet()
    user_logs_2_df.to_csv('user_log_v2_sampling.parquet',index=False) 
    print("------user_log_v2 End------")
    print("------END------")