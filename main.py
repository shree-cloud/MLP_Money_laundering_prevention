from elleptic.logger import logging
from elleptic.exception import ElepticException
import os,sys

def test():
     try:
          logging.info("start test log")
          result = 3/0
          print(result)
          logging.info("stop test log")

     except Exception as e:
          logging.debug("str")
          raise ElepticException(e, sys)

if __name__=="__main__":
     try:
          test()
     except Exception as e:
          print(e)