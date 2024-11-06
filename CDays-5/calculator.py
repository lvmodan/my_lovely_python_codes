import math
import re

class Calculator:
    def __init__(self):
        self.operatorDict ={
            '+': lambda a, b: float(a)+float(b),
            '-': lambda a, b: float(a)-float(b),
            '*': lambda a, b: float(a)*float(b),
            '/': lambda a, b: float(a)/float(b),
            '^': lambda a, b: float(a)**float(b),
        }

    def handle_expression(self, expression):
        # 添加计算功能
        if 'pi' in expression:
            expression = expression.replace('pi', str(math.pi))
        if 'sin' in expression:
            # 使用math库计算sin
            expression = re.sub('sin\((.*?)\)', lambda x: str(math.sin(math.radians(float(x.group(1))))), expression)
        if 'cos' in expression:
            # 使用math库计算cos
            expression = re.sub('cos\((.*?)\)', lambda x: str(math.cos(math.radians(float(x.group(1))))), expression)
        for i in self.operatorDict:
            expression = expression.replace(i, 's'+i+'s')
        handled_expression = expression.split('s')
        return handled_expression

    def handle_negative(self, handled_expression):
        l2, i = [], 0
        he = handled_expression
        while i < len(he):
            # 处理负数
            if he[i] == '':  # 负号开头或者负号与其他运算符连在一起,splite后会为'',例如 -5*-2  ['','-','5','*','','-','2']
                l2.append(he[i+1]+he[i+2])   # 将符号和数字合一起  -2
                i += 2
            else:
                l2.append(he[i])
            i += 1
        return l2

    def compute_times_over_or_power(self, handled_expression):
        i = 1
        he = handled_expression
        while i < len(he):  # 计算乘除
            if he[i] in ['*', '/', '^']:
                # 将符号左右以及符号三个元素替换为运算结果,必须是个列表, list[m:n] :切片取值连续,不包括n
                he[i-1:i+2] = [self.operatorDict[he[i]](he[i-1], he[i+1])]  # 运算
            else:
                i += 2
        return he

    def compute_add_or_minus(self, handled_expression):
        # 运算加减,直接按顺序计算替换
        he = handled_expression
        while len(he) > 1:
            he[0:3] = [self.operatorDict[he[1]](he[0], he[2])]
        return str(he[0])

    def compute_in_brackets(self, expression):
        he1 = self.handle_expression(expression)
        he2 = self.handle_negative(he1)
        he3 = self.compute_times_over_or_power(he2)
        result = self.compute_add_or_minus(he3)
        return result

    def handle_brackets(self, expression):
        expression = expression.replace(' ', '')
        check = re.search('\([^\(\)]+\)', expression)
        while check:
            checkValue = check.group()
            expression = expression.replace(checkValue, self.compute_in_brackets(checkValue[1:-1]))
            check = re.search('\([^\(\)]*\)', expression)
        else:
            return self.compute_in_brackets(expression)

    def run(self):
        # 让计数器支持用户循环输入，输入q退出循环
        while True:
            expression = input('请输入要计算的表达式(输入q退出): ')
            expression = expression.lower()
        
            if expression == 'q':
                print('退出计算器')
                break
            try:
                result = self.handle_brackets(expression)
                print(f"{expression} = {result}")
            except Exception as e:
                print('表达式不合法，请重新输入；错误信息：', e)

if __name__ == "__main__":
    import argparse
    argsp = argparse.ArgumentParser(description="传参直接计算，不进入循环, 不传参进入循环！")
    argsp.add_argument('-e', "--expression", required=False, default="", type=str, help="传入想要计算的表达式")
    args = argsp.parse_args()
    expression = args.expression
    cal = Calculator()
    if expression == "":
        cal.run()
    else:
        result = cal.handle_brackets(expression)
        print(f"{expression} = {result}")
