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
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # TotalPrice 칼럼 추가
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    return df

def analyze_data(df):
    print("데이터 분석 시작 :::")

    # 총 매출 계산
    total_revenue = df['TotalPrice'].sum()
    print("총 매출 :::", total_revenue)

    # 국가별 매출 분석
    country_revenue = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)
    print("상위 5개 국가별 매출 :::", country_revenue.head(5))

    # 월별 매출 추이
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly_revenue = df.groupby('Month')['TotalPrice'].sum()
    print("월별 매출 추이 ::: ")
    print(monthly_revenue)

    # 상위 판매 제품
    top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False)
    print("상위 판매 제품 5개 ::: ")
    print(top_products.head(5))

    # 고객 분석
    customer_count = df.groupby('CustomerID')['InvoiceNo'].nunique().sort_values(ascending=False)
    print("구매 횟수 기준 상위 5명의 고객 ::: ", customer_count.head(5))

    # 같은 물건을 가장 많이 산사람
    # 고객별, 상품별로 구매 횟수를 계산
    repeat_purchases = df.groupby(['CustomerID', 'StockCode', 'Description'])['InvoiceNo'].nunique().reset_index()
    repeat_purchases.columns = ['CustomerID', 'StockCode', 'Description', 'PurchaseCount']
    print("repeat_purchases ::: ", repeat_purchases.info)

    # 2번 이상 구매한 구매한 경우만 필터링
    repeat_purchases = repeat_purchases[repeat_purchases['PurchaseCount'] > 1].sort_values('PurchaseCount', ascending=False)

    # 상위 10개 겨로가 출력
    print(repeat_purchases.head(10))

    # 가장 많이 반복 구매된 상품 Top 5
    top_repeat_purchases = repeat_purchases.groupby('Description')['PurchaseCount'].sum().sort_values(ascending=False)
    print(top_repeat_purchases.head())
    # 가장 많은 상품을 반복 구매한 고객 Top 5

    return df

