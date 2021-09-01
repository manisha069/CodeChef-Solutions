// Question Link:- https://www.codechef.com/CCADAAUG/problems/FLOW010

#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        char ch;
        cin>>ch;
        if(ch=='B' or ch=='b') cout<<"BattleShip"<<endl;
        else if(ch=='C' or ch=='c') cout<<"Cruiser"<<endl;
        else if(ch=='D' or ch=='d') cout<<"Destroyer"<<endl;
        else if(ch=='F' or ch=='f') cout<<"Frigate"<<endl;
    }
    return 0;
}