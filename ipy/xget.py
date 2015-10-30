def xget(data, columns, default=None, seq=True):
    '''if seq==True data is treated as sequence of data, otherwise data is single dict or list
       if columns is sequence, xget returns projection of data sequence containing only that columns
       if columns is string, xget treats it like 'a.b.c.d' field indirection in dictionary (maybe jsonpath in future?)
       if columns is int, xget returns specified column in each data element'''

    fdef = (lambda d: default) if not callable(default) else default

    if hasattr(data, '__iter__') and not hasattr(data, 'keys') and seq:
        if hasattr(columns, '__iter__'):
            return [{k: xget(d, k, fdef(d), seq) for k in columns} for d in data]
        else:
            return [xget(d, columns, fdef(d), seq=False) for d in data]
    else:
        if hasattr(columns, '__iter__'):
            return {k: xget(data, k) for k in columns}
        else:
            if isinstance(columns,str):
                try:
                    r = data
                    for pp in columns.split('.'):
                        r = r[pp]
                    return r
                except:
                    return fdef(data)
            else:
                if isinstance(data, str):
                    return fdef(data)
                try:
                    r = data
                    return r[columns]
                except:
                    return fdef(data)

def pxget(columns, default=None, seq=True):
    f = lambda data: xget(data, columns, default, seq)
    return f

if __name__ == '__main__':
    print 'a', '=', xget(dict(a='a'),'a')
    print 'a.b', '=', xget(dict(a=dict(b='a.b')), 'a.b')
    print '{b:a.b}', '=', xget(dict(a=dict(b='a.b')), 'a')

    print 'a,c', '=', xget([['a','b'],['c','d']], 0)
    print 'a,None', '=', xget([dict(a='a',b='b'), dict(c='c',d='d')], 'a')
    print 'None,c', '=', xget([dict(a='a',b='b'), dict(c='c',d='d')], 'c')

    print 'a4, c', '=', xget([['a'],['b','c']], 1, default=lambda r: map(lambda r1:r1+'4', r))


