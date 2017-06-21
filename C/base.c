#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

int main() {
    clock_t begin = clock();

    /* code here */

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%f seconds spent executing code.\n", time_spent);
}