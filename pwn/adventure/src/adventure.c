#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void gadget_setup() {
  asm volatile ("pop %%rdi\n\t"
      "ret"
      :
      :
      : "rdi");
}

void hatchEgg(void)
{
    char name[20];

    printf("You wish to hatch the egg!\n");
    printf("Give the baby dragon a name\n");
    getchar();
    fflush(stdin);
    gets(name);

    printf("Your dragon is now called %s\n", name);
    printf("You leave the area with %s\n", name);

}
void exploreLeft()
{
    int choice;
    printf("You chose to go left.\n");
    printf("You encounter a fork in the road.\n");
    printf("Do you go uphill or downhill?\n");
    printf("1. Uphill\n");
    printf("2. Downhill\n");

    printf("Enter your choice: ");
    scanf("%d", &choice);

    if (choice == 1)
    {
        printf("You chose to go uphill.\n");
        printf("You stumble upon a hidden cave.\n");
        printf("What do you do?\n");
        printf("1. Enter the cave\n");
        printf("2. Ignore the cave and keep walking\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice == 1)
        {
            printf("You enter the cave and find a chest filled with gold!\n");
            printf("Congratulations, you're rich!\n");
        }
        else if (choice == 2)
        {
            printf("You ignore the cave and continue walking.\n");
            printf("You encounter a band of thieves who rob you of all your possessions!\n");
        }
        else
        {
            printf("Invalid choice.\n");
        }
    }
    else if (choice == 2)
    {
        printf("You chose to go downhill.\n");
        printf("You find yourself in a dense forest.\n");
        printf("Do you continue through the forest or turn back?\n");
        printf("1. Continue through the forest\n");
        printf("2. Turn back\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice == 1)
        {
            printf("You continue through the forest and encounter a mystical fairy who grants you three wishes!\n");
            printf("What do you wish for?\n");
            printf("1. Wealth\n");
            printf("2. Power\n");
            printf("3. Wisdom\n");

            printf("Enter your choice: ");
            scanf("%d", &choice);

            switch (choice)
            {
            case 1:
                printf("You wish for wealth and suddenly find yourself surrounded by piles of gold!\n");
                printf("Congratulations, you're rich!\n");
                break;
            case 2:
                printf("You wish for power and become the ruler of a vast kingdom!\n");
                printf("But power comes with its own challenges...\n");
                break;
            case 3:
                printf("You wish for wisdom and gain unparalleled knowledge!\n");
                printf("You become a respected scholar and advisor to kings.\n");
                break;
            default:
                printf("Invalid choice.\n");
            }
        }
        else if (choice == 2)
        {
            printf("You turn back and head home.\n");
            printf("Your adventure ends here, but at least you're safe.\n");
        }
        else
        {
            printf("Invalid choice.\n");
        }
    }
    else
    {
        printf("Invalid choice.\n");
    }
}

void exploreRight()
{
    int choice;

    printf("You chose to go right.\n");
    printf("You find a hidden treasure chest!\n");
    printf("This treasure chest contains a dragon egg!\n");
    
    printf("Do you want to hatch it?\n");
    printf("1. Yes\n");
    printf("2. No\n");
    scanf("%d", &choice);

    if (choice == 1)
    {
        hatchEgg();
    }
    else if (choice == 2)
    {
        printf("You do not wish to hatch the egg!\n");
        printf("You leave the treasure chest......\n");
        
        printf("You get transported out by a mysterious power.\n");
        exit(0);
    }
    else
    {
        printf("Invalid choice.\n");
    }
}

void stayWhereYouAre()
{
    int choice;
    printf("You chose to stay where you are.\n");
    printf("Suddenly, a portal appears in front of you!\n");
    printf("Do you enter the portal?\n");
    printf("1. Yes\n");
    printf("2. No\n");

    printf("Enter your choice: ");
    scanf("%d", &choice);

    if (choice == 1)
    {
        printf("You enter the portal and find yourself in another dimension!\n");
        printf("Who knows what adventures await you here...\n");
    }
    else if (choice == 2)
    {
        printf("You decide not to risk it and stay where you are.\n");
        printf("You live out the rest of your days in peace and tranquility.\n");
    }
    else
    {
        printf("Invalid choice.\n");
    }
    exit(0);
}

int main()
{
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);
    
    int choice;

    printf("Welcome to the Adventure!\n");
    printf("You find yourself standing at a crossroad.\n");
    printf("What do you do?\n");
    printf("1. Go left\n");
    printf("2. Go right\n");
    printf("3. Stay where you are\n");

    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice)
    {
    case 1:
        exploreLeft();
        break;
    case 2:
        exploreRight();
        break;
    case 3:
        stayWhereYouAre();
        break;
    default:
        printf("Invalid choice.\n");
    }

    return 0;
}

