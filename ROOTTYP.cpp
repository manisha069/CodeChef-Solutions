#include <iostream>
using namespace std;

int main() {
	int t =0;cin>>t;
	for(int i=0;i<t;i++)
	{
	    int a=0, b=0, c=0;
	    cin>>a>>b>>c;
	    int ans=0;
	    ans = (b*b) - (4*a*c);
	    
        if (ans > 0)
            cout<<"real"<<endl;
        else if (ans ==0)
            cout<<"equal"<<endl;
        else
            cout<<"imaginary"<<endl;
	}
	return 0;
}