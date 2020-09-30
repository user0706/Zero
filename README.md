
<p align="center">
  <img height="70" src="https://github.com/user0706/Zero/blob/master/ignore/logo.png?raw=true">
</p>

# About Zero
Zero is a simple tool for creating a dataset based on a known corpus and desired keywords.<br\>
To successfully create a dataset, it is necessary to define the corpus, output file, label and keyword/s.

### - Input corpus
A directory containing one or more `.txt` documents needs to be selected. Preferably, the document is `utf-8` encoded. Also, to avoid memory problems, it is recommended that the selected directory contains **more smaller documents** than one large one.
### - Output file
The output file must be `.CSV` format `utf-8` encoded, comma delimited. 
### - Label
By defining the label, the class is defined, ie. affiliation of sentences containing the desired keyword.
### - Keyword/s
For a keyword, it is possible to enter **one or more words**. Each word must be separated by a punctuation mark (preferably a comma)
## Screenshots
![enter image description here](https://github.com/user0706/Zero/blob/master/ignore/example.png?raw=true)


## To-Do
- [ ] Duplicate keyword detection
- [ ] Code adaptation for big data
