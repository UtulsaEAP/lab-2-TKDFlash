def telephone():
#   phone_number = int(input())
    ''' Type your code here. '''
    phone_number = int(input())

    area_code = phone_number // 10000000
    prefix =  (phone_number // 10000) % 1000
    line_number = phone_number % 10000

    print (f"({area_code}) {prefix}-{line_number}")

if __name__ == "__main__":
    telephone()