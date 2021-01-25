import sys
sys.path.append('app/')

from application import app as api

if _name_ == "_main_":
        api.run()
