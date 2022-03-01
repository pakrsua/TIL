#include<iostream>
#include<queue>
#include<string>
using namespace std;

int main()
{
	int N;
	cin >> N;
	queue<int>arr;

	for (int i = 0; i < N; i++)
	{
		string commend;
		cin >> commend;
		// ���ڿ��� ��
		if (commend == "push")
		{
			int num;
			cin >> num;
			arr.push(num);
		}
		else if (commend == "pop")
		{
			// ����ִ°�� -1 ���
			if (arr.empty() == true) cout << "-1" << endl;
			else
			{
				// ���� �տ� �ִ� ���� ��� �� ����
				cout << arr.front() << endl;
				arr.pop();
			}

		}
		else if (commend == "size")
		{
			// ������ ���
			cout << arr.size() << endl;
		}
		else if (commend == "empty")
		{
			// ����ִ� ��� 1 ���ڰ� �ִ� ��� 0
			if (arr.empty() == true) cout << "1" << endl;
			else cout << "0" << endl;
		}
		else if (commend == "front")
		{
			// ����ִ� ��� -1 �׷��� ���� ��� ���� ���� �� ���
			if (arr.empty() == true) cout << "-1" << endl;
			else cout << arr.front() << endl;
		}
		else
		{
			// ���� �ڿ� �� ���
			if (arr.empty() == true) cout << "-1" << endl;
			else cout << arr.back() << endl;
		}
	}
}