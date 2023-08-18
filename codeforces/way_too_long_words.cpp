#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin>>t;
    string word;
    char st, end;
    while (t--){
        cin>>word;
        if(word.length() > 10){
            st = word[0];
            end = word[word.length()-1];
            cout<<st<<word.length()-2<<end<<endl;
        }else{
            cout<<word<<endl;
        }
    }
}