import unittest
import re
def filter_success_logs(logs):
    amounts = [int(re.findall(r"\d+", log)[0]) for log in logs if "成功" in log]
    return amounts


class Test(unittest.TestCase):
    def test_extract_amounts(self):
        mock_logs = [
            "用户A 充值 100元, 状态: 成功",
            "用户B 充值 50元, 状态: 失败",
            "用户C 充值 200元, 状态: 成功"
        ]
        result = filter_success_logs(mock_logs)
        self.assertEqual(result, [100, 200])


    def test_filter_success_logs(self):
        mock_logs = ["用户B 充值 50元, 状态: 失败"]
        result = filter_success_logs(mock_logs)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()