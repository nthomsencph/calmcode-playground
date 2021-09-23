
# Numba commands
*"Numba is a tool that can make numeric code much faster in python. It offers a just in time compiler that can turn your functions into fast machine code and it can offer critical speedups. It also plays nice with numpy."* - Vincent, calmcode.io

Code-along @ https://calmcode.io/numba/introduction.html <br>

## Install numba
`pip install numba`

## Use numba
Effectively, we use the `nb.njit` decorator. 
JIT = Just In Time. 

    import numba as nb

    @nb.njit
    def func_two(n):
        result = 0
        squared = n * n
        for i in range(n):
            result += squared
        return result

## Test
**NOTE**: Numba is only faster for consecutive runs! Numba can only speed up a subset of py code, particularly numerical computations.
    start = time.time()
    func_two(1000)
    time.time() - start

## Parameters
When using numpy arrays/matrices and the operation is parallizable, numba will attempt to use multiple CPUs. Toggle this using `parallel=True`.
The `fastmath` parameter is more complex. Check the numba docs. It essentially makes a set of assumptions that can significantly speed up mathematical computation.

    @nb.njit(parallel=True, fastmath=True)

## 
