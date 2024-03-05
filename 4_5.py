#1000000(贷款金额) 2(贷款年数) 10(1/10 的年利率)
#输出: 1,1008333.33,8333.33
csv_filename = 'output.csv'
with open(csv_filename,'w') as csvfile:
    loan, year, rate = map(float, input().split())
    mon = int(year) * 12
    print("Месяц,Сумма на вкладе,Начисление",file = csvfile)
    for i in range(mon):
        accrual = loan * rate / 100.0 / 12.0
        print(i + 1, "%.2f" % (loan + float(accrual)), "%.2f" % accrual, sep=',', end='\n',file = csvfile)
        loan = loan + accrual
    csvfile.close()
