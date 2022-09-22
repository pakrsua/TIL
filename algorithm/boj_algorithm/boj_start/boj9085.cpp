#include<iostream>
using namespace std;

int main()
{
	int T, N, num;
	cin >> T;
	for (int i = 0;i < T;i++)
	{
		int ans = 0;
		cin >> N;
		for (int j = 0; j < N; j++)
		{
			cin >> num;
			ans = ans + num;
		}
		cout << ans << '\n';
	}
}