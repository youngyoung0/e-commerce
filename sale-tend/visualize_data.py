import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def visualize_chart(df):
    print("데이터 시각화 :::")

    # 국가별 매출 막대 그래프
    plt.figure(figsize=(12,6))
    country_revenue = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)
    country_revenue.plot(kind='bar')
    plt.title('Top 10 Countries by Revenue')
    plt.xlabel('Country')
    plt.ylabel('Revenue')
    plt.tight_layout()
    plt.show()


    # 월별 매출 추이 그래프
    plt.figure(figsize=(12,9))
    monthly_revenue = df.groupby('Month')['TotalPrice'].sum()
    monthly_revenue.plot(kind='line', marker = 'o')
    plt.title('Monthly Revenue Trend')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.tight_layout()
    plt.show()