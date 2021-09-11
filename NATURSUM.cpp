#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t=0;
	cin>>t;
	for(int j=0;j<t;j++)
	{
	    int n=0, s=0;
	    cin>>n>>s;
	    int ss=0;
	    for(int i =0;i<=n;i++)
	    {
	        ss+= i;
	    }
	    cout<<ss-s<<endl;
	}
	return 0;
}