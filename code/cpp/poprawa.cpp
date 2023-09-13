#include <iostream>
#include <string>
using namespace std;

void sprawdzanie(string slowo){

string slowoswap="";

for(int i=slowo.length()-1;i >=0; i--){

slowoswap = slowoswap + slowo[i];
}
if(slowo == slowoswap){
cout << "true";
}
else{
cout << "false";
}
}

int main(){
  
string slowo;

cout << "podaj slowo\n";
cin >> slowo;
sprawdzanie(slowo);

}
