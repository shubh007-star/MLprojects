import os
import sys  #to use ustom exception
from src.exception import CustomException  
from src.logger import logging  #to use logs
import pandas as pd  #because we have to work on dataframe

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig

# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer
@dataclass    #i am using a decorator which is dataclass this decorator is quite amazing because inside a class to define a class variable we need to use init varibalebut by using dataclass you will be able to directly define your clas variable 
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


# Note: if you are only defineing varibale inside the class then use dataclass on the other hand if you are defining function inside the class  also then use init


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv(r"E:\ML-project\src\Notebook\Data\stud.csv")   #i have to use r before address because compiler taking \d as regex operation due to that we have to use r 
            logging.info('Read the dataset as dataframe') 

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                #i am passing these 2 information becase these 2 itmes are required in the next step which is data_transformation
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()


