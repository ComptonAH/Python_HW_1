# # Задача 2: Найдите сумму цифр трехзначного числа.
# N = input("Enter a three-digit number: ")

# if len(N)!=3:
#     print("You must to enter a three-digit number")
# else:
#     N = int(N)
#     a = N//100; b = (N//10)%10; c = N%10
#     print(sum([a,b,c],0))




# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# N = int(input("Number of swans: "))
# # x - Петя, y - Сережа, z -  Катя. После решения системы линейных уравнений получаем:
# x = N/6; y = N/6; z = 4*N/6
# print(f"Petya made {x} swans, Serezha made {y} swans, Katya made {z} swans")





# # Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# # Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# # Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# N = input("Enter a 6-digit number: ")
# if len(N) != 6:
#     print("You must to enter a 6-digit number")
# else:
#     N = int(N)
#     a = [N//100000,N//10000 % 10,N//1000 % 10]
#     b = [N%1000 // 100, N%100 // 10, N%10]
#     c = sum(a,0); d = sum(b,0)
#     if c == d:
#         print("The ticket is 'lucky' ")
#     else:
#         print("The ticket is not 'lucky' ")






# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Enter a length of a chocolate bar: "))
m = int(input("Enter a width of a chocolate bar: "))
k = int(input("Enter a number of parts of the chocolate bar: "))

if n*m>=k and k%n == 0 or k%m == 0:
    print("This action is available")
else:
    print("This action is NOT available")