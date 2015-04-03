import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
f = open('yq01-ps-global', 'r')


x = []
for line in f:
    values = line.rstrip().split()[1].split(',')
    vec = []
    for k in range(28 - 0):
        vec.append(float(values[4 + k]))
    x.append(vec)

X = np.array(x)
Y = normalize(X, axis=0)

pca = PCA(n_components = 5)
pca.fit(Y)
PCA(copy=True, n_components=5, whiten=False)
print(pca.explained_variance_ratio_)
print(pca.components_)
    
