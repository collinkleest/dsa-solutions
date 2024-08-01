

def first_x(s: str, i: int) -> int:
    if len(s) == 0:
        return i
    if s[0] == 'x':
        return i
    
    return first_x(s[1:], i + 1)

s = "abcgjkxasd"

i = first_x(s, 0)

print(i)

