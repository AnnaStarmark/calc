# -*- coding: utf-8 -*-
import sys

def techinfo():
    print("__________________________")
    print("Сведения о платформе:")
    print(sys.version_info)
    print(sys.version)
    print("__________________________\n")

# --- Функция выводит информацию об авторе
def About():
    print(
    """
    Привет!
    ______________________________
    author: Anna Starmark
            class  8
            school 242
    e-mail: nn.starmark@gmail.com
    github: github.com/nn.starmark
    date:   09-02-2024    15:18:00
    ______________________________
    """
    )

def Selfdoc():
    print(
    ''' 
    ==========================================================           
        Арифметический калькулятор  calc
           
        В цикле надо вводить 2 числа и выбирать действие:
            +   для сложения этих чисел
            -   для вычисление разности
            *   для перемножени
            /   для деления 1-го на 2-е                         
        После выполнения действия печать результата
                
        При вводе чисел проверяется правильность чисел
            (строка должна содержать только цифры)
        Проверяется делитель при выборе деления ( != 0 )

        Вывод на дисплей в формате:
        <число> <арифметический знак> <число> = <результат> 

        В программе задействованы следующие функции:
        def About():            Об авторе
        def Selfdoc():          самодокументирования 
        def inputFloat(prompt): Ввод вещественного числа с проверкой
        def Fn_Calc(A, op, B):  Функ вычисления по аргументам A,B
                                где op из списка ['+','-','*','/']
        def Work():             Функция где весь цикл работы
        def main():             Основная функция программы
    ========================================================== 
        Пример простого диалога оператор-компьютер
    ========================================================== 
    '''
    )

def Fn_calc(vr1, oper, vr2):
    res = ""

    if(oper == '+'):
        res = str(float(vr1)+float(vr2))
    elif(oper == '-'):
        res = str(float(vr1)-float(vr2))
    elif(oper == '*'):
        res = str(float(vr1)*float(vr2))
    elif(oper == '/'):
        if(float(vr2) != 0):
            res = str(float(vr1)/float(vr2))
        else:
            res = "Деление на 0 не допустимо!"
    else:
        res = "Не верный символ оператора"

    return res

# --- Функция ввода числа с проверкой правильности
# --- В случае присутствия в числе не цифры - просит
# --- повторить ввод без ошибок
def inputFloat(prompt=None):
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print('Ошибка! Ожидалось вещественное число.')

def Work():
    while(True):
        print("Начинаем работать с калькулятором...")
        ok = input("Введите знак ? для выхода или ! для работы")
        if (ok == '?'): break

        var1 = inputFloat("Введите первое число: ")
        var2 = inputFloat("Введите первое число: ")
        op = input("Введите знак операции из списка [+, -, *, /]: ")

        print(var1, op, var2, "=", Fn_calc(var1, op, var2))

# -----------------------------------------------------
def main():
    techinfo()
    About()
    Selfdoc()
    Work()
    print("End program\n")

# =====================================================
if __name__ == "__main__":
    main()