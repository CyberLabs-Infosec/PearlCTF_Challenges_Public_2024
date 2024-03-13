#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>

int main() {
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);
    unsigned long secret_sauce_address, guess;
    int choice, max_attempts, attempts;
    int secretGamePlayed = 0;
    int makeYourOwnSaucePlayed = 0;
    int eliteness = 0;

    printf("Welcome to the Sauce Adventure!\n");

    do {
        printf("\nMenu:\n");
        printf("1. The Sauce Guessing Game\n");
        printf("2. Make Your Own Sauce\n");
        printf("3. Check Your Eliteness\n");
        printf("4. Exit\n");
        printf("Enter your choice (1-4): ");

        if (scanf("%d", &choice) != 1) {
            printf("Invalid input. Please enter a valid integer.\n");
            while (getchar() != '\n');
            continue;
        }

        switch (choice) {
            case 1:
                if (secretGamePlayed) {
                    printf("You've already played the secret sauce guessing game. Try making your own sauce!\n");
                    break;
                }

                secret_sauce_address = (unsigned long)&main;
                max_attempts = 100;
                attempts = 0;

                printf("You have stumbled upon a mysterious kitchen with a secret sauce. Try to guess its unique flavor.\n");
                printf("You have %d attempts!\n", max_attempts);

                while (attempts < max_attempts) {
                    printf("Enter your sauce recipe: ");
                    if (scanf("%lu", &guess) != 1) {
                        printf("Invalid sauce!\n");
                        while (getchar() != '\n');
                        continue;
                    }

                    attempts++;

                    if (guess < secret_sauce_address) {
                        printf("Oh no! Your sauce is bland!\n");
                    } else if (guess > secret_sauce_address) {
                        printf("Whoa! Your sauce is overdone!\n");
                    } else {
                        printf("Congratulations! You got it right. Your sauce is perfectly balanced and extraordinary!\n");
                        break;
                    }
                }
                secretGamePlayed = 1;
                if (attempts == max_attempts) {
                    printf("Sorry, you've reached the maximum number of attempts. Your sauce remains a mystery.\n");
                }
                break;

            case 2:
                if (makeYourOwnSaucePlayed) {
                    printf("You've already made your own sauce. Try something else!\n");
                    break;
                }

                printf("Welcome to the 'Make Your Own Sauce' station!\n");
                printf("Feel free to experiment with various ingredients to create your unique sauce.\n");

                char* secretSauce = NULL;
                int ingredientIndex;
                char operation;

                printf("Enter an existing sauce that you want to experiment with: ");
                if (scanf("%p", (void**)&secretSauce) != 1) {
                    printf("Invalid sauce!\n");
                    continue;
                }

                printf("Choose an ingredient: ");
                if (scanf("%d", &ingredientIndex) != 1 || ingredientIndex < 0 || ingredientIndex > 7) {
                    printf("What ingredient is that?!\n");
                    continue;
                }

                printf("Do you want to add or remove the ingredient ('a' to add, 'r' to remove): ");
                if (scanf(" %c", &operation) != 1) {
                    printf("Invalid operation!\n");
                    continue;
                }

                if (operation == 'a') {
                    if (secretSauce != NULL) {
                        *secretSauce = (*secretSauce | (1 << ingredientIndex)) & (*secretSauce | (1 << ingredientIndex));
                        printf("Ingredient added successfully.\n");
                    } else {
                        printf("The sauce blew up!\n");
                        continue;
                    }
                } else if (operation == 'r') {
                    if (secretSauce != NULL) {
                        *secretSauce = (*secretSauce & ~(1 << ingredientIndex)) | (*secretSauce & ~(1 << ingredientIndex));
                        printf("Ingredient removed successfully.\n");
                    } else {
                        printf("The sauce blew up!\n");
                        continue;
                    }
                } else {
                    printf("What did you just do?!\n");
                    continue;
                }

                makeYourOwnSaucePlayed = 1;
                break;

            case 3:
                if (eliteness == 1337) {
                    FILE *file;
                    char *content;
                    long fileSize;

                    file = fopen("flag.txt", "r");

                    if (file == NULL) {
                        perror("Error opening file");
                        continue;
                    }

                    fseek(file, 0, SEEK_END);
                    fileSize = ftell(file);
                    fseek(file, 0, SEEK_SET);

                    content = (char *)malloc(fileSize + 1);

                    if (content == NULL) {
                        perror("Error allocating memory");
                        fclose(file);
                        return 2;
                    }

                    fread(content, 1, fileSize, file);

                    content[fileSize] = '\0';
                    printf("%s", content);
                    free(content);
                    fclose(file);
                } else {
                    printf("You're not elite enough to access this feature!\n");
                }
                break;

            case 4:
                printf("Goodbye! Thanks for playing with sauces.\n");
                break;

            default:
                printf("Invalid choice. Please enter a number between 1 and 4.\n");
        }
    } while (choice != 4);

    return 0;
}

