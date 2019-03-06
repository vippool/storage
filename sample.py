#========================================================#
#                                                        #
#  sample.py - サンプルプログラム                        #
#                                                        #
#                            (C) 2019-2019 VIPPOOL Inc.  #
#                                                        #
#========================================================#

import os
from vippool.storage import vippool_storage

# 新規にコインアドレスを作成する
vs = vippool_storage( coind_type = 'monacoind_test' )
print vs.privKey() # 秘密鍵を取得
print vs.address() # コインアドレスを取得

# 既にある秘密鍵からインスタンスを生成
if os.getenv( 'PRIVKEY', None ) is None:
	vs = vippool_storage( privKey = '74657a79fd323d5072ca81c6b99e2ffb5f0735d16fd5963289ba6f837c0413ef' )
else:
	vs = vippool_storage( 'monacoind_test', os.getenv( 'PRIVKEY' ) )
print vs.privKey()
print vs.address()
print vs.balance() # 残高取得
#print vs.send( 'mt5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 1.0, 0.01 ) # 1.0 MONA を手数料 0.01 MONA で送金
#print vs.write( 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0.01 ) # 手数料 0.01 MONA で任意データ書き込み
print vs.read( '39a6c92e1fc13406b23e53812a242e7b7253b948135c5b58db9013dce8241b9a' ) # 書いたデータを読み込む
