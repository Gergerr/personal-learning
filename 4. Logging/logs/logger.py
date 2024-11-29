# Configure logging
import logging
logging.basicConfig(
    filename= 'app.log', 
    filemode= 'w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',  # Optional, specifies the timestamp format
    force= True # bruh must force
)

