'''


A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

        N is an integer within the range [1..2,147,483,647].

Complexity:

        expected worst-case time complexity is O(log(N));
        expected worst-case space complexity is O(1).


'''


# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

from re import findall


def solution(N):
    # write your code in Python 2.7
    if N == 0:
        return 0

    else:
        binary = ("{0:b}".format(N))

        try:
            bino = findall(r'[0]+', binary)
            bino.sort()
            return len(bino[-1])
        except:
            return 0


solution(0)
solution(15)
solution(1041)



# Another way to solve it
'''
def solution(N):
    binary = '{0:b}'.format(N)
    stripd = binary.strip("0")
    print(stripd)
    splited = binary.split("1")
    print(splited)
    bg = max(splited)
    #bg = max('{0:b}'.format(N).strip('0').split('1'))
    return 0 if bg == '' else len(bg)

print(solution(0))
print(solution(15))
print(solution(1041))
'''
