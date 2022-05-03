from stack import Stack

def checkExpression(expression: str):
  my_stack = Stack(100)
  CHARS_EXPRESSION_OPEN = [ "{", "(", "[" ]
  CHARS_EXPRESSION_CLOSE = [ "}", ")", "]" ]

  check = {
    "{": "}",
    "(": ")",
    "[": "]"
  }

  for char in expression:
    if char in CHARS_EXPRESSION_OPEN:
      my_stack.push(char)
    elif char in CHARS_EXPRESSION_CLOSE:
      last_char_in_stack = my_stack.pop()
      if check.get(last_char_in_stack) != char:
        return False

  return my_stack.empty()

tests = [
  "dasda[]dasd(_dasd(])jkj",
  "}",
  "{}()[][({})]",
  "a{b(c[d]e)f}"
]

for test in tests:
  print(test, checkExpression(test))
