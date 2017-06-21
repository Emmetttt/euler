#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>


bool palindrome(int number){
    bool result = true;
    int size = log10(number)+1;

    if (size % 2 > 0){ /*Check to see if number can be a palindrome by number of digits*/
        result = false;
        return result;
    }

    int digits[10];
    int i = 0;
    while (number>0){ /*Each digit in a number stored in array*/
        digits[i] = number%10;
        number/=10;
        i++;
    }

    int j = 0;
    i--;
    while (i > -1){
        if (digits[j] != digits[i]){
            result = false;
            break;
        }
        j++;
        i--;
    }
    return result;
}

bool isprime(int number){
    bool result = true;
    for (int i = 2; i < sqrt(number); i++){
        if (number%i == 0){
            result = false;
        }
    }
    return result;
}
