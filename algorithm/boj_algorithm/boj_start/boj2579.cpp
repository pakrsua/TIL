#include<iostream>
using namespace std;
#define MAX 301

int main()
{
	int score[MAX];
	int ans_list[MAX];
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> score[i];
	}
	ans_list[0] = score[0];
	ans_list[1] = score[0] + score[1];
	ans_list[2] = max(score[0] + score[2], score[1] + score[2]);

	for (int i = 3; i < N; i++)
	{
		//���� ���� �� �ʿ��� ���� �ٷ� �տ� � ��������, �װͰ� �������� �������� ��������
		ans_list[i] = max(ans_list[i - 3] + score[i] + score[i-1], ans_list[i - 2] + score[i]);
	}
	cout << ans_list[N - 1];
}