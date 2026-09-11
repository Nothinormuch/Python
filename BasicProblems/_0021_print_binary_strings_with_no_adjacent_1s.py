def func(n,i=0,sub="",prev=False):
    if(n==i):
        print(str(sub))
        return

    sub+="0"
    func(n,i+1,sub,False)
    sub=sub[:-1]
    if not prev:
        sub+="1"
        func(n,i+1,sub,True)
        sub=sub[:-1]
func(4)
