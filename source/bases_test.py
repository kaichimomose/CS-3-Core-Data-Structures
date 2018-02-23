#!python

from bases import decode, encode, convert
import unittest


class BasesDecodeTest(unittest.TestCase):

    def test_decode_binary(self):
        assert decode('0', 2) == 0
        assert decode('1', 2) == 1
        assert decode('10', 2) == 2
        assert decode('11', 2) == 3
        assert decode('100', 2) == 4
        assert decode('101', 2) == 5
        assert decode('110', 2) == 6
        assert decode('111', 2) == 7
        assert decode('1000', 2) == 8
        assert decode('1001', 2) == 9
        assert decode('1010', 2) == 10
        assert decode('1011', 2) == 11
        assert decode('1100', 2) == 12
        assert decode('1101', 2) == 13
        assert decode('1110', 2) == 14
        assert decode('1111', 2) == 15
        assert decode('111010100101', 2) == 3749
        assert decode('11010110100', 2) == 1716
        assert decode('11010110101', 2) == 1717
        assert decode('11010110110', 2) == 1718
        assert decode('111111010101101011', 2) == 259435
        assert decode('111001000101101011', 2) == 233835
        assert decode('10101011110010111', 2) == 87959
        assert decode('10011100010000', 2) == 10000
        assert decode('1111111111111111', 2) == 65535
        assert decode('1111111111111111000111011', 2) == 33553979

    def test_decode_decimal(self):
        assert decode('5', 10) == 5
        assert decode('9', 10) == 9
        assert decode('10', 10) == 10
        assert decode('25', 10) == 25
        assert decode('64', 10) == 64
        assert decode('99', 10) == 99
        assert decode('123', 10) == 123
        assert decode('789', 10) == 789
        assert decode('2345', 10) == 2345
        assert decode('6789', 10) == 6789
        assert decode('13579', 10) == 13579
        assert decode('24680', 10) == 24680
        assert decode('38737', 10) == 38737
        assert decode('8724568267', 10) == 8724568267
        assert decode('234587238', 10) == 234587238
        assert decode('345235254', 10) == 345235254
        assert decode('5645747675797', 10) == 5645747675797
        assert decode('8987567453', 10) == 8987567453
        assert decode('68980787567', 10) == 68980787567
        assert decode('645443567878', 10) == 645443567878
        assert decode('42345565786', 10) == 42345565786
        assert decode('90789456847', 10) == 90789456847

    def test_decode_hexadecimal(self):
        assert decode('a', 16) == 10
        assert decode('f', 16) == 15
        assert decode('99', 16) == 153
        assert decode('ff', 16) == 255
        assert decode('ace', 16) == 2766
        assert decode('cab', 16) == 3243
        assert decode('bead', 16) == 48813
        assert decode('face', 16) == 64206
        assert decode('c0ffee', 16) == 12648430
        assert decode('facade', 16) == 16435934
        assert decode('deadbeef', 16) == 3735928559
        assert decode('f007ba11', 16) == 4027038225
        assert decode('8BA53', 16) == 571987
        assert decode('abcd', 16) == 43981
        assert decode('12345', 16) == 74565
        assert decode('a1b2c3d4', 16) == 2712847316
        assert decode('9f8e7d', 16) == 10456701
        assert decode('567def', 16) == 5668335
        assert decode('bad', 16) == 2989
        assert decode('badface', 16) == 195951310
        assert decode('feed', 16) == 65261
        assert decode('bee5ace9cad3cdead7', 16) == 3521431233792840690391

    def test_decode_10(self):
        assert decode('10', 2) == 2
        assert decode('10', 4) == 4
        assert decode('10', 6) == 6
        assert decode('10', 8) == 8
        assert decode('10', 10) == 10
        assert decode('10', 13) == 13
        assert decode('10', 16) == 16
        assert decode('10', 17) == 17
        assert decode('10', 20) == 20
        assert decode('10', 21) == 21
        assert decode('10', 24) == 24
        assert decode('10', 25) == 25
        assert decode('10', 28) == 28
        assert decode('10', 30) == 30
        assert decode('10', 32) == 32
        assert decode('10', 35) == 35
        assert decode('10', 36) == 36


    def test_decode_1010(self):
        assert decode('1010', 2) == 10
        assert decode('1010', 4) == 68
        assert decode('1010', 6) == 222
        assert decode('1010', 8) == 520
        assert decode('1010', 10) == 1010
        assert decode('1010', 13) == 2210
        assert decode('1010', 16) == 4112
        assert decode('1010', 17) == 4930
        assert decode('1010', 20) == 8020
        assert decode('1010', 21) == 9282
        assert decode('1010', 24) == 13848
        assert decode('1010', 25) == 15650
        assert decode('1010', 28) == 21980
        assert decode('1010', 30) == 27030
        assert decode('1010', 32) == 32800
        assert decode('1010', 35) == 42910
        assert decode('1010', 36) == 46692

    def test_decode_101101(self):
        assert decode('101101', 2) == 45
        assert decode('101101', 4) == 1105
        assert decode('101101', 6) == 8029
        assert decode('101101', 8) == 33345
        assert decode('101101', 10) == 101101
        assert decode('101101', 13) == 373660
        assert decode('101101', 16) == 1052929
        assert decode('101101', 17) == 1425060
        assert decode('101101', 20) == 3208401
        assert decode('101101', 21) == 4093804
        assert decode('101101', 24) == 7977025
        assert decode('101101', 25) == 9781876
        assert decode('101101', 28) == 17233105
        assert decode('101101', 30) == 24327901
        assert decode('101101', 32) == 33588225
        assert decode('101101', 35) == 52565976
        assert decode('101101', 36) == 60514129


