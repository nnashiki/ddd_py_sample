# ddd_py_sample
PythonでDDDしてみるsample

```
export PYTHONPATH="/Users/niten.nashiki/ghq/github.com/nnashiki/ddd_py_sample/src:$PYTHONPATH"
```

# CLI

```
# [niten.nashiki@PC-L056] ~/ghq/github.com/nnashiki/ddd_py_sample/src/ec
$ python main.py 
store success
0e3ddce8-c410-424d-8a54-2ec896c747b6
```

# API

```
# ~/ghq/github.com/nnashiki/ddd_py_sample/src/ec
$ uvicorn wsgi:app --reload --host 0.0.0.0 --port 8000      
```

```
$ curl -X POST -H "Content-Type: application/json" -d '{"name":"sensuikan1973"}' localhost:8000/v1/user
{"user":"sensuikan1973"}  
```

