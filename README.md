### Pelican Site Generator For My Blog

Themes using [Pelican Blue](https://github.com/Parbhat/pelican-blue/tree/1dda054242f9267f4bd49891b022ac41c9ecfbe8).

### Generate Pelican

```
pelican content
```

### Installing Themes Pelican
In my project site, i create directory named `themes`. This directory to store all themes for pelican.
Because, i use `pelican-blue` themes, I will clone repo pelican-blue:

```
$ mkdir themes
$ cd themes
$ git clone git@github.com:Parbhat/pelican-blue.git
$ cd ../
$ pelican-themes --install themes/pelican-blue
```
And then, after success installation pelican-blue theme, I would add pelican configuration to set the theme being 'pelican-blue':

```
THEME = 'pelican-blue'
```

After that, i will generate pelican content again:

```
$ pelican content
```

For more information about `pelican-blue`, you can read the references [here](https://github.com/Parbhat/pelican-blue).