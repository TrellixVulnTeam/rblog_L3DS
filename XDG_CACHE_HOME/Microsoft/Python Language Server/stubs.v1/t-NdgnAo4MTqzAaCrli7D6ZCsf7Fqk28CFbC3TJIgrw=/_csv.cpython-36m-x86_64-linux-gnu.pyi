import builtins as _mod_builtins

class Dialect(_mod_builtins.object):
    'CSV dialect\n\nThe Dialect type records CSV parsing and generation options.\n'
    __class__ = Dialect
    def __init__(self, *args, **kwargs):
        'CSV dialect\n\nThe Dialect type records CSV parsing and generation options.\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def delimiter(self):
        pass
    
    @property
    def doublequote(self):
        pass
    
    @property
    def escapechar(self):
        pass
    
    @property
    def lineterminator(self):
        pass
    
    @property
    def quotechar(self):
        pass
    
    @property
    def quoting(self):
        pass
    
    @property
    def skipinitialspace(self):
        pass
    
    @property
    def strict(self):
        pass
    

class Error(_mod_builtins.Exception):
    __class__ = Error
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_csv'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

QUOTE_ALL = 1
QUOTE_MINIMAL = 0
QUOTE_NONE = 3
QUOTE_NONNUMERIC = 2
__doc__ = 'CSV parsing and writing.\n\nThis module provides classes that assist in the reading and writing\nof Comma Separated Value (CSV) files, and implements the interface\ndescribed by PEP 305.  Although many CSV files are simple to parse,\nthe format is not formally defined by a stable specification and\nis subtle enough that parsing lines of a CSV file with something\nlike line.split(",") is bound to fail.  The module supports three\nbasic APIs: reading, writing, and registration of dialects.\n\n\nDIALECT REGISTRATION:\n\nReaders and writers support a dialect argument, which is a convenient\nhandle on a group of settings.  When the dialect argument is a string,\nit identifies one of the dialects previously registered with the module.\nIf it is a class or instance, the attributes of the argument are used as\nthe settings for the reader or writer:\n\n    class excel:\n        delimiter = \',\'\n        quotechar = \'"\'\n        escapechar = None\n        doublequote = True\n        skipinitialspace = False\n        lineterminator = \'\\r\\n\'\n        quoting = QUOTE_MINIMAL\n\nSETTINGS:\n\n    * quotechar - specifies a one-character string to use as the \n        quoting character.  It defaults to \'"\'.\n    * delimiter - specifies a one-character string to use as the \n        field separator.  It defaults to \',\'.\n    * skipinitialspace - specifies how to interpret whitespace which\n        immediately follows a delimiter.  It defaults to False, which\n        means that whitespace immediately following a delimiter is part\n        of the following field.\n    * lineterminator -  specifies the character sequence which should \n        terminate rows.\n    * quoting - controls when quotes should be generated by the writer.\n        It can take on any of the following module constants:\n\n        csv.QUOTE_MINIMAL means only when required, for example, when a\n            field contains either the quotechar or the delimiter\n        csv.QUOTE_ALL means that quotes are always placed around fields.\n        csv.QUOTE_NONNUMERIC means that quotes are always placed around\n            fields which do not parse as integers or floating point\n            numbers.\n        csv.QUOTE_NONE means that quotes are never placed around fields.\n    * escapechar - specifies a one-character string used to escape \n        the delimiter when quoting is set to QUOTE_NONE.\n    * doublequote - controls the handling of quotes inside fields.  When\n        True, two consecutive quotes are interpreted as one during read,\n        and when writing, each quote character embedded in the data is\n        written as two quotes\n'
__file__ = '/home/rahul/code/ablog/env/lib/python3.6/lib-dynload/_csv.cpython-36m-x86_64-linux-gnu.so'
__name__ = '_csv'
__package__ = ''
__version__ = '1.0'
_dialects = _mod_builtins.dict()
def field_size_limit():
    'Sets an upper limit on parsed fields.\n    csv.field_size_limit([limit])\n\nReturns old limit. If limit is not given, no new limit is set and\nthe old limit is returned'
    pass

def get_dialect():
    'Return the dialect instance associated with name.\n    dialect = csv.get_dialect(name)'
    pass

def list_dialects():
    'Return a list of all know dialect names.\n    names = csv.list_dialects()'
    pass

def reader():
    '    csv_reader = reader(iterable [, dialect=\'excel\']\n                        [optional keyword args])\n    for row in csv_reader:\n        process(row)\n\nThe "iterable" argument can be any object that returns a line\nof input for each iteration, such as a file object or a list.  The\noptional "dialect" parameter is discussed below.  The function\nalso accepts optional keyword arguments which override settings\nprovided by the dialect.\n\nThe returned object is an iterator.  Each iteration returns a row\nof the CSV file (which can span multiple input lines).\n'
    pass

def register_dialect():
    'Create a mapping from a string name to a dialect class.\n    dialect = csv.register_dialect(name[, dialect[, **fmtparams]])'
    pass

def unregister_dialect():
    'Delete the name/dialect mapping associated with a string name.\n    csv.unregister_dialect(name)'
    pass

def writer():
    '    csv_writer = csv.writer(fileobj [, dialect=\'excel\']\n                            [optional keyword args])\n    for row in sequence:\n        csv_writer.writerow(row)\n\n    [or]\n\n    csv_writer = csv.writer(fileobj [, dialect=\'excel\']\n                            [optional keyword args])\n    csv_writer.writerows(rows)\n\nThe "fileobj" argument can be any object that supports the file API.\n'
    pass

