import random

guessesTaken=0

print('안녕하세요 이름이 무엇인가요?')
my_name=input()

number=random.randint(1,20)
print('좋습니다 '+my_name+', 1부터 20까지 숫자를 생각했습니다.')

while guessesTaken<6:
    print('맞혀보세요.')
    guess=input()#문자열임
    guess=int(guess)#정수로 바꿔줌, 그래야 비교가능

    guessesTaken=guessesTaken+1

    if guess<number:
        print('그것보단 높을 것 같아요!')
    if guess>number:
        print('그것보단 낮을 것 같아요!')
    if guess==number:
        break

if guess==number:
    guessesTaken=str(guessesTaken)
    print('잘하셨어요, '+my_name+'! 제가 생각한 숫자를'+guessesTaken+'회 안에 맞히셨네요!')
if guess!=number:
    number=str(number)
    print('아니요. 제가 생각한 숫자는 '+number+'입니다.')
