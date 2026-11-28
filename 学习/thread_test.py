# import time
# from multiprocessing.pool import ThreadPool
# import requests
# from concurrent.futures import ThreadPoolExecutor
# import threading
# def dowork(id):
#     print(f"开始{id}下载")
#     time.sleep(2)
#     print(f"{id}完成")
# time1 = time.time()
# for i in range(1, 6):
#     dowork(i)
# print(f"耗时{time.time()-time1:.4f}")
# print("-" * 10)
# time2 = time.time()
# threads = []
# for i in range(1, 6):
#     t = threading.Thread(target=dowork, args=(i,))
#     threads.append(t)
#     t.start()
# for t in threads:
#     t.join()
# print(f"耗时{time.time()-time2:.4f}")
# urls = [
#     "https://www.baidu.com/",
#     "https://www.baidu.com/",
#     "https://www.baidu.com/",
#     "https://www.baidu.com/",
#     "https://www.baidu.com/",
#     "https://www.baidu.com/",
#     "https://www.baidu.com/",
# ]
# def crawl(url):
#     try:
#         response = requests.get(url, timeout=5)
#         print(f"{url}爬取成功, 长度{len(response.text)}")
#         return len(response.text)
#     except Exception as e:
#         print(f"{url}爬取失败:{e}")
#         return 0
# time1 = time.time()
# with ThreadPoolExecutor(max_workers=20) as executor:
#     results = list(executor.map(crawl, urls))
# print(f"耗时{time.time()-time1:.4f}")
# print(sum(results))
def make_multiplier(n):
    def tiit(x):
        h = x * n
        return h
    return tiit
gi = make_multiplier(3)
print(gi(5))