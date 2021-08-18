#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t=0;
	cin>>t;
	for (int l=0;l<t; l++)
	{
	    int n, k, c=0;
	cin>>n>>k;
	int ls[n];
	for(int i=0; i<n; i++){
	    cin>>ls[i];
	}

	for(int i=0;i<n;i++)
	{

	    if (ls[i]<k)
	    {
	        c++;
	    }

	}
	cout<<c<<endl;
	}
	
	return 0;
}