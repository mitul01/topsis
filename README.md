# Topsis


## What is TOPSIS

Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) originated in the 1980s as a multi-criteria decision making method. TOPSIS chooses the alternative of shortest Euclidean distance from the ideal solution, and greatest distance from the negative-ideal solution.

## Purpose

Package for Multiple-criteria decision-making using TOPSIS. Requires input file,weights and impacts. Returns a data frame which has score and rank of every label. This package can help improve decision-making.

### Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Topsis-Mitul-101803084.

```bash
pip install TOPSIS-Mitul-101803084
```

## Usage

```python
from TOPSIS_Mitul_101803084 import Topsis_rank
Topsis_rank("input.csv","1,1,1,2","+,+,+,-")
# Outputs a dataframe with score and rank columns

```
```python
from TOPSIS_Mitul_101803084 import Topsis_rank
# if output file name is provided,output file is saved in your current directory
Topsis_rank("input.csv","1,1,1,2","+,+,+,-","output.csv")
# Dataframe named output.csv will be saved in your current directory.

```
## Things to take care

1) Weights and Impacts provided as arguments should be separated by comma's and equal to number of numerical columns.
2) Categorical columns are not supported yet. They should be dropped or feature engineered into numerical columns using techniques like One Hot encoding etc.
3) First column should be label column.

## License
[MIT](https://choosealicense.com/licenses/mit/)
