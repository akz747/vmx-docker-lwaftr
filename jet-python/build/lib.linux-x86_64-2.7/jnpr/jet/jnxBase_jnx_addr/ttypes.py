#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class JnxBaseAddressFormat:
  ADDRESS_STRING = 0
  ADDRESS_BYTES = 1

  _VALUES_TO_NAMES = {
    0: "ADDRESS_STRING",
    1: "ADDRESS_BYTES",
  }

  _NAMES_TO_VALUES = {
    "ADDRESS_STRING": 0,
    "ADDRESS_BYTES": 1,
  }

class JnxBaseAfType:
  AF_UNSPECIFIED = 0
  AF_INET = 1
  AF_INET6 = 2
  AF_MAC = 3

  _VALUES_TO_NAMES = {
    0: "AF_UNSPECIFIED",
    1: "AF_INET",
    2: "AF_INET6",
    3: "AF_MAC",
  }

  _NAMES_TO_VALUES = {
    "AF_UNSPECIFIED": 0,
    "AF_INET": 1,
    "AF_INET6": 2,
    "AF_MAC": 3,
  }


class IpAddressAddrFormat:
  """
  Attributes:
   - addr_string
   - addr_bytes
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'addr_string', None, None, ), # 1
    (2, TType.STRING, 'addr_bytes', None, None, ), # 2
  )

  def __init__(self, addr_string=None, addr_bytes=None,):
    self.addr_string = addr_string
    self.addr_bytes = addr_bytes

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.addr_string = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.addr_bytes = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IpAddressAddrFormat')
    if self.addr_string is not None:
      oprot.writeFieldBegin('addr_string', TType.STRING, 1)
      oprot.writeString(self.addr_string)
      oprot.writeFieldEnd()
    if self.addr_bytes is not None:
      oprot.writeFieldBegin('addr_bytes', TType.STRING, 2)
      oprot.writeString(self.addr_bytes)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class JnxBaseIpAddress:
  """
  Attributes:
   - AddrFormat
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'AddrFormat', (IpAddressAddrFormat, IpAddressAddrFormat.thrift_spec), None, ), # 1
  )

  def __init__(self, AddrFormat=None,):
    self.AddrFormat = AddrFormat

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.AddrFormat = IpAddressAddrFormat()
          self.AddrFormat.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('JnxBaseIpAddress')
    if self.AddrFormat is not None:
      oprot.writeFieldBegin('AddrFormat', TType.STRUCT, 1)
      self.AddrFormat.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class MacAddressAddrFormat:
  """
  Attributes:
   - addr_string
   - addr_bytes
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'addr_string', None, None, ), # 1
    (2, TType.STRING, 'addr_bytes', None, None, ), # 2
  )

  def __init__(self, addr_string=None, addr_bytes=None,):
    self.addr_string = addr_string
    self.addr_bytes = addr_bytes

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.addr_string = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.addr_bytes = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('MacAddressAddrFormat')
    if self.addr_string is not None:
      oprot.writeFieldBegin('addr_string', TType.STRING, 1)
      oprot.writeString(self.addr_string)
      oprot.writeFieldEnd()
    if self.addr_bytes is not None:
      oprot.writeFieldBegin('addr_bytes', TType.STRING, 2)
      oprot.writeString(self.addr_bytes)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class JnxBaseMacAddress:
  """
  Attributes:
   - AddrFormat
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'AddrFormat', (MacAddressAddrFormat, MacAddressAddrFormat.thrift_spec), None, ), # 1
  )

  def __init__(self, AddrFormat=None,):
    self.AddrFormat = AddrFormat

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.AddrFormat = MacAddressAddrFormat()
          self.AddrFormat.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('JnxBaseMacAddress')
    if self.AddrFormat is not None:
      oprot.writeFieldBegin('AddrFormat', TType.STRUCT, 1)
      self.AddrFormat.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
