#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
string minLexRotation(string str)
{
    int n = str.length();
    vector<string> arr;
    string concat = str + str;
    for (int i = 0; i < n; i++)
        arr.push_back(concat.substr(i, n));
    sort(arr.begin(), arr.end());
    return arr[0];
}
int main() {
    char ls[100000];
    int p=0;
    string s;
    cin>>s;
    int n,x,i,j,l;
    char ch;
    cin>>n;
    for(int abcd=0; abcd<n; abcd++) {
        cin>>x;
        cin>>i;
        if (x) {
            std::string minst;
            std::cin>>j;
            std::cin>>l;
            string subbuff;
            subbuff = s.substr(i-1,j-i+1);
            minst = minLexRotation(std::string(subbuff));
            ls[p++] = minst[l-1];
        }
        else {
            std::cin>>ch;
            s[i-1] = ch;
        }
    }    
    for(i=0; i<p; i++)
        cout<<ls[i]<<endl;
    return 0;
}