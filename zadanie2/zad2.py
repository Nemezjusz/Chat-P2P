import rsa
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

tajna_wiadomosc = b'\xe3\x12\x1dOc\xe76e\x9a\xb6\x82\x10\x87E\xd3\xa8'
aes_zaszyfrowany = b'\x17\xc4\xb6\xa6nK\xd9d2\x89:\xdf\n.%h\xb7)\x8e\x1f\x04\x92\xe3B\x0b\x07\x98\xa9gR\x9ar\xbb\x03\x03\xdca\xdeblM3t\x9c\xe2s\x12\xf9\xab\xb4\xc2\x0fdp\x05\x8e\xa0\x9e\xd9\xd2\xec\x0fD\x0c'
klucz_prywatny = rsa.PrivateKey(9997149424529136631614335470903663927295617380062087932900249811350740188441458017737386555179230970100243882831707250487788985636597140949517849032436997, 65537, 95338791679977881116910442487675510849745347857527884371616890185608322227723539656394617503281826574369678998675240606396730641294725738577802235760973, 6300149826612760702025869091128594479487566557740232530610817473856603222258439807, 1586811377453232169844504359286253902953280397364127761926237146573890171)

