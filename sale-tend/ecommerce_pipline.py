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

def explore_data(df):
    print("데이터 탐색 : ")
    print(df.describe()) # 데이터의 기본 통계 정보를 출력
    print("컬럼별 결측치 개수 : ")
    print(df.isnull().sum()) # 각
    print(df.nunique())

def preprocess_data(df):
    # 결측치 처리
    df.dropna(inplace=True)
    print("결측치 제거후 데이터 shape:", df.shape)

    # 중복제거
    df.drop_duplicates(inplace=True)
    print("중복 제거 후 데이터 shape", df.shape)

    # CustomerID가 없는 행 제거
    df = df[pd.notnull(df['CustomerID'])]
    print("CustomerID가 없는 행 제거후 데이터 shape : ", df.shape)

    # Quantity와 UnitPrice가 0이하인 행 제거
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    print("Quantity 와 UnitPrice 검증 후 데이터 shape : ", df.shape)

    # InvoiceDate를 datetime 타입으로 변환
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # TotlaPrice 컬럼 추가
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    return df

def main():
    print("전자상거래 데이터 분석 파이프라인을 시작합니다.")

    # 데이터 로드
    data = load_data('./data/data.csv')
    if data is not None:
        # 데이터 탐색
        explore_data(data)

        # 데이터 전처리
        cleaned_date = preprocess_data(data)
        print("전처리 후 데이터 미리보기 : ")
        print(cleaned_date.head())
        print("전처리 후 데이터 데이터 정보 : ")
        print(cleaned_date.info)

    else:
        print("데이터 로드 실패. 프로그램을 종료합니다.")

if __name__ == "__main__":
    main()

