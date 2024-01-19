#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Expected 1 argument, got %d\n", argc - 1);
        return 1;
    }

    char *file_path = argv[1];
    FILE *file = fopen(file_path, "r");

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    char line[100];
    while (fgets(line, sizeof(line), file) != NULL) {
        long long number = atoll(line);
        for (long long i = 2; i < number; ++i) {
            if (number % i == 0) {
                printf("%lld=%lld*%lld\n", number, number / i, i);
                break;
            }
        }
    }

    fclose(file);
    return 0;
}
