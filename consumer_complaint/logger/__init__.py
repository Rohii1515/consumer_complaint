"""
This section imports several Python modules that the script will use:
logging: Provides a flexible framework for emitting log messages from programs.
datetime: Allows working with dates and times.
os: Provides a way to interact with the operating system, used here for file and directory operations.
pandas as pd: Pandas is a library for data manipulation, but it's not used in this specific code.
consumer_complaint.constant: Imports a constant named TIMESTAMP from a module named constant within a package or module named consumer_complaint.
shutil: The shutil module in Python provides a higher-level interface for file operations. In the provided code, shutil is used to remove a directory 
"""

import logging
from datetime import datetime
import os
import pandas as pd
from consumer_complaint.constant import TIMESTAMP
import shutils


"""
This line defines a variable LOG_DIR with the value "logs," indicating the name of the directory where log files will be stored.
"""
LOG_DIR = "logs"


# Defining a function to generate a log file name based on the timestamp
"""
This defines a function get_log_file_name that, when called, returns a string representing the log file name. 
It includes the prefix "log_" and appends the TIMESTAMP constant.
"""
def get_log_file_name():
    return f"log_{TIMESTAMP}.log"


# Calling the function to get the log file name
"""
This line calls the get_log_file_name function and assigns its result to the variable LOG_FILE_NAME. 
This variable now holds the generated log file name.
"""
LOG_FILE_NAME = get_log_file_name()


# Checking if the log directory already exists and creating it if not
"""
These lines check if the directory specified by LOG_DIR already exists. 
If it does, it removes the entire directory (shutil.rmtree). Then, 
it creates a new directory with the same name using os.makedirs, 
or it ignores the creation if the directory already exists (exist_ok=True).
"""
if os.path.exists(LOG_DIR):
    shutils.rmtree(LOG_DIR)
os.makedirs(LOG_DIR, exist_ok=True)


# Creating the full path to the log file
"""
This line uses os.path.join to concatenate the log directory (LOG_DIR) and the log file name (LOG_FILE_NAME), creating the full path to the log file. 
The result is stored in the variable LOG_FILE_PATH.
"""
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)


# Configuring the logging system
"""
This block configures the logging system using basicConfig. It sets up:
filename: Specifies the file where log messages will be written (here, it's the path to the log file we created earlier).
filemode: Specifies the file opening mode. "w" means write, which creates a new file or truncates an existing one.
format: Defines the format of log messages, including timestamp, log level, line number, file name, function name, and the log message itself.
level: Sets the logging level to INFO, meaning messages with severity INFO and above will be recorded.
"""
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format="[%(asctime)s] \t%(levelname)s \t%(lineno)d \t%(filename)s \t%(funcName)s() \t%(message)s",
    level=logging.INFO,
)


# Creating a logger object
"""
This line creates a logger object named "ConsumerComplaint." 
The logger is an instance of the Logger class provided by the logging module. 
You can use this logger object (logger) to emit log messages throughout script.
"""
logger = logging.getLogger("ConsumerComplaint")
