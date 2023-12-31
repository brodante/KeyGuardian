#include <bits/stdc++.h>
#include <conio.h>
#include "hash_id.cpp"
//#include  "../../cryptopp/md5.h"
//#include  "../../cryptopp/sha.h"
#define wait cout<<"\nPress Enter to continue...";cin.ignore();cin.get();
//#include <cstdlib> // For system("cls") to clear the screen
using namespace std;
// ANSI color codes for text color
const string COLOR_RESET = "\x1B[0m";
const string COLOR_GREEN = "\x1B[32m";
const string COLOR_CYAN = "\x1B[36m";
const string COLOR_YELLOW = "\x1B[33m";
const string COLOR_RED = "\x1B[31m";
// Function to perform hash identification
void logo()
{
  system("cls");

  //cout << "\n\n";
  cout << COLOR_CYAN <<setw(50)<<"KeyGuardian v0.02" << COLOR_RESET << "\n";
  cout << COLOR_GREEN << R"(
  _  __           _____                     _ _                      ___   ___ ___    _          _
 | |/ /          / ____|                   | (_)                    / _ \ / _ \__ \  | |        | |
 | ' / ___ _   _| |  __ _   _  __ _ _ __ __| |_  __ _ _ __   __   _| | | | | | | ) | | |__   ___| |_ __ _
 |  < / _ \ | | | | |_ | | | |/ _` | '__/ _` | |/ _` | '_ \  \ \ / / | | | | | |/ /  | '_ \ / _ \ __/ _` |
 | . \  __/ |_| | |__| | |_| | (_| | | | (_| | | (_| | | | |  \ V /| |_| | |_| / /_  | |_) |  __/ || (_| |
 |_|\_\___|\__, |\_____|\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|   \_/  \___(_)___/____| |_.__/ \___|\__\__,_|
            __/ |
           |___/
)" << COLOR_RESET << endl;

}
void identifyHash()
{
    cout << COLOR_CYAN;
    hash_id();
    cout<<COLOR_RESET;
    getch();
    // Implement your hash identification logic here
    //cout << COLOR_CYAN << "Hash identification function\n" << COLOR_RESET;
}

// Function to perform encryption
void performEncryption()
{
    // Implement your encryption logic here
    cout << COLOR_CYAN << "Encryption function\n" << COLOR_RESET;
}

// Function to perform decryption
void performDecryption()
{
    // Implement your decryption logic here
    cout << COLOR_CYAN << "Decryption function\n" << COLOR_RESET;
}

// Function to attempt force decryption
void attemptForceDecryption()
{
    // Implement your force decryption logic here
    cout << COLOR_CYAN << "Force decryption function\n" << COLOR_RESET;
}

int main()
{
    // Clear the screen for better readability
    logo();
    int choice;
    do {
        system("cls");
        logo();
        cout << COLOR_YELLOW << "\n1. Hash Identification\n";
        cout << "2. Encryption\n";
        cout << "3. Decryption\n";
        cout << "4. Attempt Force Decryption\n";
        cout << "5. Exit" << COLOR_RESET << "\n";
        cout << "\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
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
                cout << COLOR_RED << "Exiting...\n" << COLOR_RESET;
                break;
            default:
                cout << COLOR_RED << "Invalid choice! Please select a valid option.\n" << COLOR_RESET;
                wait
        }
    }while(choice!=5);

    return 0;
}
