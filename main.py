"""Case-study #2
Developers:
Shunina A (40%), Matsko A (41%), Bakulina A(40%)"""


import local

# TODO: входные данные

language = str(input(local.Choose_language))

if language == local.language1:
    ind = local.Choose_individual1
    M_I = local.Read_monthly_income1
    Tax_Error = local.TaxError1
    name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    Question = local.question1
    printN = local.N1

elif language == local.language2:
    ind = local.Choose_individual2
    M_I = local.Read_monthly_income2
    Tax_Error = local.TaxError2
    name_month = ['ЯНВ', 'ФЕВ', 'МАР', 'АПР', 'МАЙ', 'ИЮН', 'ИЮЛ', 'АВГ', 'СЕН', 'ОКТ', 'НОЯ', 'ДЕК']
    Question = local.question2
    printN = local.N2

else:
    print(local.langError)

individual = str(input(ind))

S = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]

personal = [0, 9075, 36900, 89350, 186350, 405100, 406750]

family = [0, 18151, 73801, 148850, 226850, 405100, 457600]

singleparent = [0, 12950, 49400, 127550, 206600, 405100, 432200]


# TODO: формулы




D = 0
print(M_I)
for month in range(12):
    print('{} {}?: '.format(Question,name_month[month]))
    monthly_income = float(input())
    D = D + monthly_income

if individual == local.p1 or individual == local.p2:
    if personal[0] < D < personal[1]:
        N = S[1] * (D - personal[0])
    elif personal[1] < D < personal[2]:
        N = S[1] * (personal[1] - personal[0]) + S[2] * (D - personal[1])
    elif personal[2] < D < personal[3]:
        N = S[1] * (personal[1] - personal[0]) + S[2] * (personal[2] - personal[1]) + S[3] * (D - personal[2])
    elif personal[3] < D < personal[4]:
        N = S[1] * (personal[1] - personal[0]) + S[2] * (personal[2] - personal[1]) + S[3] * (
                personal[3] - personal[2]) + S[4] * (D - personal[3])
    elif personal[4] < D < personal[5]:
        N = S[1] * (personal[1] - personal[0]) + S[2] * (personal[2] - personal[1]) + S[3] * (
                personal[3] - personal[2]) + S[4] * (personal[4] - personal[3]) + S[5] * (D - personal[4])
    else:
        N = S[1] * (personal[1] - personal[0]) + S[2] * (personal[2] - personal[1]) + S[3] * (
                personal[3] - personal[2]) + S[4] * (personal[4] - personal[3]) + S[5] * (
                personal[5] - personal[4]) + S[6] * (D - personal[5])


elif individual == local.f1 or individual == local.f2:
    if family[0] < D < family[1]:
        N = S[1] * (D - family[1])
    elif family[2] < D < family[3]:
        N = S[1] * (family[2] - family[1]) + S[2] * (D - family[2])
    elif family[3] < D < family[4]:
        N = S[1] * (family[2] - family[1]) + S[2] * (family[3] - family[2]) + S[3] * (D - family[3])
    elif family[4] < D < family[5]:
        N = S[1] * (family[2] - family[1]) + S[2] * (family[3] - family[2]) + S[3] * (family[4] - family[3]) + S[4] * (
                D - family[4])
    elif family[5] < D < family[6]:
        N = S[1] * (family[2] - family[1]) + S[2] * (family[3] - family[2]) + S[3] * (family[4] - family[3]) + S[4] * (
                family[5] - family[4]) + S[5] * (D - family[5])
    else:
        N = S[1] * (family[2] - family[1]) + S[2] * (family[3] - family[2]) + S[3] * (family[4] - family[3]) + S[4] * (
                family[5] - family[4]) + S[5] * (family[6] - family[5]) + S[6] * (D - family[6])

elif individual == local.sp1 or individual == local.sp2:
    if singleparent[0] < D < singleparent[1]:
        N = S[1] * (D - singleparent[0])
    elif singleparent[1] < D < singleparent[2]:
        N = S[1] * (singleparent[1] - singleparent[0]) + S[2] * (D - singleparent[1])
    elif singleparent[2] < D < singleparent[3]:
        N = S[1] * (singleparent[1] - singleparent[0]) + S[2] * (singleparent[2] - singleparent[1]) + S[3] * (
                D - singleparent[2])
    elif singleparent[3] < D < singleparent[4]:
        N = S[1] * (singleparent[1] - singleparent[0]) + S[2] * (singleparent[2] - singleparent[1]) + S[3] * (
                singleparent[3] - singleparent[2]) + S[4] * (D - singleparent[3])
    elif singleparent[4] < D < singleparent[5]:
        N = S[1] * (singleparent[1] - singleparent[0]) + S[2] * (singleparent[2] - singleparent[1]) + S[3] * (
                singleparent[3] - singleparent[2]) + S[4] * (singleparent[4] - singleparent[3]) + S[5] * (
                D - singleparent[4])
    else:
        N = S[1] * (singleparent[1] - singleparent[0]) + S[2] * (singleparent[2] - singleparent[1]) + S[3] * (
                singleparent[3] - singleparent[2]) + S[4] * (singleparent[4] - singleparent[3]) + S[5] * (
                singleparent[5] - singleparent[4]) + S[6] * (D - singleparent[5])

else:
    print(Tax_Error)


# TODO: вывод, по вопросу задачи
print(printN, N)
