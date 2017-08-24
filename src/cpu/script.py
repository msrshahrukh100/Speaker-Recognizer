from pyAudioAnalysis import audioTrainTest as aT
import os
from pydub import AudioSegment

# print os.listdir("audiofiles/nauman/")
def splitfiles(path) :

	files = os.listdir(path)
	if len(files) == 1 :
		for i in range(6) :
			t1 = i * 10 * 1000
			t2 = (t1 + 10) * 1000
			newAudio = AudioSegment.from_wav(path + "/" +files[0])
			newAudio = newAudio[t1:t2]
			newAudio.export(path +"/"+ files[0].split(".")[0]+str(i)+'.wav', format="wav") 



def main() :
	main_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'media','data'))
	# print main_path
	training_files_path_list = [main_path+"/"+x for x in os.listdir(main_path)]
	# print training_files_path_list
	for i in training_files_path_list :
		splitfiles(i)

	aT.featureAndTrain(training_files_path_list, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm_rbf", "svmforspeakerrecognition", True)


def classify(filepath) :
	classifier_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'svmforspeakerrecognition'))
	return aT.fileClassification(filepath, classifier_path,"svm_rbf")