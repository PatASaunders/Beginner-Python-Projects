def main(number):
    result = index = 0
    while number:
        number, remainder = divmod(number, 10)
        result += (remainder + 1) * 10 ** index
        index += (remainder == 9) + 1
        print(number)
        print(remainder)
    return result or 1


print(main(998))  # 10109