// Question Link - https://www.codechef.com/CCADAAUG/problems/FLOW011

#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        float salary;
        cin>>salary;
        if(salary<1500){
            printf("%.2f\n",salary*2);
        }
        else{
            printf("%.2f\n", salary+500+(0.98*salary));
        }
    }
}