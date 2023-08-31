#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <openssl/md5.h>
#include <iomanip>

using namespace std;

string md5Hash(const string &input) {
    unsigned char hash[MD5_DIGEST_LENGTH];
    MD5(reinterpret_cast<const unsigned char*>(input.c_str()), input.size(), hash);

    stringstream ss;
    for (unsigned char c : hash) {
        ss << hex << setw(2) << setfill('0') << static_cast<int>(c);
    }
    return ss.str();
}

int main() {
    string filename;
    string targetHash;

    cout << "Enter the filename of the wordlist (e.g., rockyou.txt): ";
    cin >> filename;

    cout << "Enter the target MD5 hash: ";
    cin >> targetHash;

    ifstream wordlistFile(filename);
    if (!wordlistFile.is_open()) {
        cout << "Error opening the wordlist file." << endl;
        return 1;
    }

    string word;
    while (wordlistFile >> word) {
        string hashedWord = md5Hash(word);
        if (hashedWord == targetHash) {
            cout << "Password found: " << word << endl;
            wordlistFile.close();
            return 0;
        }
    }

    cout << "Password not found in the wordlist." << endl;
    wordlistFile.close();
    return 0;
}
