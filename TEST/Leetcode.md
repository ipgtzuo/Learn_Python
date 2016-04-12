```python
# --*-- coding: utf-8 --*--

# 将abc def形式的字符串翻转成def abc，并且去掉多余的空格。
# 先将这个字符串翻转过来，再逐次翻转每个词。


class Solution:
    def reverseWords(self, s):
        print s[::-1]
        print s[::-1].split()
        return ' '.join([word[::-1] for word in s[::-1].split()])


s = "Hello World."
a = Solution()
print a.reverseWords(s)
```