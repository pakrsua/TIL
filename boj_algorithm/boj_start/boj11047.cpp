#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int N, K;
	cin >> N >> K;
	vector<int>wallet;

	for (int i = 0; i < N ; i++)
	{
		int money;
		cin >> money;
		wallet.push_back(money);
	}
	int cnt = 0;
	for (int i = N-1; i >= 0; i--)
	{
		while (K >= wallet[i])
		{
			K = K - wallet[i];
			//cout << "K °ª :" << K << '\n';
			cnt++;
		}
	}
	cout << cnt;
}