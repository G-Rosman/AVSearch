#include <iostream> 
#include <regex> 
#include<string.h>
#include<stack>
#include<conio.h>
using namespace std;
int main()
{
	int i = 0;
	int y = 1;
	int&const icr = i; //const reference
	int& const icr1 = i; 
	int &const icr2 = i; 
	int & const icr3 = i; 
	icr = y;          
	icr = 99;         
	int x = 9;
	icr = x;
	cout << "icr: " << icr << ", y:" << y << endl;
	if (icr == x){
		icr = 10;
	}
	else if (icr == y){
		icr = y;
	}
	else if (icr == 3)	icr = 3;


	_getch();
	return 0;
}
