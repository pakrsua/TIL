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
		// �´ٸ� ������ ���ϰ� �������� 1�� ���Ѵ�
		if (arr[i] == 1)
		{
			ans = ans + score;
			score++;
		}
		// Ʋ���� �������� ������ �ʱ�ȭ�Ѵ�
		else
		{
			score = 1;
		}
	}
	cout << ans;
}