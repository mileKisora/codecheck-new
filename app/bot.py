#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Bot():
  def __init__(self, command):
    self.__command = command["command"]
    self.__data = command["data"]
    self.__hash = 0
  def get_command(self):
    return self.__command
  def set_command(self, new_command):
    self.__command = new_command
  command =  property(get_command, set_command)
  def get_data(self):
    return self.__data
  def set_data(self, new_data):
    self.__data = new_data
  data =  property(get_data, set_data)
  def get_hash(self):
    return self.__hash
  def set_hash(self, new_hash):
    self.__hash = new_hash
  hash =  property(get_hash, set_hash)
  
  def generate_hash(self):
    def str2hash(s):
      buff = ""
      for c in s:
        buff+=str(ord(c))
      buff = self.scientificNotation(int(buff))
      if(type(buff) is str):
        buff = buff[2:].replace('e+','')
        buff = int(buff.lstrip('0'))
      return buff
    x = str2hash(self.__command)
    y = str2hash(self.__data)
    self.__hash = hex(x+y)[2:]
  def scientificNotation(self, num):
    data = "%.16e" % num
    result = data if (int(data.split("e+")[1]) > 20) else num
    return result
  