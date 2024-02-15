#include <iostream>

using namespace std;

struct node{
    int level;
    int profit;
    int weight;
};

float bound(node u, int W, int n, int w[], int p[]){
    int i, k, totweight;
    float result;
    if(u.weight>= W)
        return 0;
    else{
        result= u.profit;
        i= u.level+1;
        totweight=u.weight;
        while (i<=n && totweight+ w[i]<=W){
            totweight= totweight+ w[i];
            result= result+ p[i];
            i++;
        }
        k=i;
        if (k<=n)
            result= result+(W-totweight)*p[k]/w[k];
        return result;
    }
}

void knapsack (int n, int p[], int w[], int W, int &maxprofit){
    node Q[200]={0};
    int k=0;
    int counter=0;
    node u,v;

    v.level=0; v.profit=0; v.weight=0;
    maxprofit=0;

    Q[k].level=v.level;
    Q[k].profit=v.profit;
    Q[k].weight=v.weight;
    counter++;
    while(counter!=0){
        u.level=v.level+1;
        u.weight=v.weight+w[v.level];
        u.profit=v.profit+p[v.level];
        counter--;

    if(u.weight<=W && u.profit>maxprofit)
        maxprofit=maxprofit+u.profit;

    if(bound(u,W,n,w,p)>maxprofit){
        Q[2*k+1].level=u.level;
        Q[2*k+1].profit=u.profit;
        Q[2*k+1].weight=u.weight;
        counter++;
    }
    u.weight=v.weight;
    u.profit=v.profit;

    if(bound(u,W,n,w,p)>maxprofit){
        Q[2*k+2].level=u.level;
        Q[2*k+2].profit=u.profit;
        Q[2*k+2].weight=u.weight;
        counter++;
    }
    v.level++;
    }

}
int main()
{
    int n,W,a;
    int maxprofit;
    cout<<"Enter n= ";
    cin>>n;
    cout<<"Enter W= ";
    cin>>W;
    int p[n],w[n],pw[n];

    for(int i=0;i<n;i++){
        cout<<"Enter w["<<i<<"]= ";
        cin>>w[i];
    }
     for(int i=0;i<n;i++){
        cout<<"Enter p["<<i<<"]= ";
        cin>>p[i];
    }

    for(int i=0;i<n;i++)
        pw[i]=p[i]/w[i];


    for(int i=n-1;i>0;i--){
        for(int j=0;j<i;j++)
        if(pw[j]<pw[j+1]){
            a=pw[j];
            pw[j]=pw[j+1];
            pw[j+1]=a;

            a=w[j];
            w[j]=w[j+1];
            w[j+1]=a;

            a=p[j];
            p[j]=p[j+1];
            p[j+1]=a;

        }
    }
knapsack(n,p,w,W,maxprofit);
cout<<"MAX PROFIT IS = "<<maxprofit;
    return 0;
}
