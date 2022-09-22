// 스택을 이용한 알고리즘 풀이
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
		// 만약 num이 0이면 이전 숫자를 합에서 빼고 해당 숫자 삭제
		if (num == 0)
		{	
			ans = ans - arr.top();
			arr.pop();
		}
		// 0이 아니면 stack에 추가
		else
		{
			arr.push(num);
			ans = ans + num;
		}
	}
	cout << ans;
}