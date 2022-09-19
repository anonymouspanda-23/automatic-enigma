def print_triangle(sentence: str) -> bool:
    sentence_len = len(sentence)
    if sentence_len < 4 or sentence_len >= 4 and sentence_len % 4 != 0:
        return False
    
    height = int(sentence_len / 4 + 1)
    midpoint = height

    print(' ' * (midpoint - 1), end='')
    print(sentence[0])

    for layer in range(1, height - 1):
        print(' ' * (midpoint - layer - 1), end='')
        print(sentence[layer], end='')
        print(' ' * ((layer - 1) * 2 + 1), end='')
        print(sentence[-layer])
    
    print(sentence[height - 1:sentence_len - height + 2])
    return True


if __name__ == '__main__':
    print(print_triangle('abcdefghijkl'))
    print()
    print(print_triangle('abcdefghijklmnopqrstuvwx'))
    print()
    print(print_triangle('abcdefghij'))
    print()
    print(print_triangle('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
    print()
    print(print_triangle('abcd'))
    print()
