
def caffeine():
#    caffeine_mg = float(input())
    ''' Type your code here. '''

    caffeine_intake = float(input())
    hr_6 = caffeine_intake*(0.5**(6/6))
    hr_12 = caffeine_intake*(0.5**(12/6))
    hr_24 = caffeine_intake*(0.5**(24/6))

    print(f'After 6 hours: {hr_6:.2f} mg\n'f'After 12 hours: {hr_12:.2f} mg\n'f'After 24 hours: {hr_24:.2f} mg')
    
if __name__ == "__main__":
    caffeine()