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


S1 = 0.1
S2 = 0.15
S3 = 0.25
S4 = 0.28
S5 = 0.33
S6 = 0.35
S7 = 0.396

personalD1 = 0
personalD2 = 9075
personalD3 = 36900
personalD4 = 89350
personalD5 = 186350
personalD6 = 405100
personalD7 = 406750

familyD1 = 0
familyD2 = 2 * personalD1
familyD3 = 2 * personalD2
familyD4 = 148850
familyD5 = 226850
familyD6 = personalD5
familyD7 = 457600

singleparentD1 = 0
singleparentD2 = 12950
singleparentD3 = 49400
singleparentD4 = 127550
singleparentD5 = 206600
singleparentD6 = personalD5
singleparentD7 = 432200


# TODO: формулы




D = 0
print(M_I)
for month in range(12):
    print('{} {}?: '.format(Question,name_month[month]))
    monthly_income = float(input())
    D = D + monthly_income


if individual == local.p1 or individual == local.p2:
    if personalD1 < D < personalD2:
        N = S1 * (D - personalD1)
    elif personalD2 < D < personalD3:
        N = S1 * (personalD2 - personalD1) + S2 * (D - personalD2)
    elif personalD3 < D < personalD4:
        N = S1 * (personalD2 - personalD1) + S2 * (personalD3 - personalD2) + S3 * (D - personalD3)
    elif personalD4 < D < personalD5:
        N = S1 * (personalD2 - personalD1) + S2 * (personalD3 - personalD2) + S3 * (personalD4 - personalD3) + S4 * (
                D - personalD4)
    elif personalD5 < D < personalD6:
        N = S1 * (personalD2 - personalD1) + S2 * (personalD3 - personalD2) + S3 * (personalD4 - personalD3) + S4 * (
                personalD5 - personalD4) + S5 * (D - personalD5)
    else:
        N = S1 * (personalD2 - personalD1) + S2 * (personalD3 - personalD2) + S3 * (personalD4 - personalD3) + S4 * (
                personalD5 - personalD4) + S5 * (personalD6 - personalD5) + S6 * (D - personalD6)

elif individual == local.f1 or individual == local.f2:
    if familyD1 < D < familyD2:
        N = S1 * (D - familyD1)
    elif familyD2 < D < familyD3:
        N = S1 * (familyD2 - familyD1) + S2 * (D - familyD2)
    elif familyD3 < D < familyD4:
        N = S1 * (familyD2 - familyD1) + S2 * (familyD3 - familyD2) + S3 * (D - familyD3)
    elif familyD4 < D < familyD5:
        N = S1 * (familyD2 - familyD1) + S2 * (familyD3 - familyD2) + S3 * (familyD4 - familyD3) + S4 * (
                D - familyD4)
    elif familyD5 < D < familyD6:
        N = S1 * (familyD2 - familyD1) + S2 * (familyD3 - familyD2) + S3 * (familyD4 - familyD3) + S4 * (
                familyD5 - familyD4) + S5 * (D - familyD5)
    else:
        N = S1 * (familyD2 - familyD1) + S2 * (familyD3 - familyD2) + S3 * (familyD4 - familyD3) + S4 * (
                familyD5 - familyD4) + S5 * (familyD6 - familyD5) + S6 * (D - familyD6)

elif individual == local.sp1 or individual == local.sp2:
    if singleparentD1 < D < singleparentD2:
        N = S1 * (D - singleparentD1)
    elif singleparentD2 < D < singleparentD3:
        N = S1 * (singleparentD2 - singleparentD1) + S2 * (D - singleparentD2)
    elif singleparentD3 < D < singleparentD4:
        N = S1 * (singleparentD2 - singleparentD1) + S2 * (singleparentD3 - singleparentD2) + S3 * (D - singleparentD3)
    elif singleparentD4 < D < singleparentD5:
        N = S1 * (singleparentD2 - singleparentD1) + S2 * (singleparentD3 - singleparentD2) + S3 * (
                singleparentD4 - singleparentD3) + S4 * (D - singleparentD4)
    elif singleparentD5 < D < singleparentD6:
        N = S1 * (singleparentD2 - singleparentD1) + S2 * (singleparentD3 - singleparentD2) + S3 * (
                singleparentD4 - singleparentD3) + S4 * (singleparentD5 - singleparentD4) + S5 * (D - singleparentD5)
    else:
        N = S1 * (singleparentD2 - singleparentD1) + S2 * (singleparentD3 - singleparentD2) + S3 * (
                singleparentD4 - singleparentD3) + S4 * (singleparentD5 - singleparentD4) + S5 * (
                singleparentD6 - singleparentD5) + S6 * (D - singleparentD6)

else:
    print(Tax_Error)




# TODO: вывод, по вопросу задачи
print(printN, N)
