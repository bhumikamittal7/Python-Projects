#======================== Python Library =============================
import filecmp
import os.path
import subprocess

#======== check if the contents of the file matches =====================
def check_output(expected_output_file, actual_output_file):
	if os.path.exists(expected_output_file) == True and os.path.exists(actual_output_file) == True: 
		if filecmp.cmp(expected_output_file, actual_output_file):
			return True
		else:
			return False
	elif os.path.exists(expected_output_file) == False and os.path.exists(actual_output_file) == False:
		return True
	else:
		return False

#========= return path to output file =========================
def generate_output(path_to_python_program, path_to_input_file):
	emptyFile = ''
	if os.path.exists(path_to_input_file) == True:
		try:
			with open('actual_output_file.txt', 'w') as outFile:
				subprocess.run(path_to_python_program, input=bytes(open(path_to_input_file, "r").read(), encoding= 'utf-8'), shell=True, stdout=outFile, timeout = 5, stderr = subprocess.DEVNULL)
			return str(os.path.abspath('actual_output_file.txt'))
		except:
			with open('actual_output_file.txt', 'w') as outFile:
				emptyFile
			return str(os.path.abspath('actual_output_file.txt'))
	else:
		with open('actual_output_file.txt', 'w') as outFile:
			emptyFile
		return str(os.path.abspath('actual_output_file.txt'))

#============================ checker ========================================
def check(path_to_python_program, path_to_input_file, path_to_expected_output_file):
	return(check_output(path_to_expected_output_file, generate_output(path_to_python_program, path_to_input_file)))
