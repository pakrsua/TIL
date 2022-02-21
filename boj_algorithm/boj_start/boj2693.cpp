#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int T;
	cin >> T;

	//num을 입력받아서 배열에 넣기
	for (int tc = 0; tc < T; tc++)
	{	
		vector<int>arr;
		for (int i = 0; i < 10; i++)
		{
			int num;
			cin >> num;
			arr.push_back(num);
		}
		//내림차순 정렬
		//임시로 숫자를 넣을 변수
		int temp;
		for (int i = 0; i < 10; i++)
		{
			for (int j = i + 1; j < 10; j++)
			{
				if (arr[i] < arr[j])
				{
					temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}

		}
		//count는 0부터 시작하기 때문에 3번로 큰 수의 인덱스는 2
		cout << arr[2] << '\n';
	}

}
