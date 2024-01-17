#include "bits/stdc++.h"
#define ll long long

using namespace std;

ll prefix_sum[1000000];
int main()
{
    prefix_sum[0] = 1;
    ll s = 1;
    for (ll i = 2; i < 1000001; i++)
    {
        prefix_sum[s] = prefix_sum[s - 1] + (i * i);
        s++;
    }
    ll t;
    cin >> t;
    ll n;
    while (t--)
    {
        cin >> n;
        cout << prefix_sum[((ll)pow(n, 0.5)) - 1] << "\n";
    }
    return 0;
}