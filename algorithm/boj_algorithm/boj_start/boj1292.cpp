#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int A, B, cnt = 0, num = 1;
	cin >> A >> B;
	vector<int>arr;

	while (cnt < B)
	{
		for (int i = 0; i < num;i++)
		{
			arr.push_back(num);
			cnt++;
			if (cnt > B) break;
		}
		num++;
	}
	int ans = 0;
	for (int i = A-1; i < B; i++)
	{
		ans += arr[i];
	}
	cout << ans;
}