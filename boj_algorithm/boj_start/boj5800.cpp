#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int student, max_gap = 0;
		cin >> student;
		vector<int>arr;
		for (int j = 0; j < student; j++)
		{
			int score, gap = 0;
			cin >> score;
			arr.push_back(score);
		}
		// 오름차순 정렬
		sort(arr.begin(), arr.end());
		for (int j = 0; j < student; j++)
		{
			int gap = 0;
			// 인덱스 범위를 벗어나지 않기 위해 0인 경우 제외
			if (j >= 1)
			{
				// 오름차순으로 정렬이 되어있으므로 큰 수에서 작은수 빼기
				gap = arr[j] - arr[j - 1];
				if (gap > max_gap)
				{
					max_gap = gap;
				}
			}
		}
		cout << "Class " << i + 1<<"\n";
		cout << "Max " << arr.back() << ", Min " << arr.front() << ", Largest gap " << max_gap << "\n";
	}
}