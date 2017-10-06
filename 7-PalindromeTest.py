def palindrome(n):
    result = True
    for i in range(0, len(n) // 2):
        if n[i] != n[-i - 1]:
            result = False
            break
    return result

if __name__ == "__main__":#https://stackoverflow.com/questions/419163/what-does-if-name-main-do
#how to use __name__ == "__main__
    input_str = input("Please input a string:\n")
    if palindrome(input_str):
        print("%s is a palindrome" % input_str)
    else:
        print("%s is not a palindrome" % input_str)