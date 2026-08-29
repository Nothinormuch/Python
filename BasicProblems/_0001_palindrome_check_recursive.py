# def func(Str,l,r):
#     if(l>r):
#         return True
#     return((Str[l]==Str[r]) and func(Str,l+1,r-1))

def func(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return func(s,l+1,r-1)

String = "aabbaaccaabbaab"
print(func(String,0,len(String)-1))
