import random
i = 0
o = 0
p = 0
while i<3:
  print("-"*100)
  print("\033[34m我们来猜拳,三局两胜\033[0m")
  compout = random.randint(1, 3)
  urs = int(input("1:布 2:石头 3:剪刀 请输数字："))
  if (compout == 1 and urs == 1) or (compout == 2 and urs == 2) or (compout == 3 and urs == 3):
      print(f"机器人：\033[31;42m{compout}\033[0m")
      print("机器人：\033[33m打平不算，再来\033[0m")
      print(f"\033[32m已赢{o}局\033[0m")
      print(f"\033[36m已输{p}\033[0m")
  elif (compout == 2 and urs == 1) or (compout == 3 and urs == 2) or (compout == 1 and urs == 3):
      print(f"机器人：\033[31;42m{compout}\033[0m")
      print("机器人：\033[32m可恶，你赢了，再来\033[0m")
      i += 1
      o += 1
      print(f"\033[32m已赢{o}局\033[0m")
      print(f"\033[36m已输{p}\033[0m")
      if o == 2:
          print("\033[32mwin\033[0m")
          print("机器人：还玩不？")
          hea_1 = input("1：玩 ，2：不玩")
          if hea_1 == "1":
              i = 0
              o = 0
              p = 0
          elif hea_1 == "2":
              print("结束")
  elif (compout == 1 and urs == 2) or (compout == 3 and urs == 1) or (compout == 2 and urs == 3):
      print(f"机器人：\033[31;42m{compout}\033[0m")
      print("机器人：\033[31m哈哈哈，我赢了\033[0m")
      p += 1
      i += 1
      print(f"\033[32m已赢{o}局\033[0m")
      print(f"\033[36m已输{p}\033[0m")
      if p == 2:
          print("lose")
          print("机器人：还玩不？")
          hea_1 = input("1：玩 ，2：不玩")
          if hea_1 == "1":
              i = 0
              o = 0
              p = 0
          elif hea_1 == "2":
              print("结束")
  else:
      print("\033[1;31m机器人：你会玩吗？\033[0m")
      print("\033[1;31m数据错误\033[0m")
      print(f"\033[32m已赢{o}局\033[0m")
      print(f"\033[36m已输{p}\033[0m")
