#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#include <string.h>

#define MAX_NOTES 0x10
#define NOTE_SIZE 0x200

void buffer_init()
{
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
}

char *notes[MAX_NOTES];

uint64_t get_number() {
  char buf[16];
  printf("> ");
  fgets(buf, sizeof(buf), stdin);
  return strtoull(buf, NULL, 10);
}

void create_note()
{
    char buffer[NOTE_SIZE];

    uint64_t index,malloc_size=0;
    printf("Note Index ");
    index=get_number();

    if (index >= MAX_NOTES || index < 0)
    {
        printf("Thats an invalid index.\n");
        exit(1);
    }
    printf("Note Size ");

    malloc_size=get_number();
    if (malloc_size > NOTE_SIZE)
    {
        printf("Thats too long for a single Note!!!");
        exit(1);
    }

    void *buf = malloc(malloc_size);
    if (!buf)
    {
        printf("Failed to malloc. Assuming fatal error.\n");
        exit(1);
    }
    notes[index] = buf;
    printf("Note Content > ");

    fgets(notes[index], malloc_size, stdin);
    // printf("Note added.\n");
}

void delete_note()
{
    uint64_t index;
    printf("Note Index ");
    index=get_number();

    if (index < 0 || index >= MAX_NOTES)
    {
        printf("Invalid note index.\n");
        return;
    }

    free(notes[index]);


/*VULN*/
    // notes[index] = NULL;
/*VULN*/

    printf("Note deleted.\n");
}

void view_note()
{
    uint64_t index;
    printf("Note Index ");
    index=get_number();

    if (index < 0 || index >= MAX_NOTES)
    {
        printf("Invalid note index.\n");
        return;
    }
    puts(notes[index]);
}

int main()
{
    buffer_init();
    uint64_t choice;

    while (1)
    {
        printf("\n1. Create note\n2. Delete note\n3. View notes\n4. Exit\n");
        printf("Enter choice ");
        choice=get_number();
        // getchar(); // consume newline

        switch (choice)
        {
        case 1:
            create_note();
            break;
        case 2:
            delete_note();
            break;
        case 3:
            view_note();
            break;
        case 4:
            exit(0);
        default:
            printf("Why would you do that.\n");
            break;
        }
    }

    return 0;
}
 