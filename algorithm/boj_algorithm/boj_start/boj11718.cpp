#include<iostream>
#include<string>
using namespace std;

int main()
{
	string text;
	while (1)
	{
		getline(cin, text);
		if (text == "")
		{
			break;
		}
		cout << text << '\n';
	}
}