# ************************************************************************
# Apple Store Data Set Preparation
# ************************************************************************

# Some of the exercises use the app store data set, which is available from Kaggla at
# https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps.

# In a nutshell, the data set provides information on popular apps including their price, genre, and user rating.
# Please check out the data set homepage for more information and some descriptive statistics.

# ------------------------------------------------------------------------
# Import standard libraries and load the data
# ------------------------------------------------------------------------
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# You will need to download the data from Kaggle or Moodle. Afterwards, depending on where you stored the
# data on your computer, you will need to update the following line accordingly. To that end, it is important
# to remember your current working directory.
print('Working directory is: {}'.format(os.getcwd()))
app = pd.read_csv("./AppleStore.csv")

# ------------------------------------------------------------------------
# First overview and basic preparation
# ------------------------------------------------------------------------
# Let's examine the data and remove some unneeded columns
# What columns exist and what is their type?
app.dtypes

# We do not need this Unnamed column
app.drop(['Unnamed: 0'], axis=1, inplace=True)

# There are some more columns that we will not need, so let's drop these as well
app = app.drop(["id", "ver", "user_rating_ver", "rating_count_ver"], axis=1)
app.dtypes

# We use the app name as (row) index
app = app.set_index('track_name')

# ------------------------------------------------------------------------
# Scaling
# ------------------------------------------------------------------------
# The data includes some numeric variables. As we know, such variables
# should not be put into a model in their raw format. Instead, we
# should scale variables so that the value range of a variable is
# comparable across variables. To achieve this, we apply the z-transformation
# using some scikit-learn functionality.

# These are the variables we are going to scale
vars2scale =["size_bytes", "price", "rating_count_tot", "sup_devices.num",
             "ipadSc_urls.num", "lang.num", "vpp_lic"]
# Their value rages are indeed much different
app[vars2scale].mean()
desc = app[vars2scale].describe()
desc
# Remember that we imported the standard scaler class above. It facilitates
# the scaling
scaler = StandardScaler().fit(app[vars2scale])
app[vars2scale] = scaler.transform(app[vars2scale])
# Check that it worked
app[vars2scale].describe()

# ------------------------------------------------------------------------
# Category coding
# ------------------------------------------------------------------------
# The data also includes categorical variable. Pandas will often import
# these using the data type object. The primary genre of the app being an
# example
app['prime_genre'].value_counts(normalize=True)
app['prime_genre'].hist()
plt.show()

# We can exploit the fact that all categories received the data type object.
# (Yes, the same approach would have worked above with the numeric types)
vars2code = app.select_dtypes(include=[object]).columns

# We can now transform these variables using dummy coding. # Of course,
# this will increase dimensionality a lot
app.shape
app = pd.get_dummies(app, prefix_sep="_", columns=vars2code, drop_first=False)
app.shape

# Also verify how the new dummy variables have been labeled
cols = app.columns.tolist()
cols
# ------------------------------------------------------------------------
# Finish
# ------------------------------------------------------------------------
# Later, we will use the variable user_rating as target variable and try
# to predict the user rating of an app. To that end, it is convenient to
# change the order of columns so that the target is the last column

cols.remove('user_rating')
cols.append('user_rating')
app = app[cols]

# We will use the user rating as a target variable for multinomial
# classification. For now, to keep things simple, we just round its
# values to have six different 'levels'
app["user_rating"] = app["user_rating"].round()
app["user_rating"].unique()

target_file = './AppleStore_prep.csv'
app.to_csv(target_file, sep='\t', encoding='utf-8')
print('Saved prepared data to {}'.format(target_file))


