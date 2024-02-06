
def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    ''' Type your code here. '''

    product_1 = num1*num2*num3*num4
    average_1 = (num1+num2+num3+num4)/4

    product_2 = num1*num2*num3*num4
    average_2 = (num1+num2+num3+num4)/4

    print(f'{product_1:.0f}',f'{average_1:.0f}')
    print(f'{product_2:.3f}',f'{average_2:.3f}')

if __name__ == "__main__":
    simple_stats()