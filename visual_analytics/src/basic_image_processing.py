# Importing packages
import os

from pathlib import Path
import argparse

import numpy as np
import cv2

class Assignment2:

    def __init__(self, data_dir=None):

        self.data_dir = data_dir

        if data_dir is None:

            data_dir = self.setting_default_data_dir()

        files = self.get_filepaths_from_data_dir(data_dir, file_extension="")

        filenames = self.get_filenames(files)

        image_shapes = self.get_width_height_and_n_channels(files)



    def setting_default_data_dir(self):

        root_dir = Path.cwd()  # Setting root directory.

        data_dir = root_dir / "data" / "makeup"  # Setting data directory.

        return data_dir

    def get_filepaths_from_data_dir(self, data_dir, file_extension="*.jpeg"):
        """Creates a list containing paths to filenames in a data directoryl

        Args:
            data_dir (PosixPath): PosixPath to the data directory.
            file_extension (str): A string with the given file extension you want to extract.
        """

        files = [file for file in data_dir.glob(file_extension) if file.is_file()]  # Using list comprehension to get all the file names if they are files.

        return files

    def get_filenames(self, files):
        """Creates a list of filenames in a directory.

        Args:
            files (list): List of file paths

        Returns:
            filename: list of filenames
        """

        filenames = []  # Creating empty list

        # Loop for iterating through the different files.
        for file in files:

            novel_file_name = os.path.split(file)[-1]  # I take the last snippet of the path, which is the novel filename.

            filenames.append(novel_file_name)  # Append each filename to the list.

        return filenames

    def load_images(files):

        images = []

        for file in files:

            img = cv2.imread(str(file))

            images.append(img)

        return images



    def get_width_height_and_n_channels(images):

        image_shapes = []

        for file in files:

            img = cv2.imread(str(file))

            image_shape = img.shape

            image_shapes.append(image_shape)

        return image_shapes





