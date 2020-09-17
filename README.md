# Spritesheet-Splitter

Command spritesheet splitter design to split a PNG image into smaller tile given their size.

Use:

```
python splitter.py *png_filename* *tile_width* [*tile_height*]
```

Size are in pixels and we can omit the height from the tile we want, squares with sides equal to *tile_width* will be cut instead.
