def fibonacci(num):
    if num == 0:
        return 0;
    elif num == 1:
        return 1;
    else:
        return fibonacci(num - 1) + fibonacci(num - 2);


count = 0;
while count <= 20:
    print(fibonacci(count));
    count = count+1;