from deepface import DeepFace

DeepFace.stream(db_path="DATA", detector_backend = 'mtcnn')#opencv,mtcnn
#DeepFace.stream("Nitish", detector_backend = 'mtcnn')#opencv,mtcnn 
#DeepFace.stream("dataset", detector_backend = 'ssd')
#DeepFace.stream("dataset", detector_backend = 'mtcnn')
#DeepFace.stream("dataset", detector_backend = 'dlib')
#DeepFace.stream("dataset", detector_backend = 'retinaface')