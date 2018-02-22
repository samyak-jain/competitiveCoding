#include <stdio.h>
#include <iostream>

using namespace std;

int absdiff(int a, int b)
{
    if (a == b)
        return 0;        
    if (a > b)
        return (a - b);        
    return (b - a);
}

int min_diff_els(double a[], double b[], int size, int& idx1, int& idx2)
{
    int i = 0, j = 0;
    idx1 = 0;
    idx2 = 0;
    int mindiff;

    mindiff = absdiff(a[0], b[0]);
    
    if (0 == mindiff)
        return 0;
    
    ++i; ++j;
    while (i < size && j < size){
        int cv = absdiff(a[i], b[j]);
        if (cv < mindiff) {
            idx1 = i;
            idx2 = j;
            mindiff = cv;
        }
        
        if (a[i] < b[j])
            ++i;
        else
            ++j;
    }
    
    return mindiff;
}

int main()
{
    int t;
    cin>>t;
    int arr[10000];
    int p=0;
    while (t) {
    double a,b,c,d;
    cin>>a>>b>>c>>d;
    double x[100],y[100];
    for(int i=0;i<1000;i++) {
        x[i] = a+(c*i);
        y[i] = b+(d*i);
    }
    int size = sizeof(x)/sizeof(x[0]);
    int idx1, idx2, val;
    val = min_diff_els(x, y, size, idx1, idx2);
    
    arr[p++]=val;
    t--;
    }
    for (int i=0;i<p;i++)
        cout<<arr[i]<<endl;
    return 0;
}