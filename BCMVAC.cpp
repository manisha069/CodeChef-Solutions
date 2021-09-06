using namespace std;

int main() {
	int a[3];
	for(int i=0;i<3;i++)
	{
	    cin>>a[i];
	}
a[0]+=3;
a[1]+=5;
a[2]+=8;

int mini = a[0];
for(int i=1;i<3;i++)
{
    if (a[i]<mini){
        mini = a[i];
    }
}
if (a[0]==mini)
    cout<<"A";
    
else if (a[1]==mini)
    cout<<"B";
    
else{
    cout<<"C";}
    
	return 0;
}
