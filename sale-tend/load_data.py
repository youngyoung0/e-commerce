import pandas as pd

def read_ecommerce_date(file_path):
    try:
        df = pd.read_csv(file_path, encoding='unicode_escape')
        print(f"데이터 로드 완료 :  {df.shape[0]}행 {df.shape[1]}열")
        return df
    except Exception as e:
        print(f"데이터 로드 중 오류 발생 : {e}")
        return None

def explore_data(df):
    print("데이터 탐색 :::")
    print(df.describe())
    print("컬럼별 결측치 개수 :::")
    print(df.isnull().sum())
    print("데이터프레임 (행의 수, 열의 수)")
    print(df.shape)