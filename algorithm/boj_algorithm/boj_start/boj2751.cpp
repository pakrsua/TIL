#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	vector<int>arr;
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int num;
		cin >> num;
		arr.push_back(num);
	}
	sort(arr.begin(),arr.end());
	for (int i = 0; i < N; i++)
	{
		cout << arr[i] << '\n';
	}
}