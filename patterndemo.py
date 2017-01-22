#
# Copyright (c) 2016 Rafal Biegacz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

""" this is a demo template; each demo needs to inherit after this class """

from abc import ABCMeta, abstractmethod

class PatternDemo:
    """ this is a demo template; each demo needs to inherit after this class """
    __metaclass__ = ABCMeta
    pattern_name = ""
    def __init__(self, name):
        """ constructor in Pattern Demo class, the second argument is a name for a demo """
        self.pattern_name = name
    @staticmethod
    def pattern_info():
        """ common info formating for all demos"""
        print "\n--------------------------------------------"
    @abstractmethod
    def pattern_run(self):
        """ each demo needs to implement PatternRun function"""
        pass
    