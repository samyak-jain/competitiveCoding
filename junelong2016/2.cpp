#include<iostream>
#include<cmath>

using namespace std;
int magic(int vec[10^24],int p) {
    for (int i=0;i<p;i++) {
        if (vec[i]%2) {
            return 0;
        }
    }
    return 1;
}
void rev(int array[],int size)
{   int temp;
    size--;
    for(int i=0;size>=i;size--,i++)
    {
        temp=array[i];
        array[i]=array[size];
        array[size]=temp;
    }
}
int main() {
    int t,k,d;
    int arr[10^12];
    int p=0;
    cin>>t;
    while (t) {
        cin>>k;
        int j=0,c=1,i,nozer=0;
        while (1) {
            nozer=0;
            int vec[10^24];
            int p=0;
            j+=2;
            d=j;
            while (d) {
                vec[p++] = d%10;
                d/=10;
            }
            rev(vec,p);
            if (magic(vec,p))
                c++;
            if (c==k)
                break;
            for (i=0;i<p;i++) {
                if (vec[i]==0)
                    nozer++;
            }   
            if ((vec[p-1-nozer]%2) && nozer!=0) {
                j+=pow(10.0,nozer);
                j-=2;
            }
        }
        arr[p++] = j;
        t--;
    }
    for (int i=0;i<p;i++)
        cout<<arr[i]<<endl;
    return 0;
}