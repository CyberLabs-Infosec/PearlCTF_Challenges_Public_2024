#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define NAME_SIZE 32
#define MAX_HEROES 3

struct hero {
    unsigned long attack;
    unsigned long defence;
    char name[NAME_SIZE];
};

typedef struct hero hero;

int main()
{
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);

    int length = MAX_HEROES, curr_length = 0;
    hero *heroes[length];

    hero example_hero = {0};
    example_hero.attack = 0;
    example_hero.defence = 0;

    strcpy(example_hero.name, "Kratos");

    printf("---- Welcome to The Battle Game! ----\n\n");
    

    hero *temp_hero = NULL;
    unsigned long attack = 0, defence = 0;

    while(1){
        int choice;

        printf("1. Add a new hero\n2. View heroes\n3. Edit a hero\n4. Delete a hero\n5. See Example\n6. Exit\nEnter choice: ");
        scanf("%d", &choice);

        if(choice == 1){
            if(curr_length == length){
                printf("\nHero list full, cannot add new hero.\n\n");
            }
            else{
                temp_hero = (hero*) malloc(sizeof(hero));

                printf("\nEnter hero's name: ");
                getchar();
                fflush(stdin);
                if(fgets(temp_hero->name, sizeof(temp_hero->name), stdin) != NULL)
                    temp_hero->name[strcspn(temp_hero->name, "\n")] = '\0';
                printf("Enter attack: ");
                scanf(" %lu", &(temp_hero->attack));
                printf("Enter defence: ");
                scanf(" %lu", &(temp_hero->defence));

                heroes[curr_length] = temp_hero;

                curr_length++;

                printf("Successfully added your hero\n\n");
            }
        }
        else if(choice == 2){
            printf("\n----\n");
            if(curr_length == 0){
                printf("No heroes to show!\n");
                printf("----\n");
            }
            else{
                for(int i=0; i<curr_length; i++){
                    printf("Hero %d: %s\n", i, (char*)heroes[i]->name);
                    printf("Attack: %ld\n", heroes[i]->attack);
                    printf("Defence: %ld\n", heroes[i]->defence);
                    printf("----\n");
                }
            }
            printf("\n");
        }
        else if(choice == 3){
            int idx;
            unsigned long attack, defence;
            char name[32];

            printf("\n");

            printf("Enter the index of the hero: ");
            scanf("%d", &idx);

            if(curr_length == 0 || idx >= curr_length){
                printf("\nSorry, that hero does not exist!\n\n");
                continue;
            }

            if((int)idx >= (int)0 || (unsigned long long)idx < (unsigned long long)curr_length){
                temp_hero = heroes[idx];
            }

            printf("\nEnter hero's name: ");
            getchar();
            fflush(stdin);
            if(fgets(temp_hero->name, sizeof(temp_hero->name), stdin) != NULL)
                temp_hero->name[strcspn(temp_hero->name, "\n")] = '\0';
            printf("Enter attack: ");
            scanf(" %lu", &(temp_hero->attack));
            printf("Enter defence: ");
            scanf(" %lu", &(temp_hero->defence));

            printf("Successfully edited your hero\n");
            printf("\n");
        }
        else if(choice == 4){
            int idx;

            printf("\n");

            printf("Enter the index of the hero: ");
            scanf("%d", &idx);

            if(curr_length == 0 || idx >= curr_length){
                printf("\nSorry, that hero does not exist!\n\n");
                continue;
            }

            if((int)idx >= (int)0 || (unsigned long long)idx < (unsigned long long)curr_length){
                temp_hero = heroes[idx];
            }

            for(int i=idx; i<curr_length-1; i++){
                heroes[i] = heroes[i+1];
            }
            curr_length--;

            free(temp_hero);
            temp_hero = &example_hero;

            printf("Successfully deleted your hero\n");
            printf("\n");
        }
        else if(choice == 5){
            temp_hero = (hero*) &example_hero.name;
            attack = example_hero.attack;
            defence = example_hero.defence;

            printf("\n----\n");
            printf("Hero %d: %s\n", 1337, (char*)temp_hero);
            printf("Attack: %ld\n", attack);
            printf("Defence: %ld\n", defence);  
            printf("----\n\n");
        }
        else{
            break;
        }
    }

    int final_attack = 0, final_defence = 0;
    for(int i=0; i<curr_length; i++){
        final_attack += heroes[i]->attack;
        final_defence += heroes[i]->defence;
    }

    printf("\nFinal Attack and Defence power of your heroes:\n");
    printf("Attack: %d, Defence: %d\n\n", final_attack, final_defence);

    char *opponent_name = (char*)malloc(0x100);
    int opponent_attack = 65007, opponent_defence = 56440;

    printf("Enter opponent's name: ");
    getchar();
    fgets(opponent_name, 0x100, stdin);

    if(final_attack > opponent_attack && final_defence > opponent_defence){
        printf("\nYou win!\n");
    }
    else{
        printf("\nYou lose!\n");
    }

    return 0;
}