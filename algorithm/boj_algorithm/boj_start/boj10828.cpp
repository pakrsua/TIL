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
		// 입력받은 commend와 문자열 비교
		if (commend == "push")
		{
			int num;
			cin >> num;
			arr.push(num);
		}
		else if (commend == "pop")
		{	
			// stack이 비어있는 경우 -1을 출력
			if (arr.empty() == true)
			{
				cout << "-1" << endl;
			}
			else
			{
				// 가장 위에 있는 정수 출력 후 pop으로 빼기
				cout << arr.top() << endl;
				arr.pop();
			}
			
		}
		else if (commend == "size")
		{
			// 사이즈 출력
			cout << arr.size() << endl;
		}
		else if (commend == "empty")
		{
			// 비어있는지 여부 확인
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