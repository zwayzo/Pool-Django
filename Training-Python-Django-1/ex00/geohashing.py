# geohashing.py
import antigravity  # import the library
import sys
#hashlib.md5() requires a bytes object, not a string.

if __name__ == "__main__":
    print("len:", len(sys.argv))
    if len(sys.argv) == 4:
        lat = float(sys.argv[1])
        lon = float(sys.argv[2])
        date = sys.argv[3].encode("utf-8")
        antigravity.geohash(lat, lon, date)
    else:
        print("Wront numbers of argument.\nExample of valid call: %s" % ("python3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68"))
        sys.exit(1)
        # Example usage with hardcoded value

    # print(antigravity.geohash(37.421542, -122.085589, b"2005-05-26-10458.68")
# )
