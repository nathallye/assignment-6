import sys

try:
  integers = [int(value) for value in sys.argv[1].split(',')]
  threshold = int(sys.argv[2]) 
except ValueError:
  print("<span style='color: red;'>Error message: All numbers and threshold must be integers</span>")
  sys.exit()

bitwise_and = integers[0]
bitwise_or = integers[0]
bitwise_xor = integers[0]

for current_integer in integers[1:]:
  bitwise_and &= current_integer
  bitwise_or |= current_integer
  bitwise_xor ^= current_integer

integers_filter = [integer for integer in integers if integer > threshold]

html_output = (
  f"<p>Bitwise AND: <span style='color: green;'>{bitwise_and}</span></p>"
  f"<p>Bitwise OR: <span style='color: green;'>{bitwise_or}</span></p>"
  f"<p>Bitwise XOR: <span style='color: green;'>{bitwise_xor}</span></p>"
  f"<p>Numbers greater than threshold: <span style='color: green;'>{integers_filter}</span></p>"
)

print(html_output)