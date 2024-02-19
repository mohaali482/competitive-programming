#pragma GCC optimize("O3", "unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,popcnt,lzcnt")
#include "bits/stdc++.h"
using namespace std;

int a[200000];

int main()
{
    int t = 0;
    cin >> t;
    int n, x, y, ans;
    while (t--)
    {
        ans = 0;
        cin >> n >> x >> y;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if ((a[i] + a[j]) % x == 0 && (a[i] - a[j]) % y == 0)
                {
                    ans++;
                }
            }
        }
        cout << ans << "\n";
    }
    return 0;
}