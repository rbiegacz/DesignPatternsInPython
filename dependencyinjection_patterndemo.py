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

""" this is an example of dependency injection pattern"""

from patterndemo import PatternDemo

class DependencyInjectionPatternDemo(PatternDemo):
    """ this class inherits after PatternDemo and runs the Dependency Injection Demo"""
    @staticmethod
    def pattern_info():
        """ this method delivers more information about this pattern """
        PatternDemo.pattern_info()
        print "This is an example of Dependency Injection Design Pattern"
    def pattern_run(self):
        """ this method runs the pattern """
        print "Dependency Injection not implemented yet"
