#include <cstdio>


inline unsigned int hash_value(int v)
{
    return static_cast<unsigned int>(v);
}

inline unsigned int hash_value(unsigned int v)
{
    return static_cast<unsigned int>(v);
}

template<typename T>
inline void hash_combine(unsigned int &seed, T const &v)
{
    seed ^= hash_value(v)
        + 0x9e3779b9 + (seed << 6) + (seed >> 2);
}

template<typename It>
inline void hash_range(unsigned int &seed, It first, It last)
{
    for(; first != last; ++first)
    {
        hash_combine(seed, *first);
    }
}

int main()
{
    unsigned int seed = 11;
    char data[] = {0x01, 0x00, 0x55, 0x8c, 0x35, 0x58, 0x50, 0x8c, 0x35, 0x58};
    for(int i = 0; i < 20; ++i)
    {
        seed = i;
        hash_range(seed, data, data + 10);
        printf("seed=%d, hash_sum = %x\n",i, seed);
    }
    return 0;
}
