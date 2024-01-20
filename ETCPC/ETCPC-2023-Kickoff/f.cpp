#include "bits/stdc++.h"
#define ll long long
using namespace std;

int prime_factor_size(ll n)
{
    ll prime_factors = 0;
    ll num;
    for (int i = 1; i <= (int)pow(n, 0.5); i++)
    {
        if (n % i == 0)
        {
            prime_factors++;
            num = i;
        }
    }
    prime_factors *= 2;
    if (num * num == n)
    {
        prime_factors--;
    }
    return prime_factors;
}

int main()
{
    ll n, k;
    cin >> n >> k;
    ll a[n + 1];
    for (ll i = 0; i < n + 1; i++)
    {
        a[i] = 0;
    }
    ll x;
    for (ll i = 0; i < k; i++)
    {
        cin >> x;
        a[x] = 1;
    }
    for (ll i = 1; i < n + 1; i++)
    {
        for (auto x : a)
        {
            cout << x << " ";
        }
        cout << endl;
        if (prime_factor_size(i) % 2 != 0)
        {
            if (a[i] == 1)
            {
                a[i] = 0;
            }
            else
            {
                a[i] = 1;
            }
        }
    }
    ll sum = 0;
    for (ll i = 1; i < n + 1; i++)
    {
        sum += a[i];
    }
    cout << sum;
    return 0;
}
