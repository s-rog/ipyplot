"""
IPyPlot package gives you a fast and easy way of displaying images in python notebooks environment.
It leverages HTML and IPython package under the hood which makes it very fast and efficient in displaying images.
It works best for images as string URLs to local/external files but it can also be used with numpy.ndarray or PIL.Image image formats as well.
To use it, you just need to add `import ipyplot` to your code and use one of the public functions available from top level module.
Example:
```
import ipyplot

ipyplot.plot_images(images=images, labels=labels, ..)
```
"""  # NOQA E501

import sys

from .plotting import *

name = "ipyplot"

__version__ = "1.1.0"

if 'google.colab' in sys.modules:  # pragma: no cover
    print(
        """
        WARNING! Google Colab Environment detected!
        You might encounter issues while running in Google Colab environment.
        If images are not displaying properly please try setting `base_64` param to `True`.
        """  # NOQA E501
    )
