import time
import argparse
import daemon
import logging
import uvicorn
from fastapi import FastAPI

logging.basicConfig(filename='/home/jhfoo/test.log', encoding='utf-8', level=logging.DEBUG)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
  aparser = argparse.ArgumentParser(description='vnstat export daemon')
  aparser.add_argument('-d', '--daemon', help='Run as daemon', action='store_true')
  ParsedArgs = aparser.parse_args()

  if ParsedArgs.daemon:
    with daemon.DaemonContext(
      working_directory='/home/jhfoo/vnstat-exporter/src'
    ):
      try:
        uvicorn.run('test:app', host = '0.0.0.0', port = 8088, log_level = 'info', reload=True)
      except BaseException as err:
        log.error(err)
  else:
    uvicorn.run('test:app', host = '0.0.0.0', port = 8088, log_level = 'info', reload=True)

else:
  log.debug ('This is not the main process: {}'.format(__name__))
  global app
  app = FastAPI()

  @app.get('/')
  def getDefault():
    return 'ok'