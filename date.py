def read_date():#년,월,일을 정수로 처리
    year,month,day=tuple(map(int,input().split()))
    #map: 모든 요소에 대하여 int처리 한다.tuple: 세 개를 튜플로 묶음.
    return year,month,day

def print_date(date):
    year,month,day=date
    print("%02d/%02d/%04d" % (month,day,year))

def advance_day(date):#다음날 함수
    year,month,day=date
    end_of_month=(month,day) in [(1,31),(2,28),(3,31),(4,30),(5,31),(6,30),(7,31)
                                 ,(8,31),(9,30),(10,31),(11,30),(12,31)]
    end_of_year=month == 12 and day== 31
#한달이 끝날때,그 중 연이 끝나는 달과 일의 조합이면 연에 1을 더하고,
#월과 일을 1로 한다.
#그게 아니라면 월에만 1을 더한다.
    if end_of_month:
        if end_of_year:
            year+=1
            month=1
            day=1
        else:
            month+=1
            day=1
#월의 끝이 아니면 그냥 일에 1 더함.
    else:
        day+=1

    return year,month,day

if __name__ == "__main__":
    today = read_date()#today에 입력받음
    print_date(today)#오늘 날짜 출력
    tomorrow = advance_day(today)
    print_date(tomorrow)
