#include <stdio.h>
int main(void){
  // int 철수 = 1;
  // int 영희 = 2;
  // int 민수 = 3;

  // printf("철수네 주소 : %p, 암호 : %d \n", &철수, 철수);

  // int *미션맨; // 포인터 변수
  // 미션맨 = &철수;
  // printf("미션맨이 방문하는 곳 주소: %p, 암호 : %d \n", 미션맨, *미션맨);
  // 미션맨 = &민수;
  // printf("미션맨이 방문하는 곳 주소: %p, 암호 : %d \n", 미션맨, *미션맨);
  // //스파이
  // //미션맨이 바꾼 암호에서 2를 빼라!
  // int *스파이;
  // 스파이 = &철수;
  // *스파이 = *스파이 - 2;
  // printf("스파이가 방문하는 곳 주소:  %p, 암호 : %d", 스파이, *스파이);
  int arr[3] = {5, 10, 15};
  int *ptr = arr;
  for (int i = 0; i < 3;i++){
    printf("배열 arr[%d] 의 값: %p\n", i, arr);
  }
  for (int i = 0; i < 3;i++){
    printf("포인터 ptr[%d] 의 값: %d\n", i, ptr[i]);
  }
  ptr[0] = 100;
  ptr[1] = 200;
  for (int i = 0; i < 3;i++){
    printf("배열 arr[%d] 의 값: %d\n", i, *(arr+i)  );
  }
  for (int i = 0; i < 3;i++){
    printf("포인터 ptr[%d] 의 값: %d\n", i, ptr[i]);
  }

  return 0;
}