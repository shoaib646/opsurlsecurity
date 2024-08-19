
import subprocess
windowname = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE, text=True).stdout.strip()



from dataclasses import dataclass





@dataclass
class DataIngestionArtifact:
    pass

@dataclass
class DataValidationArtifact:
    pass

@dataclass
class DataTransformationArtifact:
    pass

@dataclass
class ModelTrainerArtifact:
    pass

@dataclass
class ModelEvaluationArtifact:
    pass

@dataclass
class ModelRegistrytArtifact:
    pass






