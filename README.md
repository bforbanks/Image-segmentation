# Image segmentation

**Lab 3** project on DTU by _Benjamin Banks(s234802), Bjørn Hagbarth(s234870) and Tobias Rodrigues Bjerre(s234823)_

## Gettings started

You need to have [Python3](https://www.python.org/downloads/) installed.

When installed, run the following to install the required python packages:

```{cmd}
pip install -r requirements.txt
```

Run the acutal script by running:

```{cmd}
python main.py
```

## Code documentation

### Dev tools

-   The [Python Image Preview](https://marketplace.visualstudio.com/items?itemName=076923.python-image-preview) VSCode extention can be used.
-   The tests have been written using python unittest. It is helpfull to run the tests in debug mode.

### Folder stucture

-   The modules are code written to do the unsupervised learning.
-   The services are meant support thing, handeling stuff like loading and converting.

### Other

-   If no dimension is writen, 1d is implied.

## Unsupervised learning protocol

1. Do K-nearest once on the image
2. Use the edge_score to calculate the inital backgroundcentroid
3. Find the oposite, and make it a foregroudcentroid
4. Run K-nearest n number of times.
5. Try to use positional information from current state of the the initial background and foreground centroids, to segment the image
