def cook_meat(num):
    print("---师傅开始烤肉了---")
    for i in range(1, num + 1):
        print(f"师傅烤好第{i}盘肉...")
        yield f"第{i}盘肉"
    print("---肉全烤完了---")
meat_generator = cook_meat(3)
print("来一盘")
print(next(meat_generator))
print("再来")
print(next(meat_generator))
print("还要")
print(next(meat_generator))