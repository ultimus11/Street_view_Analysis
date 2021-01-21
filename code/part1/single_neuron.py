import numpy as np
inputs=[1,0.5,-0.98]
weights=[0.2,-0.6,2]
bias=12
results = (inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2])+bias
print(results)
results1 = np.dot(weights,inputs)+bias
out_prev=0
for idx, data in enumerate(inputs):
	output = weights[idx]*data
	out_prev = out_prev + output
results2 = out_prev+bias
print(results1)
print(results2)