import torchvision
import torch

# TODO Platonic ideals
# Create 'perfect' digits from simplified matrices and compare to those

def to_tensor(img):
    """Converts a PIL image into a pytorch tensor"""
    return torchvision.transforms.ToTensor()(img)

small_platonic_matrices = [
    # 0
    [
        [0,0,0,1,0,0,0],
        [0,0,1,0,1,0,0],
        [0,1,0,0,0,1,0],
        [0,1,0,0,0,1,0],
        [0,1,0,0,0,1,0],
        [0,0,1,0,1,0,0],
        [0,0,0,1,0,0,0],
     ]
    # TODO add more numbers
    # 1...
]

def mk_platonic_matrix(n):
    """
    Takes an n ∈ ℕ s.t. 0 <= n <= 9 and returns a 28x28 matrix representing the 'perfect'
    version of that digit
    """
    m = small_platonic_matrices[n]
    return make_bigger(m)

def make_bigger(matrix):
    """Takes a 7x7 matrix and makes it into a 28x28 version"""
    # TODO
    return matrix

def compare(t1, t2):
    """
    Returns a score representing the diff between two digit matrices
    """
    # TODO some average summing

def predict(img):
    """Predicts which digit the image represents"""
    t = to_tensor(img)
    # TODO loop through possible images and get a compare score for each platonic
    # TODO return the int with the best score

# get dataset
mnist = torchvision.datasets.MNIST('data', download=True)

# get an arbitrary digit at index 0
item = mnist.__getitem__(0)
img = item[0]
result = item[1]

print(predict(img))