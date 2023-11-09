"""
*
* *
* * *
* * * *
"""

# for row in range(4):
#     for col in range(row+1):    # 2
#         print("*", end=" ")
#     print()

for row in range(1, 5):
    print("* " * row)
print()

"""
* * * *
* * *
* *
*
"""

for row in range(4, 0, -1):
    print("* " * row)

"""
      *
    * *
  * * *
* * * *
"""

for row in range(1, 5):
    print(f'{"* " * row:>8}')

"""
* * * *
  * * *
    * *
      *
"""

for row in range(4, 0, -1):
    print(f"{'* ' * row:>8}")

"""
     *
    * *
   * * *
  * * * *
"""

for row in range(1, 5):
    print(f'{"* " * row:^8}')

"""
* * * *
 * * *
  * *
   *
"""

for row in range(4, 0, -1):
    print(f'{"* " * row:^8}')

"""
*
*
*
* *
*
* * *
*
* * * *
"""

for row in range(1, 5):
    print("*")
    print("* " * row)

"""
1
1 2
1 2 3
1 2 3 4
"""

for row in range(1, 5):
    for col in range(1, row+1):
        print(col, end=" ")
    print()

x = ""
for row in range(1, 5):
    x += str(row) + " "      # "1", "12", "123", "1234"
    print(x)

"""
a
a b
a b c
a b c d

a b c d
a b c
a b
a
"""



