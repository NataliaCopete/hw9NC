#include <iostream>
#include<ctime> 

using std::cout;
using std::endl;



int fibonacci(int N);
float get_time(int N);

int main(){
 int i;
 for(i=0;i<40;i++){

cout<<i<<" "<<get_time(i)<<endl;
}
return 0;
}


int fibonacci(int N){
  if(N==0||N==1){return N;
  } 
  else{ return fibonacci(N-2)+fibonacci(N-1);
  }
}

float get_time(int N){
clock_t t;
t = clock();
fibonacci(N);
t = clock() - t;
float time = ((float)t)/CLOCKS_PER_SEC;
return time;
}
