__author__ = 'nolan'


def group_check1(s):
    while "{}" in s or "()" in s or "[]" in s:
       s = s.replace("{}", "").replace("()", "").replace("[]", "")
    return not s


BRACES = {'(': ')', '[': ']', '{': '}'}


def group_check2(s):
    stack = []
    for b in s:
        c = BRACES.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack


if __name__ == '__main__':
    a = '[(){[][]([])}]'
    # b = '[()(())({)}]'
    # print "a", group_check1(a)
    # print "a", group_check2(a)
    # print "b", group_check1(b)
    print group_check2(a)