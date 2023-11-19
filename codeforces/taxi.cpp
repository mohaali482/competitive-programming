#include "bits/stdc++.h"

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> s(n);
    for (int i = 0; i < n; i++)
    {
        cin >> s[i];
    }
    int i, j, sum;
    i = 0;
    j = n - 1;
    sort(s.begin(), s.end());
    int counter = 0;
    while (j > 0 && s[j] == 4)
    {
        counter++;
        j--;
    }
    sum = 0;
    while (i <= j)
    {
        if (sum == 4)
        {
            sum = 0;
            counter++;
        }
        else if (sum + s[j] <= 4)
        {
            sum += s[j];
            j--;
        }
        else if (sum + s[i] <= 4)
        {
            sum += s[i];
            i++;
        }
        else
        {
            sum = 0;
            counter++;
        }
    }
    if (sum > 0)
    {
        counter++;
    }
    cout << counter << endl;
    return 0;
}
