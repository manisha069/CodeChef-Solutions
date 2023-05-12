#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int N,A,B;
	    cin>>N>>A>>B;
	    int totaltime = 2*(180+N)-(A+B);
	    cout<<totaltime<<endl;
	}
	return 0;
}
