# 复现：同样是块语句开头，同步写法保住两个空行，异步写法只剩一个
import black

mode = black.Mode()
sync = "if x:\n    def f():\n        pass\n\n\nwith a:\n    pass\n"
asyn = "if x:\n    def f():\n        pass\n\n\nasync with a:\n    pass\n"
for name, src in (("with", sync), ("async with", asyn)):
    out = black.format_str(src, mode=mode)
    blanks = out.split("\n")[3]
    print(name, "->", repr(out), "| 块头之前的空行数 =", out.count("\n\n\n") and 2 or 1)
