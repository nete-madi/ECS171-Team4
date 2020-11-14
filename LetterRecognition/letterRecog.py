import scipy.io as sio
import os


def main():
    # Read in EMNIST data as a from a matlab file
    # The .mat files can be downloaded from https://www.nist.gov/itl/products-and-services/emnist-dataset
    emnist = sio.loadmat(os.path.join('.', 'EMNIST', 'emnist-byclass'), simplify_cells=True)


if __name__ == "__main__":
    main()
