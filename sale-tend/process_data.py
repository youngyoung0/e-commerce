import pandas as pd

def preprocess_data(df):
    # 결속 처리
    df.dropna(inplace=True)
    print("결측치 제거후 데이터 shape ::: ", df.shape)

    # 중복 제거
    df.drop_duplicates(inplace=True)
    print("중복 제거 후 데이터 shape ::: ", df.shape)

    # CustomerID가 없는 행 제거
    df = df[pd.notnull(df['CustomerID'])]


    # Quantity UnitPrice가 0이하인 행 제거
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

    # InvoiceDate를 dateTiem 타입으로 변환
    df['invoiceDate']= pd.to_datetime(df['InvoiceDate'])

    # TotalPrice 칼럼 추가
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    return df