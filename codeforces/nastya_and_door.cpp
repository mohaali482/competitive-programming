#include "bits/stdc++.h"

using namespace std;

int a[200005];
int b[200005];
void solution()
{
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    for (int i = 1; i < n - 1; i++)
    {
        if (a[i - 1] < a[i] && a[i] > a[i + 1])
        {
            b[i] = 1;
        }
        else
        {
            b[i] = 0;
        }
    }
    b[0] = 0;
    b[n - 1] = 0;
    int window = 0, j = 0, i = 0, ans = 0, minL = 0;
    while (j < k - 1)
    {
        window += b[j];
        j++;
    }
    int temp;
    while (j < n)
    {
        window += b[j];
        temp = window;
        if (b[i] == 1)
        {
            temp -= 1;
        }
        if (b[j] == 1)
        {
            temp -= 1;
        }
        if (temp > ans)
        {
            ans = temp;
            minL = i;
        }
        window -= b[i];
        i++;
        j++;
    }

    cout << ans + 1 << " " << minL + 1 << "\n";
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solution();
    }
    return 0;
}