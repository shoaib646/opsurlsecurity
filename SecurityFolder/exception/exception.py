import sys



class NetworkException(Exception):
    def __init__(self, error_message, error_details):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.line_no = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error: str({self.error_message}), File {self.filename}, Line {self.line_no}"

