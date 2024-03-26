# TF-IDF
**There is a simple web service which allows you to send a text file, and receive [TF and IDF](https://ru.wikipedia.org/wiki/TF-IDF) of every word**

## Launch
```
git clone https://github.com/yuwisasha/TF-IDF.git
```
```
poetry install
```
```
uvicorn app.main:app --reload
```
## Example
There is only one endpoint ```/upload```, where you can send a file via POST request, file will be saved in a project in ```app/text```
### text.txt
```
the house had a tiny little mouse
the cat saw the mouse 
the mouse ran away from the house 
the cat finally ate the mouse
the end of the mouse story
```
### Response
```
{
  "had": {
    "tf": 0.03,
    "idf": 1.61
  },
  "tiny": {
    "tf": 0.03,
    "idf": 1.61
  },
  "little": {
    "tf": 0.03,
    "idf": 1.61
  },
  "saw": {
    "tf": 0.03,
    "idf": 1.61
  },
  "ran": {
    "tf": 0.03,
    "idf": 1.61
  },
  "away": {
    "tf": 0.03,
    "idf": 1.61
  },
  "from": {
    "tf": 0.03,
    "idf": 1.61
  },
  "finally": {
    "tf": 0.03,
    "idf": 1.61
  },
  "ate": {
    "tf": 0.03,
    "idf": 1.61
  },
  "end": {
    "tf": 0.03,
    "idf": 1.61
  },
  "of": {
    "tf": 0.03,
    "idf": 1.61
  },
  "story": {
    "tf": 0.03,
    "idf": 1.61
  },
  "house": {
    "tf": 0.06,
    "idf": 0.92
  },
  "cat": {
    "tf": 0.06,
    "idf": 0.92
  },
  "a": {
    "tf": 0.03,
    "idf": 0.22
  },
  "the": {
    "tf": 0.29,
    "idf": 0
  },
  "mouse": {
    "tf": 0.16,
    "idf": 0
  }
}
```
