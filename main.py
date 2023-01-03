import time
from colorama import Fore as F

def isReasonable(number: int):
  return number > 0 and number <= 1000


def roundTime(timeTaken: float):
  return round(time.time() - timeTaken, 2)


def formatting(x, a):
  return " ".join(map(str, x)).center(len(" ".join(map(str, a[-1]))))

  
def generate(numRows: int):
  if isReasonable(numRows):
    
    a = []
    totalInt = 0
    totalValue = 0
    fileName = input("Enter your file name (ending with .txt): ")

    task = time.time()
    for x in range(numRows):
      a.append([1])
      
      if x > 1:
        for c in range(x - 1):
          a[x].append(a[x - 1][c] + a[x - 1][c + 1])

      if x > 0:
        a[x].append(1)

      totalValue += sum(a[x])
      totalInt += len(a[x])

    with open(fileName, 'w') as file:

      for x in a:
        if x is not a[-1]:
          c = "\n"

        else:
          c = ""

        file.write(
          formatting(x,a) + c)

    buffer = f"[{F.GREEN}+{F.RESET}]"
    print(f"\n{buffer} Done creating the pyramid in {fileName} with value: {numRows}")
    
    print(f"Total: {roundTime(start)} seconds")
    print(f"Task:  {roundTime(task)} seconds")

    info = input(f"\n{buffer} Would you like additional info [yes/no]: ")
    
    if info.lower() in ['yes','y']:
      print(f"Total Int: {totalInt:,} numbers")
      print(f"Total Sum: {totalValue:,}")

    else:
      exit()
    
  else:
    bool = "large"
    if numRows == 0:
      bool = "small"
    print(f"{F.RED}Error Code: {numRows} too {bool}")


start = time.time()
numRows = int(input("Enter the amount of rows: "))
generate(numRows)