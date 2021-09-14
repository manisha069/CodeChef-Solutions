#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n=0, x=0;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++)
	{
	    cin>>a[i];
	}
	cin>>x;
	for(int i=0;i<n;i++)
	{
	    if(a[i]>=x)
	    {
	        cout<<i;
	        break;
	    }
	}
	return 0;
}