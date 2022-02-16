i=1 
while i<10: 
    print '*'*i 
    i+=1 
""" 
* 
** 
*** 
**** 
***** 
****** 
******* 
******** 
********* 
Invert the triangle along x-axis (mirror image),
"""
i=10 
while i>0: 
    print '*'*i 
    i-=1 
"""
********** 
********* 
******** 
******* 
****** 
***** 
**** 
*** 
** 
* 
Invert the triangle along y-axis (mirror image),
"""
i=1 
while i<10: 
    print ' '*(10-i) + '*'*i 
    i+=1 
 """
         * 
        ** 
       *** 
      **** 
     ***** 
    ****** 
   ******* 
  ******** 
 ********* 
Isosceles triangle,
"""
i=1 
while i<10: 
    if i==1: 
        print ' '*(10-i) + '*' 
    else: 
        print ' '*(10-i) + '*'*i + '*'*(i-1) 
    i+=1  
""" 
         * 
        *** 
       ***** 
      ******* 
     ********* 
    *********** 
   ************* 
  *************** 
 ***************** 
Empty triangle,
"""
i=1 
while i<=10: 
    if i==1: 
        print ' '*(10-i) + '*' 
    elif i==10: 
        print '*'*(2*i-1) 
    else: 
        print ' '*(10-i) + '*' + ' '*(2*i-3) + '*' 
    i+=1 
""" 
         * 
        * * 
       *   * 
      *     * 
     *       * 
    *         * 
   *           * 
  *             * 
 *               * 
******************* 
