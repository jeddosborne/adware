#include <stdio.h>
#include <stdlib.h>

void executeCommand(const char* command) {
    // Use the system() function to execute the command
    int result = system(command);

    if (result == 0) {
        printf("Command executed successfully\n");
    } else {
        printf("Error executing the command\n");
    }
}

int main() {
    executeCommand("python main.py");

    return 0;
}
