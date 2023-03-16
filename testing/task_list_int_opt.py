from time import time

def count_elapsed_time(f):
    """
    Decorator.
    Execute the function and calculate the elapsed time.
    Print the result to the standard output.
    """
    def wrapper():
        # Start counting.
        start_time = time()
        # Take the original function's return value.
        ret = f()
        # Calculate the elapsed time.
        elapsed_time = time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        return ret
    
    return wrapper


@count_elapsed_time
def main():
    objective_val = 12
    num_list = [
        -5, 4, 6, 7, 2, -10, -6, -4, 9, -9, -11, 11, -12, 12, -8, 1, -3, -1, -2, -7, -16, 10, -14, -13, 8, -17, -18, 13, -19, 14, -15, 16, -20, 20, 5, 17, -22, 22, 19, -21, -25, -23, 21, -24, -27, -26, -28, -30, 15, 25, 18, -29, -33, 30, -31, -35, -32, -37, -34, 26, -40, 24, -38, -36, 23, -42, 27, 28, 3, -39, -45, -44, -41, -43, -48, -47, -46, 29, -50, -52, -49, 31, 32, -55, -51, 34, -54, -53, 36, -57, -59, -56, -58, -60, -61, -63, -62, -65, -64, 38, -67, -68, -66, -71, 37, -70, -72, 39, 40, -75, -76, 42, -78, 35, -77, -74, -73, -69, -80, -79, 41, 43, -81, 44, 46, 45, -84, -85, 48, 47, -83, -86, -82, -87, -88, -89, -90, -92, -93, 50, -95, 49, -91, -94, 52, 51, -97, -98, -100, -96, 54, -102, 53, -99, -101, 56, 55, -105, 57, -103, -104, 59, 58, -108, -106, -107, 60, -111, 62, -109, -112, -110, 61, -113, -115, -114, 63, 65, -116, 64, 67, -118, 66, -117, 70, -121, -120, -119, 69, -123, 72, -122, -124, -125, 68, -126, 74, 71, 73, -128, -127, 75, 77, -129, -131, -130, 76, -133, -132, 78, 80, -135, -134, -137, 79, -136, 81, 82, -138, 84, 83, -141, -140, 85, -142, -139, 87, 86, -145, -144, -143, -146, 88, -148, 90, -150, -147, -149, 89, -152
    ]
    pair_list = list()

    for i in num_list:
        if objective_val - i in num_list:
            pair_list.append([i, objective_val - i])
                        

    print(pair_list)


if __name__ == "__main__":
    main()