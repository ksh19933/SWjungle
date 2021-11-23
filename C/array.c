#include <stdio.h>

int main(void){
  // int subway_1 = 30;
  // int subway_2 = 40;
  // int subway_3 = 50;

  // printf("지하철 1호차에 %d명이 타고 있습니다. \n", subway_1);
  // printf("지하철 2호차에 %d명이 타고 있습니다. \n", subway_2);
  // printf("지하철 3호차에 %d명이 타고 있습니다. \n", subway_3);

  // int subway_array[3];
  // subway_array[0] = 30;
  // subway_array[1] = 40;
  // subway_array[2] = 50;
  // for (int i = 0; i < 3;i++){
  //   printf("지하철 %d호차에 %d명이 타고 있습니다. \n", i+1, subway_array[i]);
  // }

  float arr[10] = {1.0f, 2.0f, 3, 4, 5, 6, 7, 8, 9, 10};
  for (int i = 0; i < 10;i++){
    printf("%.2f\n", arr[i]);
  }

    return 0;
}