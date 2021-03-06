from models import base
import sys
import subprocess
import os
import os.path

from controllers.config_controller import config_controller

class wakeup_sysexec_component(base.base) :
    def __init__(self, controller) :
        super().__init__()
        self.controller = controller


    def initialize(self):
        pass

    def reboot(self, argvs):
        exec_str = self.get_exec_str()
        exec_str.extend(argvs)
        exec_str.append(config_controller.get_project_dir() + 'source')
        self.new_instance(exec_str)
        


    def get_exec_str(self) :
        result_args = []
        dir_path = config_controller.get_project_dir() + 'source/wakeup/'
        if sys.platform[0:3] == 'win' :
            dir_path = dir_path + 'batches/reboot.bat'
        else:
            dir_path = dir_path + 'batches/reboot.sh' 
            result_args.append('sh')

        result_args.append(dir_path)
        return result_args

    @staticmethod
    def new_instance(argvs) :
        msg = ''
        for it in argvs :
            msg = msg + it + ' '
        print(msg)
        subprocess.Popen(argvs)
