def run():
  increment = lambda x: x + 5
  high_order_func = lambda x, func: x + func(x)

  result = high_order_func(10, increment)
  result2 = high_order_func(10, lambda x: x ** 2)
  
  print(result)
  print(result2)

if __name__ == '__main__':
  run()
