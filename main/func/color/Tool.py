def rgb(r,g,b): # RGB(255,255,255) => ffffff
    s = "0123456789abcdef"
    re = ""
    re += s[b//16] + s[b%16]
    re += s[g//16] + s[g%16]
    re += s[r//16] + s[r%16]
    return re