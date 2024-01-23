#include "bits/stdc++.h"

using namespace std;

void solution(){
    int n, k;
    cin >> n >> k;
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    map<int, int> count;
    for(int i = 0; i < n; i++){
        count[a[i]]++;
    }
    vector<int> m;
    for(auto x : count){
        m.push_back(x.first);
    }
    int ansl = 0, ansr = 0;
    int l = 0, r = 0;
    int _max = 0;
    while(r < m.size()){
        if(count[m[r]] >= k){
            if(m[r] - m[l] >= _max){
                _max = m[r] - m[l];
                ansl = m[l];
                ansr = m[r];
            }
        }else{
            l = r+1;
            r++;
            continue;
        }
        
        
        if(r < m.size() - 1 && m[r] + 1 == m[r + 1]){
            r++;
        }else{
            l = r+1;
            r++;
        }
    }

    if (ansl == 0 && ansr == 0){
        cout << -1 << endl;
        return;
    }

    cout << ansl << " " << ansr << endl;

}
int main(){
    int t;
    cin >> t;
    while(t--){
        solution();
    }
    return 0;
}