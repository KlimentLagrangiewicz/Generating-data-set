from sklearn.datasets import make_blobs, make_swiss_roll, make_moons
import sys, csv


def write_matrix_and_array_to_csv(matrix, array, filename):
	"""
	Writes a matrix (n x m) and an array (n elements) to a CSV-file.
	Each element of the array is added to the end of the corresponding row of the matrix.
	
	Function arguments:
	matrix (list of lists): 2D data matrix
	array (list): 1D data array
	filename (str): filename to save
	"""
	if len(matrix) != len(array):
		raise ValueError("The number of rows in the matrix must match the length of the array")
	with open(filename, 'w', newline='\n', encoding='utf-8') as csvfile:
		writer = csv.writer(csvfile)
		for row, value in zip(matrix, array):
			writer.writerow([*row, value])

if __name__ == "__main__":
	try:
		if (int(len(sys.argv)) < 3):
			print("Not enough parameters...\n")
			sys.exit(1)
		if int(sys.argv[1]) == 0:
			x, y = make_moons(n_samples = int(sys.argv[2]))
			write_matrix_and_array_to_csv(x, y, 'testMoons_' + sys.argv[2] + '.csv')
		elif int(sys.argv[1]) == 1:
			x, y = make_swiss_roll(n_samples = int(sys.argv[2]))
			write_matrix_and_array_to_csv(x, y, 'testSwissRoll_' + sys.argv[2] + '.csv')
		else:
			if (int(len(sys.argv)) > 4):
				x, y = make_blobs(n_samples = int(sys.argv[2]), centers = int(sys.argv[4]), n_features = int(sys.argv[3]), random_state = 0)
				write_matrix_and_array_to_csv(x, y, 'testBlobs_' + sys.argv[2] + "_" + sys.argv[3] + "_" + sys.argv[4] + '.csv')
			elif (int(len(sys.argv)) > 3):
				x, y = make_blobs(n_samples = int(sys.argv[2]), centers = 2, n_features = int(sys.argv[3]), random_state = 0)
				write_matrix_and_array_to_csv(x, y, 'testBlobs_' + sys.argv[2] + "_" + sys.argv[3] + "_2" + '.csv')
			else:
				x, y = make_blobs(n_samples = int(sys.argv[2]), centers = 2, n_features = 2, random_state = 0)
				write_matrix_and_array_to_csv(x, y, 'testBlobs_' + sys.argv[2] + "_2_2" + '.csv')
	except:
		print("Something went wrong...")
