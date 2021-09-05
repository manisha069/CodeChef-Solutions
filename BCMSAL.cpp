#include <iostream>
using namespace std;

int main() {

	int n;
	cin>>n;
	int a[n];
	int z=0, o=0;
	for(int i=0;i<n;i++)
	{
	    cin>>a[i];
	    if (a[i]==0)
	    {
	        z++;
	    }
	    else if (a[i]==1)
	    {
	        o++;
	    }
	}
	for(int i =0;i<z;i++)
	{
	    cout<<0<<" ";
	}
	for(int i =0;i<o;i++)
	{
	    cout<<1<<" ";
	}
	int t= n-(z+o);
	for(int i =0;i<t;i++)
	{
	    cout<<2<<" ";
	}
	return 0;
}
