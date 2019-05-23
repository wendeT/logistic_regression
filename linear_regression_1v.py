# Pythonic implementation of linear regresstion with single variables
# Parameters thetha0 and theath1
# Termination condition - number of iteration
# Initialization - zero
# Data - artificially generated 
# Wendet - 2018 

train_x = []
train_y = []
pred_p = []
iter_ = 10000
theta0 = 0.0
theta1 = 0.0
l_rate = 0.01
train_size = 0

def normalize_f(data_):
	# Using zi = (xi-min(x))/(max(x)-min(x))
	normalized_data = []
	min_data = min(data_)
	max_data = max(data_)
	normalized_data = [round(((data_[i]-min_data)/(max_data-min_data)),1) for i in range(len(data_))]
	return normalized_data

def predict_f(theta0,theta1):
	# Predict on existing data set(internal evailuation)
	global pred_p
	pred_p = [round((theta0 + theta1*train_x[i]),1) for i in range(train_size)]
	return pred_p


def evaluate_f(predicted_,train_y):
	# Compute the prediction based on the parameter value
	correct = []
	correct = [1 for i in range(train_size) if train_y[i] == predicted_[i]]
	accuracy_ = (correct.count(1)/train_size)
	return accuracy_


def generate_f():
	# Generater function - Y = X+1
	global train_x,train_y
	train_x1 = [float(i) for i in range(10)]
	train_y1 = [float(i+1) for i in range(10)]
	# print train_x1
	# print train_y1
	# Normalize the data to avoid exploding cost value
	train_x = normalize_f(train_x1)
	train_y = normalize_f(train_y1)
	

def hypothesis_f(i,theta0,theta1):
	val = theta0 + theta1*train_x[i]
	return val

def sum_f0(theta0,theta1):
	sum_ = 0.0
	# Go through all training data to compute the thetha
	for i in range(train_size):
		error_i = (theta0 + theta1*train_x[i]) - train_y[i]
		sum_ += error_i
	return sum_

def sum_f1(theta0,theta1):
	sum_ = 0.0
	# Go through all training data to compute the thetha
	for i in range(train_size):
		error_i = (theta0 + theta1*train_x[i] - train_y[i])*train_x[i]
		sum_ += error_i
	return sum_

def gsd_f():
	global theta0,theta1
	print 'initial theta0 %f ' % (theta0)
	print 'initial theta1 %f ' % (theta1)
	print 'initial l_rate %f ' % (l_rate)
	i = 0
	while i < iter_:
		# Termination condition
		print ' Working at iteration %d ' % i
		error_sum0 = sum_f0(theta0,theta1)
		error_sum1 = sum_f1(theta0,theta1)
		new_temp0 = l_rate * 1/float(train_size) * (error_sum0)
		new_temp1 = l_rate * 1/float(train_size) * (error_sum1)
		print '		new_theta0 {0:.16f} '.format(new_temp0)
		print '		new_theta1 {0:.16f} '.format(new_temp1)
		print '		error_sum0 {0:.16f} '.format(error_sum0)
		print '		error_sum1 {0:.16f} '.format(error_sum1)
		temp0 = theta0 - new_temp0
		temp1 = theta1 - new_temp1
		# Update the parameters simultaneously
		theta0 = temp0
		theta1 = temp1
		i += 1
	print 'Number of iteration %d ' % (iter_)
	print 'Approximated theta0 %f ' % (theta0)
	print 'Approximated theta1 %f ' % (theta1)
	predicted_ = predict_f(theta0,theta1)
	accuracy_ = evaluate_f(predicted_,train_y)
	print 'Predicted Value%s \n' % predicted_
	print 'Actual Value %s \n' % train_y
	print'Accuracy : '+'{:.2%}'.format(accuracy_)
	


if __name__ == '__main__':
	generate_f()
	train_size = len(train_x)
	print train_x
	print train_y
	gsd_f()
