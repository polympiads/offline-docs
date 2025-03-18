
import argparse

def main ():
    parser = argparse.ArgumentParser("offdocs", description="Offline Documentation Builder")
    parser.add_argument("config")
    
    args = parser.parse_args()

if __name__ == "__main__":
    main()
