#include <iostream>
//#include <stack>
#include <string>
#include <math.h>
using namespace std;
template<class T>
class stack {
	private:
	    T items[1000];
	    int topi;
    public:
       stack(){
       	topi=-1;
        }
        bool empty (){
        	if (topi==-1)
        	   return true;
        	else
        	   return false;
        }
        void pop (){
        	topi--;
        }
        void push (T x){
        	items[++topi]=x;
        }
        T top (){
        	return items[topi];
        }
        int size(){
            return topi+1;
        }
};
//______________
float eval (float o1,float o2,char a){
    if (a=='+')
        return o1+o2;
    if (a=='-')
        return o1-o2;
    if (a=='*')
        return o1*o2;
    if (a=='/')
        return (float)o1/o2;
    if (a=='^')
        return pow(o1,o2);
}
bool is_amalvand(char a){
    if (a>='A'&&a<='Z'||a<='z'&&a>='a')
        return true;
    else
        return false;
}
bool prcden (char o2,char o1){
    if (o1='!'){
        if (o2=='^'||o2=='('||o2=='['||o2=='{')
            return true;
        else
            return false;
    }
    if (o1=='^'){
        if (o2=='^'||o2=='('||o2=='['||o2=='{')
            return true;
        else
            return false;
    }
    else if (o1=='*'||o1=='/'){
        if (o2=='^'||o2=='('||o2=='['||o2=='{')
            return true;
        else
            return false;
    }
    else if (o1=='+'||o1=='-'){
        if (o2=='+'||o2=='-'||o2==')'||o2==']'||o2=='}')
            return false;
        else
            return true;
    }
    else if (o1=='('||o1=='['||o1=='{'){
        if (o2==')'||o2==']'||o2=='}')
            return false;
        else
            return true;
    }
    else if (o1=='_'){
        if (o2==')'||o2==']'||o2=='}')
            return false;
        else
            return true;
    }
    else
        return true;
}
//______
int inf_to_pos (string in,char o[],char operand[]){
    stack <char>a;
    bool t=true;
    int amalvand=0,j=0;
    for (int i=0;in[i]!=0;i++){
        if (in[i]=='-'&&in[i-1]=='('){
            in[i]='_';
        }
        if (in[i]=='s'&&in[i+1]=='i'||in[i]=='c'&&in[i+1]=='o'){
            a.push(in[i]);
            i+=2;
        }
        else if (is_amalvand(in[i])){
            o[j]=in[i];
            operand[amalvand++]=in[i];
            j++;
        }
        else {
            t=true;
            for (;!(a.empty())&&!(prcden(in[i],a.top()));){
                if (a.top()=='('){
                    a.pop();
                    t=false;
                    if (a.empty())
                    break;
                    if (a.top()=='s'){
                       o[j++]=a.top();
                       a.pop();
                       o[j++]='i';
                       o[j++]='n';
                    }
                    else if (a.top()=='c'){
                       o[j++]=a.top();
                       a.pop();
                       o[j++]='o';
                       o[j++]='s';
                    }
                    break;
                }
                    o[j++]=a.top();
                    a.pop();
            }
            if (t)
            a.push(in[i]);
        }
    }
    while (!(a.empty())){
        o[j++]=a.top();
        a.pop();
    }
    o[j]=0;
    return amalvand ;

}
//___________
float eq(char p[],float x[]){
    stack<float>a;
    float temp,temp2;
    for (int i=0,j=0;p[i]!=0;i++){
        if (p[i]=='_'){
            	temp=a.top();
            	a.pop();
            	a.push(-temp);
            }
        else if (p[i]=='!'){
            	temp=a.top();
            	a.pop();
            	int temp1=1;
            	for (int i=temp;i>1;i--)
                temp1=temp1*i;
            	a.push(temp1);
            }

         else if (p[i]=='s'&&p[i+1]=='i'&&p[i+2]=='n'){
            temp=sin (a.top());
            a.pop();
            a.push(temp);
            i+=2;
        }
        else if(p[i]=='c'&&p[i+1]=='o'&&p[i+2]=='s'){
            temp=cos (a.top());
            a.pop();
            a.push(temp);
            i+=2;
        }
        else if(is_amalvand(p[i])){
            a.push(x[j++]);

        }
        else {
            temp2=a.top();
            a.pop();
            temp=a.top();
            a.pop();
            a.push(eval(temp,temp2,p[i]));
        }
    }
    return a.top();
}
int main()
{
    string input;
    char post[1000];
    char op [1000],a='y';
    while (a=='y'){
        cout<<"put in infix: ";
        cin>> input;
        int n;
        n=inf_to_pos (input,post,op);
        float x[n];
        cout <<"x= ";
        cin>>x[0];
        for(int i=0;i<n;i++){
           x[i]=x[0];
        }
        cout<< post<<endl<<eq(post,x)<<endl;
        do {
           cout <<"\ndo you whant to contineue?(y,n)";
           cin>>a;
    }while (a!='y'&&a!='n');
    }
    return 0;
}
