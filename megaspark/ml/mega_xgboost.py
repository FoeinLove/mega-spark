from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.sql.functions import col
from pyspark.ml.feature import StringIndexer, VectorAssembler
# from megaspark.ml.sparkxgb import XGBoostEstimator


class XGBoostClassifier:

    def __init__(self, feat_name, label_name, pred_name):

        # self.xgb = XGBoostEstimator(
        #     featuresCol=feat_name,
        #     labelCol=label_name,
        #     predictionCol=pred_name
        # )
        ...

    def fit(self, df):

        # In order to convert the nominal values into numeric
        # ones we need to define aTransformer for each column:
        sexIndexer = StringIndexer() \
            .setInputCol("Sex") \
            .setOutputCol("SexIndex") \
            .setHandleInvalid("keep")

        cabinIndexer = StringIndexer() \
            .setInputCol("Cabin") \
            .setOutputCol("CabinIndex") \
            .setHandleInvalid("keep")

        embarkedIndexer = StringIndexer() \
            .setInputCol("Embarked") \
            .setOutputCol("EmbarkedIndex") \
            .setHandleInvalid("keep")

        vectorAssembler = VectorAssembler() \
            .setInputCols(["Pclass", "SexIndex", "Age",
                           "SibSp", "Parch", "Fare",
                           "CabinIndex", "EmbarkedIndex"]) \
            .setOutputCol("features")

        pipeline = Pipeline().setStages([sexIndexer,
                                         cabinIndexer, embarkedIndexer,
                                         vectorAssembler, self.xgb])

        # get a new transformer
        self.model = pipeline.fit(df)

    def predict_proba(self, df):
        print("来到了预测环节")

        return self.model.transform(df)

