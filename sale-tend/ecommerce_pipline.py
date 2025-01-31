import numpy as np
from load_data import read_ecommerce_date, explore_data
from process_data import preprocess_data, analyze_data
from visualize_data import visualize_chart


def main():
    print("전자상거래 데이터 분석 파이프라인을 시작합니다.")

    # 데이터 로드
    data = read_ecommerce_date('./data/data.csv')
    if data is not None:
        # 데이터 탐색
        explore_data(data)

        # 데이터 전처리
        cleaned_date = preprocess_data(data)

        analyzed_data = analyze_data(cleaned_date)

        visualize_chart(analyzed_data)

        # print("전처리 후 데이터 미리보기 : ")
        # print(cleaned_date.head())
        # print("전처리 후 데이터 데이터 정보 : ")
        # print(cleaned_date.info)

    else:
        print("데이터 로드 실패. 프로그램을 종료합니다.")

if __name__ == "__main__":
    main()

