#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

char *read_flag()
{
    FILE *file;
    char *c;
    long file_size;

    file = fopen("flag.txt", "rb");
    if(file == NULL){
        perror("Error opening file");
        return '\0';
    }
    
    c = (char*) malloc(128);

    if(c == NULL){
        fclose(file);
        perror("Error allocating memory");
        return '\0';
    }

    fseek(file, 0, SEEK_END);
    file_size = ftell(file);
    rewind(file);

    if(fread(c, 1, file_size, file) != file_size){
        fclose(file);
        free(c);
        perror("Error reading file");
        return '\0';
    }

    c[file_size] = '\0';
    fclose(file);

    return c;
}

int check_xor_value(int val){
    if(val > 5000)
        return 1;
    else if(val < 0)
        return 2;
    else if(val%2)
        return 3;
    return 0;
}

void xor_array(int *array, int length)
{
    int val, idx;
    printf("Enter the number to xor with: ");
    scanf(" %d", &val);

    int check = check_xor_value(val);
    if(check != 0){
        free(array);
        if(check == 1){
            printf("The value must be less than or equal to 5000");
            return;
        }
        else if(check == 2){
            printf("The value must be zero or positive");
            return;
        }
        else{
            printf("The value must be even");
            return;
        }
    }

    printf("Enter the index of the element: ");
    scanf(" %d", &idx);

    if(idx >= 0 && idx < length){
        array[idx] = array[idx] ^ val;
    }
    else{
        free(array);
        printf("Array index out of range\n");
        exit(0);
    }
}

struct return_object{
    int *password;
    int check;
};

struct return_object check_password(int *password, int *array, int length){
    int idx, check = 1;
    srand((unsigned int)time(NULL));
    printf("You can skip checking any one index of the array for the password\n");
    printf("Enter the index: ");
    scanf(" %d", &idx);

    for(int i=0; i<length; i++){
        if(i != idx){
            password[i] = 5;
        }
    }

    for(int i=0; i<length; i++){
        if(password[i] ^ array[i] != 0x1337){
            check = 0;
            break;
        }
    }

    struct return_object obj;
    obj.password = (int*)malloc(length * sizeof(int));
    memcpy(obj.password, password, length * sizeof(int));
    obj.check = check;

    return obj;
}

void vuln()
{
    int length = 32, choice, second_choice;
    int *array = (int*)malloc(length * sizeof(int));

    printf("Enter the initial array of size %d: ", length);
    for(int i=0; i<length; i++){
        scanf(" %d", &array[i]);
    }

    printf("You can xor any 4 elements of the array with a number\n");
    for(int i=0; i<4; i++){
        xor_array(array, length);
    }

    int *password = (int*)malloc(length * sizeof(int));
    char *flag = read_flag();
    struct return_object obj = check_password(password, array, length);

    if(obj.check){
        printf("Congrats! Here's your flag: %s", flag);
    }
    else{
        printf("Sorry, wrong password\n");
        printf("The password was: \n");
        for(int i=0; i<length; i++){
            printf("%d ", obj.password[i]);
        }
        printf("\n");
    }

}

int main()
{
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);
    vuln();
    return 0;
}