#========================================================#
#                                                        #
#  test.py - vippool_storage 動作テスト                  #
#                                                        #
#                            (C) 2019-2021 VIPPOOL Inc.  #
#                                                        #
#========================================================#

# ライブラリのインポート
import sys
sys.path.append( '..' )
from vippool import storage

# ECDSA のテスト
storage.ECDSA.selfTest()
