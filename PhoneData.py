import Cellphone


def main():
    phones = make_list()
    print('Here is data entered')
    display_list(phones)


def make_list():
    phone_list = []
    print('Enter data for 5 phones')
    for count in range(1, 6):
        print('number' + str(count) + ': ')
        man = input('Enter manufacturer: ')
        mod = input('Enter model num: ')
        retail = float(input('Enter price: '))
        print()
        phone = classes2.Cellphone(man, mod, retail)
        phone_list.append(phone)
    return phone_list


def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_price())
        print()


main()


