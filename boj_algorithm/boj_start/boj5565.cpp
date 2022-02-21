#include<iostream>
using namespace std;

int main()
{
	int price, book, plus = 0;

	cin >> price;
	for (int i = 0; i < 9 ; i++)
	{
		cin >> book;
		plus = plus + book;
	}
	cout << price - plus;

}
