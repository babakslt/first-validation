""" First validation
"""

from pathlib import Path

from hashlib import sha1


#from pandas import read_csv

data_pth = Path() / 'data'
example_pth =  data_pth / '24719.f3_beh_CHYM.csv'

if not example_pth.is_file():
    raise RuntimeError('Have you run the "get_data.py" script?')

contents = example_pth.read_bytes()
hash_value = sha1(contents).hexdigest()

print(f'Hash value for {example_pth} is {hash_value}')

hashes_pth = data_pth / 'data_hashes.txt'

print(f'Contents of {hashes_pth}')
hashes_text = hashes_pth.read_text()
print(hashes_text)


def hash_for_fname(fname):
    """ Return SHA1 hash string for file in `fname`

    `fname` can be a string or a Path.
    """
    # Convert a string filename to a Path object.
    fpath = Path(fname)
    # Your code here.
    contents = fpath.read_bytes()
    hash_value = sha1(contents).hexdigest()
    return hash_value


# Fill in the function above to make the test below pass.
# The test passes when there is no error.
calc_hash = hash_for_fname(example_pth)
exp_hash = '7fa09f0f0dc11836094b8d360dc63943704796a1'
assert calc_hash == exp_hash, f'{calc_hash} does not match {exp_hash}'


def check_hashes(hash_fname):
    """ Check hashes and filenames in given in file `hash_fname`
    """
    hash_pth = Path(hash_fname)
    # Directory containing hash filenames file.
    data_dir = hash_pth.parent
    # Read in text for hash filename
    # Split into lines.
    # For each line:
        # Split each line into expected_hash and filename
        # Calculate actual hash for given filename.
        # Check actual hash against expected hash
        # Return False if any of the hashes do not match.
    def get_file_hash(path_fname):
        contents = path_fname.read_bytes()
        hash_value = sha1(contents).hexdigest()
        return hash_value

    hash_text = hash_fname.read_text().splitlines()
    for line in hash_text:
        hash,_,file = line.split(" ")
        _hash = get_file_hash(data_dir/Path(file))
        if hash == _hash:
            continue
        else: return False
    return True


assert check_hashes(hashes_pth), 'Check hash list does not return True'
