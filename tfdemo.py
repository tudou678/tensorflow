# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 18:28:10 2018

@author: Administrator
"""
#import tensorflow lib
import tensorflow as tf
tf.reset_default_graph()
#create a graph
g = tf.Graph()
with g.as_default():
    a = tf.constant(2,name='a')
   # print(a.name,a)
    b = tf.constant(3,name='b')
  #  print(b.name,b)    
    x = tf.add(a,b,name='add')
  #  print(x.name,x)
# write the graph definiation to disk
writer = tf.summary.FileWriter('./graphs_add',g)
#print(g.as_graph_def())
writer.close()

# we show that node is append to the graph step by step.
with tf.Graph().as_default() as new:
    # add node a to graph
    c = tf.placeholder(tf.float32,name='c')
   # print(new.as_graph_def())
    # you can visualize it in tensorboard!
    tf.summary.FileWriter('./graphs_add',new).close()
    # add node b to graph
    d = tf.placeholder(tf.float32,name='d')
   # print(new.as_graph_def().node)
    # you can visualize it in tensorboard!
    tf.summary.FileWriter('./graphs_add',new).close()
    e = tf.add(c,d,name='e')
    #print(new.as_graph_def().node)
    
"""  
from graphviz import Digraph

dot = Digraph()
for n in new.as_graph_def().node:
    dot.node(n.name,label=n.name)
    for i  in n.input:
        dot.edge(i,n.name)
dot
"""