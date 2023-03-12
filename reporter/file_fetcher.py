import json
from pandas import json_normalize
import jinja2 as jinja


class FileFetcher:
    def get_json_data_to_dataframe(self, filename):
        """
        Reads a JSON file from the "data_samples" directory, normalizes it using pandas,
        and returns the resulting dataframe.

        Args:
            filename (str): The name of the JSON file to read.

        Returns:
            pandas.DataFrame: A normalized dataframe representing the data in the JSON file.
        """
        data = json.load(open("data_samples/" + filename))
        df = json_normalize(data)
        return df

    def get_json_data(self, filename):
        """
        Reads a JSON file from the "data_samples" directory and returns its contents as a dict.

        Args:
            filename (str): The name of the JSON file to read.

        Returns:
            dict: A dictionary representing the contents of the JSON file.
        """
        data = json.load(open("data_samples/" + filename))
        return data

    def get_template(self, filename):
        """
        Loads a Jinja template from the "reporter/templates" directory and returns it.

        Args:
            filename (str): The name of the Jinja template to load.

        Returns:
            jinja2.Template: A Jinja template object representing the template file.
        """
        environment = jinja.Environment(
            loader=jinja.FileSystemLoader("reporter/templates/")
        )
        template = environment.get_template(filename)
        return template

    def get_css(self, filename):
        """
        Reads a CSS file from the "data_samples" directory and returns its contents as a string.

        Args:
            filename (str): The name of the CSS file to read.

        Returns:
            str: A string representing the contents of the CSS file.
        """
        css_file = open("data_samples/" + filename)
        css = css_file.read()
        return css

    def get_string_from_file(self, file):
        """
        Reads a file and returns its contents as a string.

        Args:
            file (file): The file object to read from.

        Returns:
            str: A string representing the contents of the file.
        """
        read_content = file.read()
        return read_content
