# SVG-Box2dWeb

Parses all the circles, rectangles, and polygons in your SVG drawing. Defines and initalizes a Box2dWeb world with all its physics bodies & fixtures. Takes an SVG as an input, and outputs javascript that no one should ever have to code by hand. Note that all of your SVG elements should have a unique id attribute. Run the script with an SVG you've created and then have a look at `demo.html` in your browser.
## Usage
```bash
cd SVG-Box2dWeb
python svg-box2dweb.py ./test.svg > ./js/level1.js
```
