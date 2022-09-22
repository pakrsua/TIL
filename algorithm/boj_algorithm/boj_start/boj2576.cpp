#include<iostream>
using namespace std;

int main()
{	
	int plus_ans = 0, min_ans = 100;
	for (int i = 0; i < 7; i++)
	{
		int num;
		cin >> num;
		// 나머지가 1이면
		if (num % 2 == 1)
		{
			plus_ans = plus_ans + num;
			//최소값보다 값이 작으면
			if (num < min_ans)
			{
				min_ans = num;
			}
		}
	}
	if (plus_ans > 0)
	{
		cout << plus_ans << '\n' << min_ans << '\n';
	}
	else cout << "-1" << '\n';
	
}