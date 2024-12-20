my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
while True:
    set_ = my_list[number]
    if number == len(my_list):
        break
    if set_ == 0:
        number = number + 1
        continue
    if set_ > 0:
        print(set_)
        number = number + 1
    else:
        break
