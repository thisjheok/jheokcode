import random
import time
체력=random.randrange(3,7)
공격=random.randrange(3,7)
방어=random.randrange(3,7)
특수공격=random.randrange(3,7)
특수방어=random.randrange(3,7)
스피드=random.randrange(3,7)
print("알에서 포켓몬이 태어났다!")
time.sleep(2)
print("태어난 포켓몬의 이름을 지어주시겠습니까?(y/n)")
A=input()
if A=="y":
    new=input("이름을 입력하세요")
    print(f"""[{new}의 상태]
레벨=1
체력={체력}
공격={공격}
방어={방어}
특수공격={특수공격}
특수방어={특수방어}
스피드={스피드}
""")
if A=="n":
    print(f"""[포켓몬의 상태]
레벨=1
체력={체력}
공격={공격}
방어={방어}
특수공격={특수공격}
특수방어={특수방어}
스피드={스피드}
""")



