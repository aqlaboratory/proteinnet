## Parsers
Two sample parsers of ProteinNet records are provided, one for the text-based file format ([text_parser.py](https://github.com/aqlaboratory/proteinnet/blob/master/code/text_parser.py)) and one for the `TFRecord` based file format ([tf_parser.py](https://github.com/aqlaboratory/proteinnet/blob/master/code/tf_parser.py)).

## Usage
### Text-based parser ([text_parser.py](https://github.com/aqlaboratory/proteinnet/blob/master/code/text_parser.py))
```
python text_parser.py text_sample > out
```

This will print the python dict corresponding to each record in `text_sample` to standard output. The function `read_record` can also be used to process ProteinNet records programmatically.

### TF-based parser ([tf_parser.py](https://github.com/aqlaboratory/proteinnet/blob/master/code/tf_parser.py))
This parser can only be used programmatically by invoking the `read_protein` function. For an example of its use see [the RGN repository](https://github.com/aqlaboratory/rgn/blob/master/model/model.py#L544).
