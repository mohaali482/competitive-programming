#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    vector<int> v(t);
    vector<int> sorted_v(t);
    vector<long long> prefix_unsorted_sum(t, 0);
    vector<long long> prefix_sorted_sum(t, 0);

    for (int i = 0; i < t; i++)
    {
        cin >> v[i];
        sorted_v[i] = v[i];
    }
    sort(sorted_v.begin(), sorted_v.end());

    prefix_unsorted_sum[0] = v[0];
    prefix_sorted_sum[0] = sorted_v[0];

    for (int i = 1; i < t; i++)
    {
        prefix_sorted_sum[i] = prefix_sorted_sum[i - 1] + sorted_v[i];
        prefix_unsorted_sum[i] = prefix_unsorted_sum[i - 1] + v[i];
    }

    int m, l, r, inc;
    cin >> m;
    while (m--)
    {
        cin >> inc >> l >> r;
        if (inc == 1)
        {
            if (l != 1)
            {
                cout << prefix_unsorted_sum[r - 1] - prefix_unsorted_sum[l - 2] << endl;
            }
            else
            {
                cout << prefix_unsorted_sum[r - 1] << endl;
            }
        }
        else
        {
            if (l != 1)
            {
                cout << prefix_sorted_sum[r - 1] - prefix_sorted_sum[l - 2] << endl;
            }
            else
            {
                cout << prefix_sorted_sum[r - 1] << endl;
            }
        }
    }

    return 0;
}