import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.shape != v2.shape:
		raise ValueError("Input vectors must have the same shape.")

	if v1.size == 0 or v2.size == 0:
		raise ValueError("Input vectors cannot be empty.")

	l2_norm_v1 = np.sqrt(np.sum(np.abs(v1) ** 2))
	l2_norm_v2 = np.sqrt(np.sum(np.abs(v2) ** 2))

	if l2_norm_v1 == 0 or l2_norm_v2 == 0:
		raise ValueError("Input vectors cannot have zero magnitude.")
	
	dot_product = np.dot(v1, v2)

	return float(dot_product / (l2_norm_v1 * l2_norm_v2))