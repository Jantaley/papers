#include <cstdio>
#include <fstream>
#include <iostream>
void readMatrix( const std::string& strFilename, float** mat, int m ,int n );
void printMatrix(float**  mat, int m, int n );
int main()
{
    float  mult[2][16];
    int i, j, k;
    int r1 = 2,c1=16,c2=16;

    float ** a;
    // float a[2][16];
    float ** b;
    // float b[16][16]; 
    a = new float *[16];
    b = new float *[16];
    readMatrix("a.txt",a,2,16);
    readMatrix("b.txt",b,16,16);
    printMatrix(a,2,16); 
    // Initializing elements of matrix mult to 0.
    for(i = 0; i < r1; ++i)
        for(j = 0; j < c2; ++j)
        {
            mult[i][j]=0;
        }

    // Multiplying matrix a and b and storing in array mult.
    for(i = 0; i < r1; ++i)
        for(j = 0; j < c2; ++j)
            for(k = 0; k < c1; ++k)
            {
                mult[i][j] += a[i][k] * b[k][j];
            }

    // Displaying the multiplication of two matrix.

    return 0;
}

void readMatrix(  const std::string& strFilename, float** mat, int m, int n ) {
 std::ifstream myfile;
 myfile.open ( strFilename);
 for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
       myfile >> mat[i][j];
    }
 }
    // Do Work Here To Populate Matrix Object
} // readMatrix

void printMatrix(float ** mat,int m, int n ) {
    for(int i = 0; i < m; ++i)
    for(int j = 0; j < n; ++j)
    {
        printf(" %f ",mat[i][j]);
        if(j == n-1)
        printf("\n");
    }
    // Do Work Here To Print Matrix Being Passed In 
    } // printMatrix
