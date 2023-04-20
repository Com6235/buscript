import compiler
# Usage example
d = compiler.compile_file("test.buscript")
print(d)
exec(d)