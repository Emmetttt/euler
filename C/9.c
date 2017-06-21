#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>

double pythagsum(double a, double b){
	double c = sqrt((a*a) + (b*b));
	return a+b+c;
}

double pythagproduct(double a, double b){
	double c = sqrt((a*a) + (b*b));
	return a*b*c;
}

int main() {
    clock_t begin = clock();

    double max = 0;

    for (double a = 200; a<1000; a++){
    	for (double b = 200; b<1000; b++){
    		if (pythagsum(a, b) == 1000 && pythagproduct(a, b) > max){
    			max = pythagproduct(a, b);
    			printf("%f^2 + %f^2 + %f^2 = %f\n", a, b, sqrt((a*a) + (b*b)), pythagsum(a,b));
    		}
    	}
    }
    printf("A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,\n\na2 + b2 = c2\nFor example, 32 + 42 = 9 + 16 = 25 = 52.\n\nThere exists exactly one Pythagorean triplet for which a + b + c = 1000.\nFind the product abc.\n\n");
    printf("Largest product is %f\n", max);

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%f seconds spent executing code.\n", time_spent);
}