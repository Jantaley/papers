#include<iostream>
#include<iomanip>
#include <math.h>
using namespace std;

//该文件名称：cpptest.cpp

//终端下编译指令：

//g++ -o cpptest.so -shared -fPIC cpptest.cpp

//-o 指定生成的文件名，-shared 指定微共享库，-fPIC 表明使用地址无关代码

extern "C"{//在extern “C”中的函数才能被外部调用

    int test(int int_test,char char_test,char *test_string,int int_arr[4],char char_arr2[2][2]) {

        cout<<"输出参数中的int型:";
        cout<<int_test<<endl;

        cout<<"输出参数中的char型：";
        cout<<char_test<<endl;

        cout << "输出参数中的字char*字符:";
        cout<<test_string<<endl;

        cout << "输出参数中的int数组";
        for(int x = 0;x< 4;x++){cout << int_arr[x]<<"    ";}
        cout << endl;

        cout <<"输出参数中的二维数组：";
        for(int x = 0;x<2;x++){
            for(int y = 0;y<2;y++){
            cout <<char_arr2[x][y] << "    ";
            }
        }

        cout << endl;
        return 0;
    }
    typedef struct {
        int s, e, m;
        float v;
        double mv;//1+m/pow(2.,23)
    }sme;
    class float_sme_acc_kit{
        public:
            void float_sme_kit(){
                mvalue.s=0;
                mvalue.e=0;
                mvalue.m=0;
                mvalue.v=0;
                mvalue.mv=0;//true mv 1+m/pow(2.,23)
            };
            // void ~float_sme_kit();
            void clear(){
                mvalue.s=0;
                mvalue.e=0;
                mvalue.m=0;
                mvalue.v=0;
                mvalue.mv=0;//true mv 1+m/pow(2.,23)
                empty = true;
            };
            double rnd_even(double tempm){
                  int result;
                  double interm = tempm*pow(2.,23);
                  if((interm - floor(interm))==0.5){
                      result =fmod((interm-0.5), 2)==0 ? (int)(interm-0.5) : (int)(interm+0.5); 
                  }
                  else {
                       result  = round(interm);
                  }
                  return result/pow(2.,23);
            };
            float operator ()(
                float data
            ){
            //    std::cout<<"step0: new value = "<<data<<"   ";
               sme data2beadd = float2sme(data); 
               data2beadd = sme2float(data2beadd);
            //    std::cout<<data2beadd.s <<" "<< data2beadd.e<<" "<<data2beadd.m<<" "<<data2beadd.v<<std::endl;
               if(empty){
                mvalue = float2sme(data);
                mvalue = sme2float(mvalue);
                empty =false;
                return mvalue.v;
               }
               int diffe =  mvalue.e - data2beadd.e;
            //    std::cout << "mvalue.e= "<< mvalue.e <<" data2beadd.e= "<< data2beadd.e<<" diffe= "<<diffe <<std::endl;
            // std::cout<<diffe<<std::endl;
               if( diffe > 0 ){
                //   data2beadd.e = mvalue.e; 
                  double tempmv = data2beadd.mv / pow(2., diffe);
                //   std::cout<<"before rnd= "<<tempmv<<" after rnd = "<< rnd_even(tempmv)<<std::endl;
                  double resultmv = mvalue.mv*pow(-1, mvalue.s) + rnd_even(tempmv)*pow(-1, data2beadd.s); 
                  double result = mvalue.e==0 ? resultmv*pow(2.,-126): resultmv*pow(2.,mvalue.e-127);
                  mvalue = float2sme(result);
                  mvalue =sme2float(mvalue);
                //   std::cout<<"after rnd even = "<<data2beadd.m<<std::endl;
               }
               else{
                //    mvalue.e   = data2beadd.e;
                  double tempmv = mvalue.mv / pow(2., -diffe);
                //   std::cout<<"before rnd= "<<tempmv<<" after rnd = "<< rnd_even(tempmv)<<std::endl;
                  double resultmv = data2beadd.mv*pow(-1, data2beadd.s) + rnd_even(tempmv)*pow(-1, mvalue.s); 
                  double result = resultmv*pow(2.,data2beadd.e);
                  mvalue = float2sme(result);
                //    std::cout<<"after rnd even = "<<mvalue.m<<std::endl;
               }
               return mvalue.v;
            };
            sme float2sme(float data){//update s e m 
               sme sme_temp;  
               int temp_int = *(int *)&data; 
               sme_temp.s = temp_int >> 31;
               sme_temp.e = (temp_int & 0x7f800000)>>23;
               sme_temp.m =  temp_int & 0x007fffff;
               return sme_temp;
            };
            sme sme2float(sme temp_sme){//update mv and v
                // float test_float = e==0 ?  static_cast<float>(pow(-1,s)*(pow(2,e-127)))*static_cast<float>(( (static_cast<float>(m))/static_cast<float>(1<<23))): static_cast<float>(pow(-1,s)*pow(2,e-127))*static_cast<float>((1 + (static_cast<float>(m))/pow(2.,23)));
                if(temp_sme.e==0 && temp_sme.m==0)  { 
                    temp_sme.mv = 0;
                    temp_sme.v = 0;
                }
                else if(temp_sme.e==0 && temp_sme.m!=0){
                    // temp_sme.v = static_cast<float>(pow(-1,temp_sme.s)*(pow(2,-126)))*static_cast<float>(( (static_cast<float>(temp_sme.m))/static_cast<float>(1<<23)));
                    temp_sme.mv = temp_sme.m/pow(2.,23);
                    temp_sme.v = temp_sme.mv*pow(2.,-126)*pow(-1,temp_sme.s);
            }
                else{
                    // temp_sme.v =static_cast<float>(pow(-1,temp_sme.s)*pow(2,temp_sme.e-127))*static_cast<float>((1 + (static_cast<float>(temp_sme.m))/pow(2.,23)));
                    temp_sme.mv =1 + temp_sme.m/pow(2.,23);
                    temp_sme.v = temp_sme.mv*pow(2.,temp_sme.e-127)*pow(-1,temp_sme.s);
                }
                return temp_sme;
            };
            private:
                sme mvalue;
                bool empty;
    };
    float float_accsum(const float * input_float, int datalength){
        float_sme_acc_kit acc_kit;
        acc_kit.clear();
        int * input_int = (int *) input_float;
        float temp_acc=0;
        for(int i=0; i<datalength; i++){
            // float test_float = e==0 ?  static_cast<float>(pow(-1,s)*(pow(2,e-127)))*static_cast<float>(( (static_cast<float>(m))/static_cast<float>(1<<23))): static_cast<float>(pow(-1,s)*pow(2,e-127))*static_cast<float>((1 + (static_cast<float>(m))/pow(2.,23)));
            temp_acc = acc_kit( *(input_float+ i)); 
            float temp_float = *(input_float+ i);
            // std::cout<<std::hex<<*(input_int + i)<<std::endl;
            // std::cout<<std::dec<<"s, e, m = "<<s<<", "<<e<<", "<<m<<std::endl;
            std::cout<<"new value = "<< temp_float <<", acc ="<<temp_acc<<std::endl;
            // if(test_float == temp_float) std::cout<<"PASS!"<<std::endl;
            // else std::cout<<"FAIL!"<< test_float-temp_float<<std::endl;
        }
        return temp_acc;
    }
}
