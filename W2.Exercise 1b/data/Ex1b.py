import numpy as np
from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import pydicom as dicom
from sklearn import decomposition

import seaborn as sns 
import pandas as pd

in_dir = "Exercise 1b/data/"
txt_name = "irisdata.txt"
iris_data = np.loadtxt(in_dir + txt_name, comments="%")

x = iris_data[0:50, 0:4]

n_feat = x.shape[1]
n_obs = x.shape[0]
print(f"Number of features: {n_feat} and number of observations: {n_obs}")


#----------------- Exercise 2 -----------------#

sep_l = x[:, 0]
sep_w = x[:, 1]
pet_l = x[:, 2]
pet_w = x[:, 3]

# Use ddof = 1 to make an unbiased estimate
var_sep_l = sep_l.var(ddof=1)
var_sep_w = sep_w.var(ddof=1)
var_pet_l = pet_l.var(ddof=1)
var_pet_w = pet_w.var(ddof=1)

# print(var_pet_l, var_pet_w, var_sep_l, var_sep_w)
# print(len(sep_l))

#----------------- Exercise 3 -----------------#

for i in range(len(sep_l)):
    count1 =+ sep_l[i]*sep_w[i]
    count2 =+ sep_l[i]*pet_l[i]

cov_lw = count1/(len(sep_l)-1)
cov_sp = count2/(len(sep_l)-1)

# print("Sepal and petal", cov_sp," Length and witdh" , cov_lw)

#----------------- Exercise 4 -----------------#

# plt.figure()

# d = pd.DataFrame(x, columns=['Sepal lenght', 'Sepal width', 'Petal lenght', 'Petal width'])
# sns.pairplot(d)

# plt.show()

#----------------- PCA Analysis  --------------#

#----------------- Exercise 5 -----------------#

mn = np.mean(x, axis = 0)
data = x - mn

print(data.shape)

Cx = np.matmul(np.transpose(data), data)/(len(data)-1)
Cx2 = np.cov(data)

# print(Cx)


#----------------- Exercise 6 -----------------#

values, vectors = np.linalg.eig(Cx)

print("values: ", values," \n ", "vectors: ", vectors)

#----------------- Exercise 7 -----------------#

# v_norm = values / values.sum() * 100
# plt.plot(v_norm)
# plt.xlabel("Principal component")
# plt.ylabel("Percent explained variance")
# plt.ylim([0, 100])
# plt.show()

#----------------- Exercise 8 -----------------#

pc_proj = vectors.T.dot(data.T)

# print(pc_proj.shape)

# plt.figure()

# d = pd.DataFrame(pc_proj)
# sns.pairplot(d)

# plt.show()

#----------------- Exercise 9 -----------------#

pca = decomposition.PCA()
pca.fit(x)
values_pca = pca.explained_variance_
exp_var_ratio = pca.explained_variance_ratio_
vectors_pca = pca.components_
data_transform = pca.transform(data)

print(pca, pca.fit(x), values_pca, vectors_pca)