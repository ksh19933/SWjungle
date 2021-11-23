#include <time.h>
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
  //srand(time(NULL)); // 난수 초기화

  printf("난숫 초기화 이전.. \n");
  for (int i = 0; i < 10; i++)
    printf("%d", rand() % 10); // 1~3 랜덤

  srand(time(NULL));
  printf("\n난수 초기화 이후.. \n");
  for (int i = 0; i < 10; i++)
    printf("%d", rand() % 10);

  return 0;
}