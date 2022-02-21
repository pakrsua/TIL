#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int N;
	cin >> N;
	vector<int>arr;
	int ans = 0;
	for (int i = 0; i < N; i++)
	{
		int num;
		cin >> num;
		arr.push_back(num);
	}
	int score = 1;
	for (int i = 0;i < N;i++)
	{
		// 맞다면 점수를 더하고 점수값에 1을 더한다
		if (arr[i] == 1)
		{
			ans = ans + score;
			score++;
		}
		// 틀리면 더해지는 점수를 초기화한다
		else
		{
			score = 1;
		}
	}
	cout << ans;
}