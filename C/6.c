#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

int main() {
    clock_t begin = clock();

	int sum = 0;
	int square = 0;
	int max = 100;

	for (int i = 1; i < max+1; i++){ /*sum*/
		sum += i*i;
		square += i;
	}

	square = square*square;
	int difference = square - sum;
	printf("The sum of the squares of the first ten natural numbers is,\n\n12 + 22 + ... + 102 = 385\n\nThe square of the sum of the first ten natural numbers is,\n\n(1 + 2 + ... + 10)2 = 552 = 3025\n\nHence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.\n\nFind the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.\n\n");
	printf("%d\n", difference);

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%f seconds spent executing code.\n", time_spent);
}