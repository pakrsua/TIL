// ������ �̿��� �˰��� Ǯ��
#include<iostream>
#include<stack>
using namespace std;

int main()
{
	int N, ans = 0;
	stack<int>arr;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		int num;
		cin >> num;
		// ���� num�� 0�̸� ���� ���ڸ� �տ��� ���� �ش� ���� ����
		if (num == 0)
		{	
			ans = ans - arr.top();
			arr.pop();
		}
		// 0�� �ƴϸ� stack�� �߰�
		else
		{
			arr.push(num);
			ans = ans + num;
		}
	}
	cout << ans;
}