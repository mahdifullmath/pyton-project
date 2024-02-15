#include <immintrin.h>

void add_arrays_128bit(float* a, float* b, float* result, int size) {
    for (int i = 0; i < size; i += 4) {
        __m128 vec_a = _mm_load_ps(&a[i]);
        __m128 vec_b = _mm_load_ps(&b[i]);
        __m128 vec_result = _mm_add_ps(vec_a, vec_b);
        _mm_store_ps(&result[i], vec_result);
    }
}
void add_arrays_256bit(float* a, float* b, float* result, int size) {
    __m256 vec_a, vec_b, vec_c;
    for (int i = 0; i < size; i += 8) {
        vec_a = _mm256_load_ps(&a[i]);
   	    vec_b = _mm256_load_ps(&b[i]);
    	vec_c = _mm256_add_ps(vec_a, vec_b);
    	_mm256_store_ps(&result[i], vec_c);


    }
}