class BasesEncodeTest(unittest.TestCase):

    def test_encode_binary(self):
        # assert encode(0, 2) == '0'  # Should '' be valid?
        assert encode(1, 2) == '1'
        assert encode(2, 2) == '10'
        assert encode(3, 2) == '11'
        assert encode(4, 2) == '100'
        assert encode(5, 2) == '101'
        assert encode(6, 2) == '110'
        assert encode(7, 2) == '111'
        assert encode(8, 2) == '1000'
        assert encode(9, 2) == '1001'
        assert encode(10, 2) == '1010'
        assert encode(11, 2) == '1011'
        assert encode(12, 2) == '1100'
        assert encode(13, 2) == '1101'
        assert encode(14, 2) == '1110'
        assert encode(15, 2) == '1111'
        assert encode(100, 2) == '1100100'
        assert encode(201, 2) == '11001001'
        assert encode(302, 2) == '100101110'
        assert encode(432, 2) == '110110000'
        assert encode(5345, 2) == '1010011100001'
        assert encode(683745, 2) == '10100110111011100001'
        assert encode(77243656, 2) == '100100110101010010100001000'
        assert encode(88743265, 2) == '101010010100001110101100001'
        assert encode(989823057, 2) == '111010111111111000000001010001'
        assert encode(2199023255551, 2) == '11111111111111111111111111111111111111111'
        assert encode(110, 2) == '1101110'
        assert encode(129384, 2) == '11111100101101000'
        assert encode(1398245, 2) == '101010101010111100101'

    def test_encode_decimal(self):
        # assert encode(0, 10) == '0'  # Should '' be valid?
        assert encode(5, 10) == '5'
        assert encode(10, 10) == '10'
        assert encode(25, 10) == '25'
        assert encode(64, 10) == '64'
        assert encode(99, 10) == '99'
        assert encode(123, 10) == '123'
        assert encode(789, 10) == '789'
        assert encode(2345, 10) == '2345'
        assert encode(6789, 10) == '6789'
        assert encode(13579, 10) == '13579'
        assert encode(24680, 10) == '24680'
        assert encode(58742, 10) == '58742'
        assert encode(108276, 10) == '108276'
        assert encode(22542355, 10) == '22542355'
        assert encode(64256344, 10) == '64256344'
        assert encode(9524569, 10) == '9524569'
        assert encode(129287253, 10) == '129287253'
        assert encode(3289475, 10) == '3289475'
        assert encode(287452865, 10) == '287452865'
        assert encode(6724578689, 10) == '6724578689'
        assert encode(18827635978, 10) == '18827635978'

    def test_encode_hexadecimal(self):
        assert encode(10, 16) == 'a'
        assert encode(15, 16) == 'f'
        assert encode(153, 16) == '99'
        assert encode(255, 16) == 'ff'
        assert encode(2766, 16) == 'ace'
        assert encode(3243, 16) == 'cab'
        assert encode(48813, 16) == 'bead'
        assert encode(64206, 16) == 'face'
        assert encode(12648430, 16) == 'c0ffee'
        assert encode(16435934, 16) == 'facade'
        assert encode(3735928559, 16) == 'deadbeef'
        assert encode(4027038225, 16) == 'f007ba11'
        assert encode(571987, 16) == '8ba53'
        assert encode(43981, 16) == 'abcd'
        assert encode(2712847316, 16) == 'a1b2c3d4'
        assert encode(10456701, 16) == '9f8e7d'
        assert encode(5668335, 16) == '567def'
        assert encode(2989, 16) == 'bad'
        assert encode(195951310, 16) == 'badface'
        assert encode(65261, 16) == 'feed'
        assert encode(3521431233792840826887, 16) == 'bee5ace9cad3d00007'

    def test_encode_1234(self):
        assert encode(1234, 2) == '10011010010'
        assert encode(1234, 3) == '1200201'
        assert encode(1234, 4) == '103102'
        assert encode(1234, 5) == '14414'
        assert encode(1234, 6) == '5414'
        assert encode(1234, 8) == '2322'
        assert encode(1234, 10) == '1234'
        assert encode(1234, 12) == '86a'
        assert encode(1234, 13) == '73c'
        assert encode(1234, 16) == '4d2'
        assert encode(1234, 17) == '44a'
        assert encode(1234, 20) == '31e'
        assert encode(1234, 21) == '2gg'
        assert encode(1234, 23) == '27f'
        assert encode(1234, 24) == '23a'
        assert encode(1234, 26) == '1lc'
        assert encode(1234, 28) == '1g2'
        assert encode(1234, 32) == '16i'

    def test_encode_248975(self):
        assert encode(248975, 2) == '111100110010001111'
        assert encode(248975, 3) == '110122112022'
        assert encode(248975, 4) == '330302033'
        assert encode(248975, 5) == '30431400'
        assert encode(248975, 6) == '5200355'
        assert encode(248975, 8) == '746217'
        assert encode(248975, 10) == '248975'
        assert encode(248975, 12) == '1000bb'
        assert encode(248975, 13) == '8942c'
        assert encode(248975, 16) == '3cc8f'
        assert encode(248975, 17) == '2gb8a'
        assert encode(248975, 20) == '1b28f'
        assert encode(248975, 21) == '15ibk'
        assert encode(248975, 23) == 'kaf0'
        assert encode(248975, 24) == 'i05n'
        assert encode(248975, 25) == 'fn90'
        assert encode(248975, 32) == '7j4f'
        assert encode(248975, 36) == '5c3z'

    def test_encode_into_10(self):
        assert encode(2, 2) == '10'
        assert encode(3, 3) == '10'
        assert encode(4, 4) == '10'
        assert encode(5, 5) == '10'
        assert encode(6, 6) == '10'
        assert encode(8, 8) == '10'
        assert encode(10, 10) == '10'
        assert encode(12, 12) == '10'
        assert encode(13, 13) == '10'
        assert encode(16, 16) == '10'
        assert encode(17, 17) == '10'
        assert encode(20, 20) == '10'
        assert encode(21, 21) == '10'
        assert encode(23, 23) == '10'
        assert encode(24, 24) == '10'
        assert encode(25, 25) == '10'
        assert encode(32, 32) == '10'
        assert encode(36, 36) == '10'

    def test_encode_into_1010(self):
        assert encode(10, 2) == '1010'
        assert encode(30, 3) == '1010'
        assert encode(68, 4) == '1010'
        assert encode(130, 5) == '1010'
        assert encode(222, 6) == '1010'
        assert encode(520, 8) == '1010'
        assert encode(1010, 10) == '1010'
        assert encode(1740, 12) == '1010'
        assert encode(2210, 13) == '1010'
        assert encode(4112, 16) == '1010'
        assert encode(4930, 17) == '1010'
        assert encode(8020, 20) == '1010'
        assert encode(9282, 21) == '1010'
        assert encode(12190, 23) == '1010'
        assert encode(13848, 24) == '1010'
        assert encode(15650, 25) == '1010'
        assert encode(32800, 32) == '1010'
        assert encode(46692, 36) == '1010'

    def test_encode_into_101101(self):
        assert encode(45, 2) == '101101'
        assert encode(280, 3) == '101101'
        assert encode(1105, 4) == '101101'
        assert encode(3276, 5) == '101101'
        assert encode(8029, 6) == '101101'
        assert encode(33345, 8) == '101101'
        assert encode(101101, 10) == '101101'
        assert encode(250705, 12) == '101101'
        assert encode(373660, 13) == '101101'
        assert encode(1052929, 16) == '101101'
        assert encode(1425060, 17) == '101101'
        assert encode(3208401, 20) == '101101'
        assert encode(4093804, 21) == '101101'
        assert encode(6449040, 23) == '101101'
        assert encode(7977025, 24) == '101101'
        assert encode(9781876, 25) == '101101'
        assert encode(33588225, 32) == '101101'
        assert encode(60514129, 36) == '101101'


