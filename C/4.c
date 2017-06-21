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

int main(){
	int X = 999;
	int Y = 999;
	int largest = 0;
	for (int i=0; i < 100; i++){
		for (int j=0; j < 100; j++){
			int mult = X*Y;

			if (palindrome(mult)) {
				if (mult > largest){
					largest = mult;
				}
			}
			Y--;
		}
		X -= 1;
		Y = X;
	}
	printf("A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.\n\nFind the largest palindrome made from the product of two 3-digit numbers.\n\n");
	printf("%d is the largest palindrome\n", largest);
}