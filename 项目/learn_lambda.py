# def square(x):
#     return x * x
# print(square(5))
# sq = lambda x: x * x
# print(sq(5))
# records = [
#     {"item": "午饭", "amount": 30},
#     {"item": "工资", "amount": 10000},
#     {"item": "打车", "amount": 50}
# ]
# records.sort(key=lambda r:r["amount"], reverse=True)
# print(records)
import re
def filter_success_logs(logs):
    amounts = [int(re.findall(r"\d+", log)[0]) for log in logs if "成功" in log]
    return amounts
