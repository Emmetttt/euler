#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>


bool isprime(int number){
    bool result = true;
    for (int i = 2; i < sqrt(number); i++){
        if (number%i == 0){
            result = false;
        }
    }
    return result;
}


int main() {
    clock_t begin = clock();

    int numprimes = 1; /*auto count 2*/
    int i = 3;
    int nthprime = 10001;
    while (numprimes < nthprime){
    	if (isprime(i)){
    		numprimes++;
    	}
    	i+=2;
    }
    i-=2;	
    printf("By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.\n\nWhat is the 10 001st prime number?\n\n");
    printf("%d\n", i);

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%f seconds spent executing code.\n", time_spent);
}