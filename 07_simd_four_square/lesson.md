# SIMD Four-Square

    def simd_four_square(num):

“Single Instruction, Multiple Data” (SIMD) is a technique used in modern computers to speed up calculations. When a computer applies same function to many different inputs, it often just applies the function to each input, one at a time. However, if we know ahead of time that this function is just being repeated over and over, we could just apply the function to all the inputs all at once! When used correctly, this technique can yield substantial speedups.†

Your task is to implement an imitation of what a SIMD-ized square operation would do. Such an operation would take the input num and treat it as four equidigit inputs. If there aren’t enough digits to evenly divide num into four chunks, then pad zeros to the left. Square those four chunks, and then throw away the appropriate amount of left digits such that the remaining number has the same number of digits as the original (including padding). Then, concatenate the four squared chunks and return the result.

![document image](https://i.imgur.com/bhDtlWS.png)



Examples:

    >>> simd_four_square(4)     #interpreted as 0004
    6
    >>> simd_four_square(54321) #interpreted as 00054321
    254941
    >>> simd_four_square(60271598)
    292504
    >>> simd_four_square(3210)
    9410
    >>> simd_four_square(11121314)
    21446996

†This is a simplification of what “really” happens. In reality, we are often restricted by the hardware to only 2–8 inputs at a time, but the speedups are still very significant. Additionally, because we are using Python, it is unlikely that this will actually be any faster than just computing squares on each number individually.