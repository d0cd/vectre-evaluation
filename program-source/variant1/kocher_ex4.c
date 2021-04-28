#include <stdlib.h>
#include <stdint.h>
extern size_t array1_size, array2_size, array_size_mask;
extern uint8_t array1[], array2[], temp;

// ----------------------------------------------------------------------------------------
// EXAMPLE 4:  Add a left shift by one on the index.
// 
// Comments: Output is unsafe.

void victim_function_v04(size_t x) {
     if (x < array1_size)
          temp &= array2[array1[x << 1] * 512];
}
