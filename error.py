import string
from SWR import *
# ANSI color codes
RED = '\033[91m'
RESET = '\033[0m'

#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS
class Error:
  
  def __init__(self, pos_start, pos_end, error_name, details):
    self.pos_start = pos_start
    self.pos_end = pos_end
    self.error_name = error_name
    self.details = details
  
  
  def as_string(self):
    result  = f'{RED}{self.error_name}: {self.details}\n'
    result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}{RESET}'
    result += '\n\n' + string_with_arrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
    return result

class IllegalCharError(Error):
  
  def __init__(self, pos_start, pos_end, details):
    super().__init__(pos_start, pos_end, f'{RED}Kor/IllegalCharError', details)

class ExpectedCharError(Error):
  
  def __init__(self, pos_start, pos_end, details):
    super().__init__(pos_start, pos_end, f'{RED}Kor/ExpectedCharError', details)

class InvalidSyntaxError(Error):
  
  def __init__(self, pos_start, pos_end, details=''):
    super().__init__(pos_start, pos_end, f'{RED}Kor/InvalidSyntaxError', details)

class RTError(Error):
  
  def __init__(self, pos_start, pos_end, details, context):
    super().__init__(pos_start, pos_end, f'{RED}Kor/RuntimeError', details)
    self.context = context

  
  def as_string(self):
    result  = self.generate_traceback()
    result += f'{RED}{self.error_name}: {self.details}\n'
    result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}{RESET}'
    return result

  
  def generate_traceback(self):
    result = ''
    pos = self.pos_start
    ctx = self.context

    while ctx:
      result = f'  File {pos.fn}, line {str(pos.ln + 1)}, in {ctx.display_name}\n' + result
      pos = ctx.parent_entry_pos
      ctx = ctx.parent

    return f'{RED}Traceback (most recent call last):\n{result}{RESET}'

class ExtentionError(Error):
  
  def __init__(self, extention):
    print(f"{RED}Kor/ExtentionError: {extention} is not a valid extention, please use '.ko' extention{RESET}")