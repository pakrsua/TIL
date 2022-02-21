#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	int n, p;
	
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> p;
		vector <int> price(p);
		vector <string>player(p);
		int max_num = 0;
		string ans;

		for (int j = 0; j < p; j++)
		{
			cin >> price[j] >> player[j];

			if (max_num < price[j])
			{
				max_num = price[j];
				ans = player[j];
			}
		}
		cout << ans << endl;
	}
}