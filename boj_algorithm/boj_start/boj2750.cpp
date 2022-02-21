#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int N;
	cin >> N;
	vector<int>arr;

	for (int i = 0; i < N; i++)
	{
		int num;

		cin >> num;
		arr.push_back(num);
	}
	int temp;
	for (int i = 0; i < N;i++)
	{
		for (int j = i+1; j < N; j++)
		{
			if (arr[i] > arr[j])
			{
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}
	for (int i = 0; i < N; i++)
	{
		cout << arr[i] << '\n';
	}
}