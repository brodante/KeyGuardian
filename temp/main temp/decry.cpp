#define CRYPTOPP_ENABLE_NAMESPACE_WEAK 1
#include <iostream>
#include <string>
#include  "../../cryptopp/cryptlib.h"
#include  "../../cryptopp/md5.h"
#include  "../../cryptopp/sha.h"
#include  "../../cryptopp/sha3.h"
#include  "../../cryptopp/ripemd.h"
#include  "../../cryptopp/whrlpool.h"
#include  "../../cryptopp/hex.h"
#include  "../../cryptopp/filters.h"

using namespace std;
using namespace CryptoPP;
using namespace CryptoPP::Weak;

string identifyHash(const string &hash) {
    try {
        // SHA-256
         CryptoPP::SHA256 sha256;
        string sha256Hash;
        StringSource(hash, true, new HexDecoder(new StringSink(sha256Hash)));
        if (sha256Hash.length() == sha256.DigestSize()) {
            return "SHA-256";
        }

        // MD5
        MD5 md5;
        string md5Hash;
        StringSource(hash, true, new HexDecoder(new StringSink(md5Hash)));
        if (md5Hash.length() == md5.DigestSize()) {
            return "MD5";
        }

        // RIPEMD-160
        RIPEMD160 ripemd160;
        string ripemd160Hash;
        StringSource(hash, true, new HexDecoder(new StringSink(ripemd160Hash)));
        if (ripemd160Hash.length() == ripemd160.DigestSize()) {
            return "RIPEMD-160";
        }

        // Whirlpool
        Whirlpool whirlpool;
        string whirlpoolHash;
        StringSource(hash, true, new HexDecoder(new StringSink(whirlpoolHash)));
        if (whirlpoolHash.length() == whirlpool.DigestSize()) {
            return "Whirlpool";
        }

        // Add more hash types here...

        // If none of the above matches, it's unidentified
        return "Unidentified";
    } catch (const Exception &ex) {
        cerr << "Crypto++ error: " << ex.what() << endl;
        return "Error";
    }
}

int main() {
    string inputHash;
    cout << "Enter a hash in hexadecimal format: ";
    cin >> inputHash;

    string hashType = identifyHash(inputHash);
    cout << "Hash identified as: " << hashType << endl;

    return 0;
}
