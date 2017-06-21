#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>

bool isprime(int number){
    bool result = true;
    if (number%2 == 0){
        result = false;
    }
    for (int i = 3; i < sqrt(number)+1; i+=2){
        if (number%i == 0){
            result = false;
        }
    }
    return result;
}

int main() {
    clock_t begin = clock();

    long long sum = 2; /*2 is the only even prime*/
    int i = 3; /*start with 3*/
    int max = 2000000;

    while ( i<max ) {
    	if (isprime(i)){
    		sum+=i;
    	}
    	i+=2;
    }

    printf("The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.\n\nFind the sum of all the primes below two million.\n\n");
    printf("The sum of all primes up to %d is %lld.\n", max, sum);

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%f seconds spent executing code.\n", time_spent);
}