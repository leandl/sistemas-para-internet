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
  ( "[]{}(){([])}", True ),
  ( "{", False ),
  ( "}", False ),
  ( "as[]sdas(", False ),
  ( "a[b{c(d)e}f]", True ),
  ( "(]", False ),
  ( "(}", False ),
  ( "{)", False ),
  ( "{]", False ),
  ( "[)", False ),
  ( "[}", False ),
  ( "[b]b{a}a(a){b(b[dsadsa]b)b}b", True ),
]

for expression, expected_result in tests:
  result = checkExpression(expression)
  test_valid = result == expected_result

  print(f"expression: '{expression}', expected_result: {expected_result}, result: {result}, test_valid: {test_valid}")
