import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding='unicode_escape')
        print(f"데이터 로드 완료 :  {df.shape[0]}행 {df.shape[1]}열")
        return df
    except Exception as e:
        print(f"데이터 로드 중 오류 발생 : {e}")
        return None

def main():
    print("전자상거래 데이터 분석 파이프라인을 시작합니다.")

    # 데이터 로드
    data = load_data('./data/data.csv')
    if data is not None:
        print(data.head())
        print(data.info())
    else:
        print("데이터 로드 실패. 프로그램을 종료합니다.")

if __name__ == "__main__":
    main()

