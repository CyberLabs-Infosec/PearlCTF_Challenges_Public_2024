#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

__attribute__((constructor))
void setup()
{
    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
}

void gadget_setup() {
  asm volatile ("pop %%rdi\n\t"
      "ret"
      :
      :
      : "rdi");
}

void review(){
    char note[20];
    int rate;

    printf("Rate your ticket booking experience from 1 to 5: ");
    scanf("%d", &rate);

    if (rate == 5)
    {
        printf("Thank you for the rating\n");
        printf("We hope you have a great journey\n");
        exit(0);
    }
    else if (rate < 5)
    {
        printf("We are sorry for the inconvenience\n");
        printf("Please help us to improve your future experience\n");
        getchar();
        fflush(stdin);
        gets(note);
    }
    else
    {
        printf("Invalid rating\n");
        printf("Please try again\n");
    }

    return 0;
}

int main(void){

    char firstname[10];
    char lastname[10];
    int age;
    char dest[20];

    int confirm = 0;
    printf("-------------------------------------------------------------\n");
    printf("Welcome to the Ticketing Service of Dhanbad Railway Station\n");
    printf("-------------------------------------------------------------\n");
    printf("Please fill up your details below:\n");

    printf("First Name: ");
    scanf("%s", &firstname);

    printf("Last Name: ");
    scanf("%s", &lastname);

    printf("Age: ");
    scanf("%d", &age);

    printf("Please select the destination you want to travel to: \n");
    printf("Delhi\n");
    printf("Mumbai\n");
    printf("Kolkata\n");
    printf("Chennai\n");
    printf("Bangalore\n");
    scanf("%s", &dest);

    printf("-------------------------------------------------------------\n");
    printf("Would you like to confirm the details? (1/0): ");
    scanf("%d", &confirm);

    if (confirm > 1 || confirm < 0)
    {
        printf("Please fill up the details again\n");
        confirm = 0;
        exit(0);
    }

    printf("-------------------------------------------------------------\n");
    printf("Thank you for confirming the details\n");
    printf("-------------------------------------------------------------\n");

    printf("Your ticket has been booked successfully\n");
    printf("Your ticket details are as follows:\n");
    printf("First Name: %s                   Last Name %s \n", firstname, lastname, age);
    printf("Origin: Dhanbad            Destination: %s\n", dest);
    printf("-------------------------------------------------------------\n");

    printf("Thank you for visiting Dhanbad\n");
    printf("Please give us a review based on your experience\n");
    review();
}
