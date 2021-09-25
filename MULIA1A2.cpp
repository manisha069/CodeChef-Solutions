#include <iostream>
using namespace std;

int main() {
	// your code goes here
		int t=0;
		cin>>t;
	while(t!=0)
	{
	    t--;
	    int n;
	    cin>>n;
	    int a[n], b[n];
	    for(int i =0;i<n;i++)
	    {
	        cin>>a[i];
	    }
	    for(int i=n-1;i>=0;i--)
	    {
	        cin>>b[i];
	    }

	    int ans =0;
	    for(int i =0;i<n;i++)
	    {
	        ans += a[i]*b[i];
	    }
	    cout<<ans<<endl;
	}
	return 0;
}