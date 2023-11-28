#include "bits/stdc++.h"

using namespace std;

int main()
{
    int n, k, q, l, r, maximum, minimum;
    maximum = 0;
    minimum = 200009;
    cin >> n >> k >> q;
    vector<int> a(200009, 0);
    for (int i = 0; i < n; i++)
    {
        cin >> l >> r;
        a[l]++;
        a[r + 1]--;
    }

    for (int i = 1; i < a.size(); i++)
    {
        a[i] = a[i] + a[i - 1];
    }

    for (int i = 1; i < a.size(); i++)
    {
        if (a[i] >= k)
        {
            a[i] = 1;
        }
        else
        {
            a[i] = 0;
        }
    }

    for (int i = 1; i < a.size(); i++)
    {
        a[i] = a[i] + a[i - 1];
    }
    int c, b;
    for (int i = 0; i < q; i++)
    {
        cin >> c >> b;
        if (b > 0)
        {
            cout << a[b] - a[c - 1] << "\n";
        }
        else
        {
            cout << a[b] << "\n";
        }
    }

    return 0;
}