# 판매 상품 세팅
Products = [
    {
        "상품명" : "무선 이어폰",
        "가격" : 89_000,
        "재고" : 3
},
    {
        "상품명" : "텀블러",
        "가격" : 15_000,
        "재고" : 10
    },
    {
        "상품명" : "보조배터리",
        "가격" : 32_000,
        "재고" : 5
    },
    {
        "상품명" : "마우스패드",
        "가격" : 9_000,
        "재고" : 0
    },
    {
        "상품명" : "USB 허브",
        "가격" : 18_000,
        "재고" : 4
    }
]

class ShoppingMall:
    # 공통 기능
    # 판매 타이틀
    def show_title():
        print("-"*40)
        print("1. 상품목록 2. 담기 3. 빼기 4. 장바구니 5. 쿠폰 6. 결제 q. 종료")
        print("-"*40)
        answer = input("선택 : ").strip()

        if answer in ("1", "2", "3", "4", "5", "6"):
            return int(answer)

        elif answer in ("q"):
            return answer

        print("제공된 보기 중에서 입력하세요.")

    # 1. 상품 목록
    def product_list(Products):
        for number, product in enumerate(Products, start=1):
            print(f"{number}. {product['상품명']}     {product['가격']:,}원  (재고 {product['재고']}개)")

    # 2. 담기
    def Put():
        product_number = input("상품 번호: ").strip()

        # 상품 목록 중에 선택지를 고른 경우
        if product_number in ("1", "2", "3", "4", "5"):
            usernumber = int(product_number)
            usernumber -= 1
            user_seleted = Products[usernumber]

        # 선택한 상품의 재고가 0(없는) 경우
        elif user_seleted['재고'] == 0:
            print(f"상품 번호: {product_number}")
            print("품절된 상품입니다.")

        # 선택한 상품의 재고가 있는 경우
        elif user_seleted['재고'] != 0:
            product_amount = input("수량: ").strip()
            product_amount = int(product_amount)

            if product_amount > user_seleted['재고']:
                print(f"수량: {user_seleted['재고']}")
                print(f"재고가 부족합니다. (담을 수 있는 수량: {user_seleted['재고']}개)")

            elif product_amount <= user_seleted['재고']:
                print(f"수량: {user_seleted['재고']}")
                print(f"{user_seleted['상품명']} {product_amount}개를 담았습니다.")
                # 잔여 재고 양 변경
                user_seleted['재고'] = user_seleted['재고'] - product_amount

        print("제공된 보기 중에서 입력하세요.")
