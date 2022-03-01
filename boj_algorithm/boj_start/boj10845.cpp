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
		// 문자열로 비교
		if (commend == "push")
		{
			int num;
			cin >> num;
			arr.push(num);
		}
		else if (commend == "pop")
		{
			// 비어있는경우 -1 출력
			if (arr.empty() == true) cout << "-1" << endl;
			else
			{
				// 가장 앞에 있는 정수 출력 후 삭제
				cout << arr.front() << endl;
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
			// 비어있는 경우 1 숫자가 있는 경우 0
			if (arr.empty() == true) cout << "1" << endl;
			else cout << "0" << endl;
		}
		else if (commend == "front")
		{
			// 비어있는 경우 -1 그렇지 않은 경우 가장 앞의 수 출력
			if (arr.empty() == true) cout << "-1" << endl;
			else cout << arr.front() << endl;
		}
		else
		{
			// 가장 뒤에 수 출력
			if (arr.empty() == true) cout << "-1" << endl;
			else cout << arr.back() << endl;
		}
	}
}