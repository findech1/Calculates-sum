#include<stdio.h>
//declare the function
void read();
float calc(int *x, float *y); // Corrected the declaration

int main()
{
    //call and pass nothing
    read();
    return 0;
}

//define read() function
void read(){
    int a;
    float b, c;
    printf("Enter whole number followed by a real number\n");
    scanf("%d %f", &a, &b);
    c=calc(&a, &b);
    printf("The result is %.2f\n", c);
}

//define calc() function
float calc(int *x, float *y){
    float z;
    z= *x + *y;
    return z;
}