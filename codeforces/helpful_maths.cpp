#include<bits/stdc++.h>

using namespace std;

int main(){
    vector<string> nums;
    string input, word="";
    cin>>input;
    for (int i=0; i<input.length(); ++i){
        if (input[i] == '+'){
            nums.push_back(word);
            word = "";
            continue;
        }
        word += input[i];
    }

    if (word.length() > 0){
        nums.push_back(word);
    }

    sort(nums.begin(), nums.end());
    string output="";
    for (int i=0; i < nums.size(); ++i){
        output += nums[i];
        if (i+1 < nums.size()){
            output += "+";
        }
    }

    cout<<output;
    
}