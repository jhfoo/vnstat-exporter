# core
import argparse
# public
import uvicorn
# custom
import src.lib.util as util
import src.lib.appinit as appinit
import src.lib.api as api


if __name__ == '__main__':
  aparser = argparse.ArgumentParser(description='vnstat export daemon')
  aparser.add_argument('-d', nargs='?', const=False)
  # print (aparser.parse_args())
  util.BaseValidations()

app = appinit.init()
api.init(app)