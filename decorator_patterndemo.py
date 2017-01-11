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

"""This script implements a simple example showing how docorator pattern works"""

from patterndemo import PatternDemo


def logging(logging_prefix, logging_suffix):
    """Implementation of logging decorator"""
    def logging_decorator(func):
        """decorator generator function"""
        def func_wrapper(name):
            """wrapping function used by decorator"""
            return "{0}{1}{2}".format(logging_prefix, func(name), logging_suffix)
        return func_wrapper
    return logging_decorator

@logging(">>> Info:", ".")
def loginfo(text):
    """ Example showing usage of logging decorator (info level)"""
    return text

@logging(">>> Warning:", "?")
def logwarning(text):
    """ Example showing usage of logging decorator (warning level)"""
    return text

@logging(">>> Error:", "!")
def logerror(text):
    """ Example showing usage of logging decorator (error level)"""
    return text

class DecoratorPatternDemo(PatternDemo):
    """ Demo class for Decorator Pattern; it inherits after PatternDemo"""
    @staticmethod
    def pattern_info():
        PatternDemo.pattern_info()
        print "This is an example of Decorator Design Pattern"
        print "Insipired by http://thecodeship.com/patterns/guide-to-python-function-decorators/"
    def pattern_run(self):
        print loginfo("Decorator Pattern is cool")
        print logwarning("There might be a problem w/ Decorator pattern")
        print logerror("Your Decorator has a problem")
