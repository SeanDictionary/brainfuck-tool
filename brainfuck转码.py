# BrainFuck 解释器
def brainfuck(code):
    # 创建数据内存带
    tape = [0] * 30000  # 使用 30,000 个单元格作为内存
    pointer = 0  # 指针初始位置
    code_pointer = 0  # 代码的指针
    bracket_map = {}  # 用于处理 [] 的跳转
    output = []  # 用来保存输出结果

    # 预处理：生成括号匹配的映射
    open_bracket_stack = []
    for i, command in enumerate(code):
        if command == '[':
            open_bracket_stack.append(i)
        elif command == ']':
            start = open_bracket_stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start

    while code_pointer < len(code):
        command = code[code_pointer]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            tape[pointer] = (tape[pointer] + 1) % 256  # 确保在 0-255 之间循环
        elif command == '-':
            tape[pointer] = (tape[pointer] - 1) % 256  # 确保在 0-255 之间循环
        elif command == '.':
            output.append(chr(tape[pointer]))  # 输出当前指针值对应的字符
        elif command == ',':
            tape[pointer] = ord(input('Input a character: ')[0])  # 接受一个字符输入
        elif command == '[':
            if tape[pointer] == 0:
                code_pointer = bracket_map[code_pointer]  # 跳转到相应的 ]
        elif command == ']':
            if tape[pointer] != 0:
                code_pointer = bracket_map[code_pointer]  # 跳回到相应的 [

        code_pointer += 1

    return ''.join(output)  # 返回输出结果

file_path = input("文件路径：")

with open(file_path,'r') as file:
    content = file.read()
    content = "".join(content.split())
print(brainfuck(content))