class BasesConvertTest(unittest.TestCase):

    def test_convert_from_binary(self):
        assert convert('1101', 2, 3) == '111'
        assert convert('1101', 2, 4) == '31'
        assert convert('1101', 2, 8) == '15'
        assert convert('1101', 2, 10) == '13'
        assert convert('101010', 2, 3) == '1120'
        assert convert('101010', 2, 4) == '222'
        assert convert('101010', 2, 8) == '52'
        assert convert('101010', 2, 10) == '42'
        assert convert('101010', 2, 16) == '2a'
        assert convert('101010', 2, 25) == '1h'
        assert convert('101010', 2, 32) == '1a'
        assert convert('101010', 2, 36) == '16'

    def test_convert_to_binary(self):
        assert convert('111', 3, 2) == '1101'
        assert convert('31', 4, 2) == '1101'
        assert convert('15', 8, 2) == '1101'
        assert convert('13', 10, 2) == '1101'
        assert convert('101', 3, 2) == '1010'
        assert convert('101', 4, 2) == '10001'
        assert convert('101', 8, 2) == '1000001'
        assert convert('101', 10, 2) == '1100101'
        assert convert('101', 16, 2) == '100000001'
        assert convert('101', 25, 2) == '1001110010'
        assert convert('101', 32, 2) == '10000000001'
        assert convert('101', 36, 2) == '10100010001'

    def test_convert_hexadecimal_to_decimal(self):
        assert convert('a', 16, 10) == '10'
        assert convert('f', 16, 10) == '15'
        assert convert('99', 16, 10) == '153'
        assert convert('ff', 16, 10) == '255'
        assert convert('ace', 16, 10) == '2766'
        assert convert('cab', 16, 10) == '3243'
        assert convert('bead', 16, 10) == '48813'
        assert convert('face', 16, 10) == '64206'
        assert convert('c0ffee', 16, 10) == '12648430'
        assert convert('facade', 16, 10) == '16435934'
        assert convert('deadbeef', 16, 10) == '3735928559'
        assert convert('f007ba11', 16, 10) == '4027038225'

    def test_convert_decimal_to_hexadecimal(self):
        assert convert('10', 10, 16) == 'a'
        assert convert('15', 10, 16) == 'f'
        assert convert('153', 10, 16) == '99'
        assert convert('255', 10, 16) == 'ff'
        assert convert('2766', 10, 16) == 'ace'
        assert convert('3243', 10, 16) == 'cab'
        assert convert('48813', 10, 16) == 'bead'
        assert convert('64206', 10, 16) == 'face'
        assert convert('12648430', 10, 16) == 'c0ffee'
        assert convert('16435934', 10, 16) == 'facade'
        assert convert('3735928559', 10, 16) == 'deadbeef'
        assert convert('4027038225', 10, 16) == 'f007ba11'

    def test_convert_hexadecimal_to_binary(self):
        assert convert('a', 16, 2) == '1010'
        assert convert('b', 16, 2) == '1011'
        assert convert('c', 16, 2) == '1100'
        assert convert('d', 16, 2) == '1101'
        assert convert('e', 16, 2) == '1110'
        assert convert('f', 16, 2) == '1111'
        assert convert('c840', 16, 2) == '1100100001000000'
        assert convert('d951', 16, 2) == '1101100101010001'
        assert convert('ea62', 16, 2) == '1110101001100010'
        assert convert('fb73', 16, 2) == '1111101101110011'

    def test_convert_binary_to_hexadecimal(self):
        assert convert('1010', 2, 16) == 'a'
        assert convert('1011', 2, 16) == 'b'
        assert convert('1100', 2, 16) == 'c'
        assert convert('1101', 2, 16) == 'd'
        assert convert('1110', 2, 16) == 'e'
        assert convert('1111', 2, 16) == 'f'
        assert convert('1100100001000000', 2, 16) == 'c840'
        assert convert('1101100101010001', 2, 16) == 'd951'
        assert convert('1110101001100010', 2, 16) == 'ea62'
        assert convert('1111101101110011', 2, 16) == 'fb73'

    def test_convert_base_13_to_base_19(self):
        assert convert('3', 13, 19) == '3'
        assert convert('bac234', 13, 19) == '1edigg'
        assert convert('ccb324', 13, 19) == '1i02ib'
        assert convert('828bcb', 13, 19) == '1474c0'
        assert convert('984520', 13, 19) == '188h5d'
        assert convert('24566', 13, 19) == '9e2g'
        assert convert('53', 13, 19) == '3b'
        assert convert('a9251', 13, 19) == '26b11'
        assert convert('322', 13, 19) == '193'
        assert convert('cb73cbaaaaaaa', 13, 19) == '2aibd3037278'

    def test_convert_base_19_to_base_13(self):
        assert convert('3', 19, 13) == '3'
        assert convert('1edigg', 19, 13) == 'bac234'
        assert convert('1i02ib', 19, 13) == 'ccb324'
        assert convert('1474c0', 19, 13) == '828bcb'
        assert convert('188h5d', 19, 13) == '984520'
        assert convert('9e2g', 19, 13) == '24566'
        assert convert('3b', 19, 13) == '53'
        assert convert('26b11', 19, 13) == 'a9251'
        assert convert('193', 19, 13) == '322'
        assert convert('2aibd3037278', 19, 13) == 'cb73cbaaaaaaa'

    def test_convert_base_36_to_hexadecimal(self):
        assert convert('87w4', 36, 16) == '5d9f4'
        assert convert('v2578n', 36, 16) == '6ff0d1e7'
        assert convert('2n7289vn', 36, 16) == '303f5a9203'
        assert convert('wirun', 36, 16) == '3417d7f'
        assert convert('93gdf', 36, 16) == 'e91ea3'
        assert convert('w48tv', 36, 16) == '33725b3'
        assert convert('mvirug854', 36, 16) == '3ab1a04a9738'
        assert convert('cwj4758', 36, 16) == '68a33302c'
        assert convert('vrw98jw3', 36, 16) == '243c051afb3'
        assert convert('prow56', 36, 16) == '5cdfb7ba'

    def test_convert_hexadecimal_to_base_36(self):
        assert convert('5d9f4', 16, 36) == '87w4'
        assert convert('6ff0d1e7', 16, 36) == 'v2578n'
        assert convert('303f5a9203', 16, 36) == '2n7289vn'
        assert convert('3417d7f', 16, 36) == 'wirun'
        assert convert('e91ea3', 16, 36) == '93gdf'
        assert convert('33725b3', 16, 36) == 'w48tv'
        assert convert('3ab1a04a9738', 16, 36) == 'mvirug854'
        assert convert('68a33302c', 16, 36) == 'cwj4758'
        assert convert('243c051afb3', 16, 36) == 'vrw98jw3'
        assert convert('5cdfb7ba', 16, 36) == 'prow56'


if __name__ == '__main__':
    unittest.main()
