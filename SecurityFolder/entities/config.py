
import subprocess
windowname = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE, text=True).stdout.strip()
class TrainingPipelineConfig:
    pass

class DataIngestionConfig:
    pass

class DataTransformationConfig:
    pass

class DataValidationConfig:
    pass

class ModelDeploymentConfig:
    pass

class ModelEvaluationConfig:
    pass

class ModelTrainerConfig:
    pass


