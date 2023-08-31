#include <bits/stdc++.h>
using namespace std;
unordered_map<string, string> hashTypes = {
  {"MD5", "^[a-fA-F0-9]{32}$"},
  {"SHA-1", "^[a-fA-F0-9]{40}$"},
  {"SHA-256", "^[a-fA-F0-9]{64}$"},
  {"SHA512", "^\\$[0-9]+\\$[a-zA-Z0-9./]+\\$[a-zA-Z0-9./]+$"},
  {"CRC32", "^[a-fA-F0-9]{8}$"},
  {"LM", "^[0-9A-F]{32}:[0-9A-F]{32}$"},
  {"NTLM", "^\\$NT\\$[a-fA-F0-9]{32}$"},
  {"MySQL323", "^[0-9A-F]{16}$"},
  {"PostgreSQL", "^[0-9A-F]{32}$"},
  {"Cisco PIX", "^[0-9A-F]{16}$"},
  {"RipeMD-160", "^[a-fA-F0-9]{40}$"},
  {"Haval-128", "^[a-fA-F0-9]{32}$"},
  {"MD4", "^[a-fA-F0-9]{32}$"},
  {"GOST R 34.11-94", "^[a-fA-F0-9]{64}$"},
  {"Whirlpool", "^[a-fA-F0-9]{128}$"},
  {"CRC16-CCITT", "^[a-fA-F0-9]{4}$"},
};

vector<string> identifyHash(const string& hash)
{
    vector<string> possibleTypes;
    for (const auto& entry : hashTypes)
    {
        regex pattern(entry.second);
        if (regex_match(hash, pattern))
            possibleTypes.push_back(entry.first);
    }
    return possibleTypes;
}

int main()
{
    string inputHash;
    cout<<"Enter hash: ";
    cin>>inputHash;
    vector<string>possibleTypes=identifyHash(inputHash);
    if(possibleTypes.empty())
        cout<<"Unidentified hash\n";
    else if(possibleTypes.size()==1)
        cout<<"Hash identified as: " <<possibleTypes[0]<<'\n';
    else
    {
        cout << "Hash can be from any of the following types:\n";
        for(const auto& type : possibleTypes)
            cout << "- " << type << '\n';
    }
    return 0;
}
