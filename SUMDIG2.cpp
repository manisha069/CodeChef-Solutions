#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{
	    int n=0;
	    cin>>n;
	    int s=0;
	    int arr[n][n];
	    for(int i=0;i<n;i++)
	    {
	        for(int j=0;j<n;j++)
	        {
	            cin>>arr[i][j];
	        }
	    }

	    for(int i=0;i<n;i++)
	    {
	   // 	cout<<arr[i][i]<<endl;
	        s= s + arr[i][i];
	   // 	cout<<arr[i][n-i-1]<<endl;
	        s= s + arr[i][n-i-1];
	    }

	    if(n%2!=0)
	    {
	        s = s- arr[n/2][n/2];
	    }
	    cout<<s<<endl;

	}
	return 0;
}

