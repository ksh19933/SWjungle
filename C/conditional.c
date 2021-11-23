#include <stdio.h>

int main(void){
  // 버스를 탄다고 가정, 학생 / 일반인으로 구분
  int age = 12;
  if (age>=20)
  {
    printf("일반인 입니다.\n");
  }
  else if (age >=17)
  {
    printf("고등학생입니다.\n");
  }
  else if (age >=14)
  {
    printf("중학생입니다.\n");
  }
  else if (age >=8)
  {
    printf("초등학생입니다.\n");
  }
  return 0;
}