import compiler
# Usage example
d = compiler.compile_file("test.ruscript")
print(d)
exec(d)