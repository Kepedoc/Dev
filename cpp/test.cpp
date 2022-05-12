#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;
 
int main()
{
    const int n = 7;
                                                
	int tab[n];
	for(int i=0;i<n;i++)
        {

             cin<<tab[i]<<" ";
        }
        cout<<endl;
        for(int i=0;i<n;i++)
		if(tab[i]%2==0)
        cout<<tab[i]<<" ";
        cout<<endl;
        for(int i=0;i<n;i++)

        cout<<tab[i]<<" ";
        cout<<endl;       
        system("pause");
        
        return 0;
}
