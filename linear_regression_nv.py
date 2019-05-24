# Pythonic implementation of linear regresstion with multiple variables
# Parameters thetha0 and theath1
# Termination condition - number of iteration
# Initialization - zero
# Data - artificially generated 
# Wendet - 2018 
# Generator function Y = 3*X1+2*X2+1

import random


train_x1 = []
train_x2 = []
train_y = []
pred_p = []
iter_ = 100000
theta0 = 0.0
theta1 = 0.0
theta2 = 0.0
l_rate = 0.01
train_size = 0

def normalize_f(data_):
	# Using zi = (xi-min(x))/(max(x)-min(x))
	min_data = min(data_)
	max_data = max(data_)
	normalized_data = [round(((data_[i]-min_data)/(max_data-min_data)),1) for i in range(len(data_))]
	return normalized_data

def predict_f():
	# Predict on existing data set(internal evailuation)
	global pred_p
	pred_p = [round((theta0 + theta1*train_x1[i]+theta2*train_x2[i]),1) for i in range(train_size)]
	return pred_p


def evaluate_f(predicted_,train_y):
	# Compute the prediction based on the parameter value
	correct = [1 for i in range(train_size) if train_y[i] == predicted_[i]]
	accuracy_ = (correct.count(1)/train_size)
	return accuracy_


def generate_f():
	# Generater function - Y = 3X1+2X2+1
	global train_x1,train_x2,train_y
	train_x1 = [random.uniform(1,100) for i in range(10)]
	train_x2 = [random.uniform(1,100) for i in range(10)]
	train_y = [float(3*train_x1[i]+ 2*train_x2[i]+1) for i in range(10)]
	print train_x1
	print train_x2
	print train_y

	# Normalize the data to avoid exploding cost value
	train_x1 = normalize_f(train_x1)
	train_x2 = normalize_f(train_x2)
	train_y = normalize_f(train_y)
	

def hypothesis_f(i,theta0,theta1,theta2):
	val_ = theta0 + theta1*train_x1[i]+theta2*train_x2[i]
	return val_

def sum_f0():
	error_i = [((theta0 + theta1*train_x1[i]+theta2*train_x2[i]) - train_y[i]) for i in range(train_size)]
	sum_ = sum(error_i)
	return sum_

def sum_f(train_x):
	error_i = [(((theta0 + theta1*train_x1[i]+theta2*train_x2[i]) - train_y[i])*train_x[i]) for i in range(train_size)]
	sum_ = sum(error_i)
	return sum_

def gsd_f():
	global theta0,theta1,theta2
	print 'initial theta0 %f ' % (theta0)
	print 'initial theta1 %f ' % (theta1)
	print 'initial theta1 %f ' % (theta2)
	print 'initial l_rate %f ' % (l_rate)
	i = 0
	while i < iter_:
		# Termination condition
		print ' Working at iteration %d ' % i
		error_sum0 = sum_f0()
		error_sum1 = sum_f(train_x1)
		error_sum2 = sum_f(train_x2)
		new_temp0 = l_rate * 1/float(train_size) * (error_sum0)
		new_temp1 = l_rate * 1/float(train_size) * (error_sum1)
		new_temp2 = l_rate * 1/float(train_size) * (error_sum2)
		print '		new_theta0 {0:.16f} '.format(new_temp0)
		print '		new_theta1 {0:.16f} '.format(new_temp1)
		print '		error_sum0 {0:.16f} '.format(error_sum0)
		print '		error_sum1 {0:.16f} '.format(error_sum1)
		temp0 = theta0 - new_temp0
		temp1 = theta1 - new_temp1
		temp2 = theta2 - new_temp2
		# Update the parameters simultaneously
		theta0 = temp0
		theta1 = temp1
		theta2 = temp2
		i += 1
	print 'Number of iteration %d ' % (iter_)
	print 'Approximated theta0 %f ' % (theta0)
	print 'Approximated theta1 %f ' % (theta1)
	print 'Approximated theta1 %f ' % (theta2)
	predicted_ = predict_f()
	accuracy_ = evaluate_f(predicted_,train_y)
	print 'Predicted Value%s \n' % predicted_
	print 'Actual Value %s \n' % train_y
	print'Accuracy : '+'{:.2%}'.format(accuracy_)
	


if __name__ == '__main__':
	generate_f()
	train_size = len(train_x1)
	print train_size
	gsd_f()
