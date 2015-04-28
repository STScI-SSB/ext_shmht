# using Pandokia - http://ssb.stsci.edu/testing/pandokia
#
# using this feature:
# http://ssb.stsci.edu/testing/pandokia/docs_new/runner_minipyt.html#linear-execution-in-sequential-code-with-statement
#
import pandokia.helpers.pycode as pycode
from   pandokia.helpers.filecomp import safe_rm

import shmht

testfile = 'test_shmht.dat'

safe_rm(testfile)

with pycode.test('open-error') :

    try :
        ident = shmht.open( testfile )

    except shmht.error as e :
        pass

    else :
        assert False, 'should have raised an exception'

with pycode.test('open-init') :

    ident = shmht.open( testfile, 10 )

with pycode.test('insert-lookup') :

    shmht.setval( ident, 'arf', 'data for arf' )
    assert shmht.getval( ident, 'arf' ) == 'data for arf'

    shmht.setval( ident, 'narf', 'data for narf' )
    assert shmht.getval( ident, 'narf' ) == 'data for narf'

    assert shmht.getval( ident, 'arf' ) == 'data for arf'
    assert shmht.getval( ident, 'narf' ) == 'data for narf'

with pycode.test('iter-small') :
    d = { }
    def collect( key, value ):
        d[key] = value

    shmht.foreach( ident, collect )

    print d
    assert d == { 'arf' : 'data for arf', 'narf' : 'data for narf' }

with pycode.test('remove') :
    shmht.remove( ident, 'arf' )
    assert shmht.getval( ident, 'arf' ) == None
    assert shmht.getval( ident, 'narf' ) == 'data for narf'
    shmht.remove( ident, 'narf' )
    assert shmht.getval( ident, 'arf' ) == None
    assert shmht.getval( ident, 'narf' ) == None

    def collect( key, value ):
        assert 0, 'somehow found %s : %s'% (key, value)

    shmht.foreach( ident, collect )

with pycode.test('fill') :
    for x in range(57):
        shmht.setval( ident, str(x), str(x)+' data' )
