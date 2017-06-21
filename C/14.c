#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

int collatz(double n, double count){
	if (n == 1){
		return count;
	}
	if (fmod(n,2) == 0){/*even*/
		n = n/2;
		count++;
		return collatz(n, count);
	}
	else {
		n = (3*n) + 1;
		count++;
		return collatz(n, count);
	}
}

int main() {
    clock_t begin = clock();

    double largest = 0;
    double *startnum;

    for (double i = 10; i < 1000001; i++){
    	if (collatz(i, 1) > largest){
    		largest = collatz(i, 1);
    		startnum = &i;
    		printf("%f produces longest chain\n", *startnum);
    	}
    }

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%f seconds spent executing code.\n", time_spent);
}