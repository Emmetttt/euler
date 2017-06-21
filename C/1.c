#include <stdio.h>  

int main(){
    int length = 1000;
    int x = 3;
    int y = 5;
    int sum = 0;
    for (int i=0; i < length; i++){
        if (i % x == 0 || i % y == 0){
            sum = sum + i;
        }
    }
    printf("If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.\n\nFind the sum of all the multiples of 3 or 5 below 1000.\n\n");
    printf("%d", sum);
} 
