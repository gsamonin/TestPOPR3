class Perevod:
    def FutVMetr(self, x):
        return x * 0.3

    def DumVMetr(self, x):
        return x * 0.025

    def YardVMetr(self, x):
        return x * 0.91

    def VershVMetr(self, x):
        return x * 0.044

    def VershVMetr(self, x):
        return x * 0.044

    def PyadVMetr(self, x):
        return x * 0.18


# def  AmVSI(x):
#    print('Перевод из Американской в СИ')
#    per = int(input('Укажите единицу измерения:\n 1. Дюйм\n'
#                    ' 2. Фут \n 3. Ярд\n 4. Миля\n'))
#    if (per == 2):
#        print('Выбраты футы')
#        j = float(input())
#        FutVMetr(j)

#   print('Выберите тип перевода. \n 1. Перевод из Американской в СИ'
#         ' \n 2. Перевод из Старорусской в СИ \n 3. Выйти из системы')
#   x = int(input())
#   if (x == 1):
#       AmVSI(x)
#   elif (x == 2):
#       AmVSI(x)
#   else:
#       return 0


if __name__ == '__main__':
    main()
