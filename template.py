import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

Project_name = "mlproject"

list_of_files= [
    f"src/{Project_name}/___init__.py",
    f"src/{Project_name}/componets/__init__.py",
    f"src/{Project_name}/componets/data_ingestion.py",
    f"src/{Project_name}/componets/data_transformation.py",
    f"src/{Project_name}/componets/model_trainer.py",
    f"src/{Project_name}/componets/model_monitoring.py",
    f"src/{Project_name}/pipelines/__init__.py",
    f"src/{Project_name}/pipelines/taining_pipeline.py",
    f"src/{Project_name}/pipelines/prediction_pipeline.py",
    f"src/{Project_name}/exception.py",
    f"src/{Project_name}/logger.py",
    f"src/{Project_name}/utils.py",
    "main.py",
    "app.py",
    "dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Create directory:{filedir} for the file {filename}")
        
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
    
    else:
        logging.info(f"{filename}is already exists")
        
        