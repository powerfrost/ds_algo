def minAddToMakeValid(S):

        stack = []
        count = 0

        for i in S:
            if i == "(":
                stack.append(")")
            else:
                if len(stack) == 0:
                    count += 1
                elif i == stack[-1]:
                    stack.pop(-1)
        return len(stack) + count

def test():
    assert minAddToMakeValid("(") == 1
    assert minAddToMakeValid("()") == 0
    assert minAddToMakeValid(")") == 1
    assert minAddToMakeValid("(((") == 3
    assert minAddToMakeValid(")))") == 3
    assert minAddToMakeValid("()))") == 2
    assert minAddToMakeValid("()((") == 2
    assert minAddToMakeValid("((()") == 2
    assert minAddToMakeValid("") == 0

if __name__ == "__main__":
    test()
    print("Everything passed")
