#include<iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i=0; i < T; i++)
	{
		int s, n, ans = 0;
		cin >> s >> n;
		ans = ans + s;
		for (int j=0; j < n; j++)
		{
			int q, p;
			cin >> q >> p;
			ans = ans + (q * p);
		}
		cout << ans << '\n';
	}
}