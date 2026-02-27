import re

for _ in range(int(input())):
    pattern = input()
    try:
        re.compile(pattern)

        # Manual check for invalid multiple quantifiers
        if "*+" in pattern or "++" in pattern or "?+" in pattern:
            print("False")
        else:
            print("True")

    except re.error:
        print("False")
