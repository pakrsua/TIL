#include<iostream>
using namespace std;

int main()
{
	int T, cnt=0, arr[5];
	cin >> T;
	for (int i = 0; i < 5; i++)
	{
		cin >> arr[i];
	}
	for (int i = 0; i < 5; i++)
	{
		if (arr[i] == T)
		{
			cnt++;
		}
	}
	cout << cnt;

}