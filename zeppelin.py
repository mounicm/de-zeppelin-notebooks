'''
Zeppelin Dynamic Forms
pip install py4j
'''
%python
### Input form
print (z.input("f1","defaultValue"))

### Select form
print (z.select("f1",[("o1","1"),("o2","2")],"2"))

### Checkbox form
print("".join(z.checkbox("f3", [("o1","1"), ("o2","2")],["1"])))

'''
Matplotlib integration
The python interpreter can display matplotlib graph with the function z.show(). You need to have matplotlib module installed and a XServer running to use this functionality
'''
%python
import matplotlib.pyplot as plt
plt.figure()
(.. ..)
z.show(plt)
plt.close()

'''
z.show function can take optional parameters to adapt graph width and height
'''
%python
z.show(plt, width='50px')
z.show(plt, height='150px')
