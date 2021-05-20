from task_2_3 import currency_rates

print(currency_rates())

def main(argv):
   from task_2_3 import currency_rates
   program, *args = argv
   result = args
   result = ''.join(result)
   print(currency_rates(result))

   return 0


if __name__ == '__main__':
   import sys

   exit(main(sys.argv))