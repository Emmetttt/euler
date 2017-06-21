#include <stdio.h> 
#include <math.h>
#include <stdbool.h>
#include <time.h>

bool isprime(int number){
    bool result = true;
    for (int i = 2; i < number/2; i++){
        if (number%i == 0){
            result = false;
        }
    }
    return result;
}

int main(){
    clock_t begin = clock();

    double number = 600851475143;
    double maximum = number/2;
    int largest = 0;

    int i = 2;
    if (fmod(number,i) == 0) {
        largest = i;
    } 

    for (i = 3; i < maximum; i+=2){
        if (fmod(number,i) == 0 && isprime(i)) {
            maximum = number/i;
            largest = i;
        } 
    }
    printf("The prime factors of 13195 are 5, 7, 13 and 29.\n\nWhat is the largest prime factor of the number 600851475143 ?\n\n");
    printf("%d\n", largest);

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%f seconds spent executing code.\n", time_spent);
}

