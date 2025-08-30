import ast
import textwrap

# Check for syntax errors using AST
def check_syntax(code: str):
    try:
        ast.parse(code)
        return "NO ERRORS 😊👍"
    except SyntaxError as e:
        return f"Bro There is an Error 😭 on line {e.lineno} at column {e.offset}\nError is {e.msg}"
    
if __name__ == "__main__":
    code = """
    print("helloworld")
    age = int(input())
    if age == 18:
        pritn("okay")
    else:
        print("no")
    """

    code = textwrap.dedent(code)  
    print(check_syntax(code))