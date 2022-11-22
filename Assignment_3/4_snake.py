snake_len = int(input("Enter lenth of snake  : "))
count = 0
if snake_len == 1: 
    print("*")
else :
    for j in range(1,snake_len ):
        if count < snake_len : 
            print('*', end='')
            count += 1 
            if count == snake_len :
                break
        if count < snake_len :
            count += 1
            print('#', end='')
            if count == snake_len :
                break