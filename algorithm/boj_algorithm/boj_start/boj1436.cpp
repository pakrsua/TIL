#include<iostream>
#include<string>
using namespace std;

int main()
{
	string davel = "666";
	int cnt = 0, N, ans = 0, i = 0;
	cin >> N;
	while (true)
	{
		i++;
		if (to_string(i).find(davel) != string::npos)
		{
			cnt++;
			ans = i;
			//cout << cnt << "번 째 작은수" << ans << endl;
			if (cnt == N)
			{
				break;
			}
		}

	}
	cout << ans;
}