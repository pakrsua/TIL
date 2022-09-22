#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main()
{
	int N;
	cin >> N;
	stack<int>arr;
	for (int i = 0; i < N; i++)
	{
		string commend;
		cin >> commend;
		// �Է¹��� commend�� ���ڿ� ��
		if (commend == "push")
		{
			int num;
			cin >> num;
			arr.push(num);
		}
		else if (commend == "pop")
		{	
			// stack�� ����ִ� ��� -1�� ���
			if (arr.empty() == true)
			{
				cout << "-1" << endl;
			}
			else
			{
				// ���� ���� �ִ� ���� ��� �� pop���� ����
				cout << arr.top() << endl;
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
			// ����ִ��� ���� Ȯ��
			if (arr.empty() == true)
			{
				cout << "1" << endl;
			}
			else cout << "0" << endl;
		}
		else
		{
			if (arr.empty() == true)
			{
				cout << "-1" << endl;
			}
			else cout << arr.top() << endl;
		}
	}
}