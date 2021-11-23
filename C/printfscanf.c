#include <stdio.h>

int main(void){
  // float f = 46.5;
  // printf("%.2f\n", f);
  // double d = 4.428;
  // printf("%.2lf", d);
  // const int YEAR = 2000;
  // printf("%d\n", YEAR);
  //printf
  // int add = 3 + 7; // 10
  // printf("3 + 7 = %d\n", add);
  // printf("%d x %d = %d", 3, 7, 3 * 7);
  //scanf
  // int input;
  // printf("값을 입력하세요: ");
  // scanf("%d", &input);
  // printf("입력값은: %d\n", input);

  // int one, two, three;
  // printf("3개의 정수를 입력하세요: ");
  // scanf("%d %d %d", &one, &two, &three);
  // printf("one, two, three: %d, %d, %d\n", one, two, three);
  char str[15];
  scanf("%s", str, sizeof(str));
  printf("%s", str);


  return 0;
}