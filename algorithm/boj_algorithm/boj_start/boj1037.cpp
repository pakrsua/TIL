#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int N;
	cin >> N;
	vector<int>nums;

	for (int i = 0; i < N; i++)
	{
		int num;
		cin >> num;
		nums.push_back(num);
	}
	sort(nums.begin(), nums.end());
	// vector의 가장 첫 원소
	//cout << nums.front();
	// vector의 가장 마지막 원소
	//cout << nums.back();
	cout << nums.front() * nums.back();
}