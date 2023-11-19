#include <bits/stdc++.h>

using namespace std;

#define ll long long

ll dfs(unordered_set<ll> &added, unordered_map<ll, unordered_set<ll>> &graph, ll node, vector<ll> &cost)
{
    ll ans = cost[node];
    added.insert(node);
    for (auto x : graph[node])
    {
        if (added.find(x) == added.end())
        {
            ans = min(ans, dfs(added, graph, x, cost));
        }
    }

    return ans;
}

int main()
{
    ll n, m, st, en;
    cin >> n >> m;
    vector<ll> c(n + 1);
    for (ll i = 1; i < n + 1; i++)
    {
        cin >> c[i];
    }
    unordered_map<ll, unordered_set<ll>> graph;
    while (m--)
    {
        cin >> st >> en;
        graph[st].insert(en);
        graph[en].insert(st);
    }
    ll ans;
    ans = 0;

    unordered_set<ll> added;
    for (ll i = 1; i < n + 1; i++)
    {
        if (added.find(i) == added.end())
        {
            ans += dfs(added, graph, i, c);
        }
    }

    cout << ans << endl;

    return 0;
}