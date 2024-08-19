
import subprocess
windowname = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE, text=True).stdout.strip()



class DataIngestionArtifact:
    pass

class DataTransformationArtifact:
    pass

class DataValidationArtifact:
    pass

class ModelDeploymentArtifact:
    pass

class ModelEvaluationArtifact:
    pass

class ModelTrainerArtifact:
    pass


