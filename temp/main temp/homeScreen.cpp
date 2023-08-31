#include <iostream>
#include <string>
#include <cstdlib> // For system("cls") to clear the screen

using namespace std;

// ANSI color codes for text color
const string COLOR_RESET = "\x1B[0m";
const string COLOR_GREEN = "\x1B[32m";
const string COLOR_CYAN = "\x1B[36m";
const string COLOR_YELLOW = "\x1B[33m";
const string COLOR_RED = "\x1B[31m";

// Function to perform hash identification
void identifyHash() {
    // Implement your hash identification logic here
    cout << COLOR_CYAN << "Hash identification function\n" << COLOR_RESET;
}

// Function to perform encryption
void performEncryption() {
    // Implement your encryption logic here
    cout << COLOR_CYAN << "Encryption function\n" << COLOR_RESET;
}

// Function to perform decryption
void performDecryption() {
    // Implement your decryption logic here
    cout << COLOR_CYAN << "Decryption function\n" << COLOR_RESET;
}

// Function to attempt force decryption
void attemptForceDecryption() {
    // Implement your force decryption logic here
    cout << COLOR_CYAN << "Force decryption function\n" << COLOR_RESET;
}

int main() {
    // Clear the screen for better readability
    system("cls");

    cout << "\n\n";
    cout << COLOR_GREEN << "                       Data Encryption/Decryption Software v1.00                     " << COLOR_RESET << "\n";
    cout << COLOR_GREEN << R"(
   _  __           _____                     _ _                    __   ___   ___  
  | |/ /          / ____|                   | (_)                  /_ | / _ \ / _ \ 
  | ' / ___ _   _| |  __ _   _  __ _ _ __ __| |_  __ _ _ __   __   _| || | | | | | |
  |  < / _ \ | | | | |_ | | | |/ _` | '__/ _` | |/ _` | '_ \  \ \ / / || | | | | | |
  | . \  __/ |_| | |__| | |_| | (_| | | | (_| | | (_| | | | |  \ V /| || |_| | |_| |
  |_|\_\___|\__, |\_____|\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|   \_/ |_(_)___/ \___/ 
            __/ |                                                                  
           |___/                                                                   
    )" << COLOR_RESET << endl;

    int choice;
    
    do {
        cout << COLOR_YELLOW << "\n1. Hash Identification\n";
        cout << "2. Encryption\n";
        cout << "3. Decryption\n";
        cout << "4. Attempt Force Decryption\n";
        cout << "5. Exit" << COLOR_RESET << "\n";
        cout << "\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                identifyHash();
                break;
            case 2:
                performEncryption();
                break;
            case 3:
                performDecryption();
                break;
            case 4:
                attemptForceDecryption();
                break;
            case 5:
                cout << COLOR_CYAN << "Exiting...\n" << COLOR_RESET;
                break;
            default:
                cout << COLOR_RED << "Invalid choice! Please select a valid option.\n" << COLOR_RESET;
        }
        
        // Wait for user input before clearing the screen
        cout << "\nPress Enter to continue...";
        cin.ignore();
        cin.get();
        
    } while (choice != 5);
    
    return 0;
}
