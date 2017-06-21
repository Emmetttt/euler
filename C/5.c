#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>

bool divisible(int number, int max){
    for (int i = 2; i < max+1; i++){
    	if (number%i != 0){
    		return false;
    	}
    }
    return true;
}

int main() {
    clock_t begin = clock();

    int i = 20;
    int max = 20;
    while (divisible(i, max) == false){
    	i+=20;
    }
    printf("2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.\n\nWhat is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?\n\n");
    printf("%d\n", i, max);

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%f seconds spent executing code.\n", time_spent);
}