#mistake
time 모듈
time.strftime('%a', time.ctime())를 시도했으나 오류가 난 이유:
time.strftime() 함수의 두 번째 자리에는 time.localtime()이 반환하는 것과 같은 '시간 튜플(struct_time)' 객체가 들어가야 함.
time.ctime(): 이 함수는 'Wed Nov 5 18:05:12 2025'처럼 이미 완성된 문자열을 반환하기 때문
time.strftime('%a', time.localtime())을 쓰거나 생략하여 time.strftime('%a')쓰기

#random 모듈
로또 숫자들을 뽑아주는 프로그램을 만드려 했으나 잘 작동하지 않았음
(1) 초기 작성 코드 
import random
number_list = range(1,46)
popped_list= []
while len(pop_list) <6:

  number= random.randint(0, len(number_list)-1)

  number_list.pop(number)

  popped_list.append(number)

  return popped_list

#잘못한 부분
1.return 오류 : return은 함수 안에서만 사용할 수 있어서 오류 발생 -> print(popped_list)를 사용
2.range 객체 오류: range(1,46)은 리스트가 아닌 객체이고 range는 .pop() 매서드를 가지고 있지 않음 -> lsit(range(1,46))을 사용
3.논리 오류: popped_list.append(number)는 뽑힌 숫자가 아닌 인덱스를 리스트에 추가하고 있음 -> number가 아닌 number_list.pop(number)를 추가해야함


#수정한 코드 
import random
number_list = list(range(1,46))
pop_list= []
while len(pop_list) < 6:
  number= random.randint(0, len(number_list)-1)
  popped_number= number_list.pop(number)
  pop_list.append(popped_number)
print(pop_list)

# random.sample()을 사용한 더 간단한 코드 
import random
number_list = range(1, 46)
result_list = random.sample(number_list, 6)

print(result_list)