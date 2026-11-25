import json
class Record:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount
    def __str__(self):
        return f"{self.item}:{self.amount}元"
    def __eq__(self, other):
        return self.item == other.item and self.amount == other.amount
    def to_dict(self):
        return {"item": self.item, "amount": self.amount}
class IncomeRecord(Record):
    def __str__(self):
        return f"+{self.item}:{self.amount}"
    def to_dict(self):
        d = super().to_dict()
        d["type"] = "income"
        return d
DATA_FILE = "账本.json"
LOG_FILE = "日志.txt"
def find_max_expense(records):
    if not records:
        return None
    best = records[0]
    for r in records:
        if best.amount < r.amount:
            best = r
    return best
records = []
try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        records = []
        for d in json.loads(f.read()):
            if d.get("type") == "income":
                records.append(IncomeRecord(d["item"], d["amount"]))
            else:
                records.append(Record(d["item"], d["amount"]))
except FileNotFoundError:
    records = []
while True:
    print("\n==== 我的记账本 ====")
    print("1. 记一笔 2. 查看账本 3. 退出 4. 今日统计 5. 日志 6. 删一笔 7. 记收入")
    choice = input("请选择:")
    if choice == "1":
        item = input("项目:")
        try:
            amount = int(input("金额:"))
        except ValueError:
            print("要是数字")
        else:
            record = Record(item, amount)
            records.append(record)
            print(record)
            with open(LOG_FILE, 'a', encoding="utf-8") as f:
                f.write(f"记账:{item}:{amount}\n")
            dicts = [r.to_dict() for r in records]
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(dicts, f, ensure_ascii=False)
    elif choice == "2":
        for r in records:
            print(r)
    elif choice == "3":
        print("再见!")
        break
    elif choice == "4":
        spend = 0
        income = 0
        if not records:
            print("账本是空的")
        else:
            expenses = [r for r in records if not isinstance(r, IncomeRecord)]
            best = find_max_expense(expenses)
            if best:
                print(f"最贵一笔:{best.item}:{best.amount}")
            else:
                print("还没有支出")
        for r in records:
            if isinstance(r, IncomeRecord):
                income += r.amount
            else:
                spend += r.amount
        print(f"总支出:{spend}元 总收入:{income}元")
        if spend > 100:
            print("超了")
        else:
            print("节省")
    elif choice == "5":
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("无")
    elif choice == "6":
        other_item = input("要删的项目名:")
        try:
            other_amount = int(input("要删的金额:"))
        except ValueError:
            print("金额要是数字")
        else:
            target = Record(other_item, other_amount)
            try:
                records.remove(target)
            except ValueError:
                print("没找到")
            else:
                print("已删")
                dicts = [r.to_dict() for r in records]
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump(dicts, f, ensure_ascii=False)
    elif choice == "7":
        item = input("收入项目:")
        try:
            amount = int(input("金额:"))
        except ValueError:
            print("要是数字")
        else:
            record = IncomeRecord(item, amount)
            records.append(record)
            print(record)
            dicts = [r.to_dict() for r in records]
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(dicts, f, ensure_ascii=False)
    else:
        print("错误, 重新输入")


