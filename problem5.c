/*
 * ========================================================================
 *
 *       Filename:  problem5.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Friday, February 01, 2013 03:27:05 HKT
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Andy Scout (), andyhuzhill@gmail.com
 *   Organization:  
 *
 * =========================================================================
 */

#include <stdio.h>

int
main(int argc, char *argv[])
{
    long n, i, flag=0;

    n = 2520;
    while(!flag)
    {
        for(i=1; i< 21; i++)
        {
            if (n % i !=0) 
            {
                n ++;
                break;
            }
            else
                if ( i == 20 && n %i == 0) 
                {
                    flag = 1;
                }
        }
    }
    printf ( "%ld\n", n );
    return 0;
}
