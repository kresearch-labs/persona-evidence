# TASK
The project (learn, checked out at an old commit) has this issue:

FeatureUnion not working when aggregating data and pandas transform output selected
### Describe the bug

I would like to use `pandas` transform output and use a custom transformer in a feature union which aggregates data. When I'm using this combination I got an error. When I use default `numpy` output it works fine.

### Steps/Code to Reproduce

```python
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import set_config
from sklearn.pipeline import make_union

index = pd.date_range(start="2020-01-01", end="2020-01-05", inclusive="left", freq="H")
data = pd.DataFrame(index=index, data=[10] * len(index), columns=["value"])
data["date"] = index.date


class MyTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X: pd.DataFrame, y: pd.Series | None = None, **kwargs):
        return self

    def transform(self, X: pd.DataFrame, y: pd.Series | None = None) -> pd.DataFrame:
        return X["value"].groupby(X["date"]).sum()


# This works.
set_config(transform_output="default")
print(make_union(MyTransformer()).fit_transform(data))

# This does not work.
set_config(transform_output="pandas")
print(make_union(MyTransformer()).fit_transform(data))
```

### Expected Results

No error is thrown when using `pandas` transform output.

### Actual Results

```python
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[5], line 25
     23 # This does not work.
     24 set_config(transform_output="pandas")
---> 25 print(make_union(MyTransformer()).fit_transform(data))

File C:/Users/agent/.local/share/virtualenvs/3e_VBrf2/lib/python3.10/site-packages/sklearn/utils/_set_output.py:150, in _wrap_method_output.<locals>.wrapped(self, X, *args, **kwargs)
    143 if isinstance(data_to_wrap, tuple):
    144     # only wrap the first output for cross decomposition
    145     return (
    146         _wrap_data_with_container(method, data_to_wrap[0], X, self),
    147         *data_to_wrap[1:],
    148     )
--> 150 return _wrap_data_with_container(method, data_to_wrap, X, self)

File C:/Users/agent/.local/share/virtualenvs/3e_VBrf2/lib/python3.10/site-packages/sklearn/utils/_set_output.py:130, in _wrap_data_with_container(method, data_to_wrap, original_input, estimator)
    127     return data_to_wrap
    129 # dense_config == "pandas"
--> 130 return _wrap_in_pandas_container(
    131     data_to_wra

Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
