def findPalindromes(inputString):
    for i in range(len(inputString)):
        print(expand(inputString, i, i))


def expand(inputString, left, right):
    while left >= 0 and right <= (len(inputString)-1) and inputString[left] == inputString[right]:
        left += 1
        right -= 1
    return left+1, right



if __name__ == '__main__':
    findPalindromes("abba")
