### Slicing

- Creating a new array by taking chunks of values out of an existing one.

```python

Unsliced = np.array([[1,2,3,4,5],[6,7,8,9,0]])

# [[1 2 3 4 5]
# [6 7 8 9 0]]

Sliced = Unsliced[:]
# If we do not specify anything we take the entire NDarray.

Sliced_2 = Unsliced[0:0]
#The above means "start at index 0, and stop before reaching index 0."

#The above will always result in an empty array (or an empty view of the original array), regardless of the contents or shape of Unsliced.



```

### Slicing through portion of N-Dimension Arrays

```python
new_array = np.array([[56,43,56],[43,62,46],[44,67,76]])

slicing_row_columns = new_array[:,1:]

# The first portion represents the row while after the comma we have columns

print(slicing_row_columns)

array([[43,56],[62,46],[67,76]])


slicing_rows_columns_simultaneously = new_array([1:,1:])

array([[62,46],[67,76]])
```