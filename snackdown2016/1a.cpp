#include <iostream>
#include <ctime>

using namespace std;

int check(int a[100000],int n) {
    for (int i=0;i<n-2;i++) {
        if (a[i]==a[i+1] && a[i+1]==a[i+2])
            return 1;
    }
    return 0;
}
int main() {
    clock_t ti;
    int t,p=0;
    cin>>t;
    int arr[100000];
    while (t) {
        int n;
        cin>>n;
        ti = clock();
        int c[100000];
        for (int i=0;i<n;i++)
            cin>>c[i];
        if (check(c,n))
            arr[p++] = 1;
        else
            arr[p++] = 0;
        t--;
        ti = clock() - ti;
        cout<<((float)ti)/CLOCKS_PER_SEC<<endl;
    }
    for(int i=0;i<p;i++) {
        if (arr[i])
            cout<<"Yes"<<endl;
        else
            cout<<"No"<<endl;
    }
}