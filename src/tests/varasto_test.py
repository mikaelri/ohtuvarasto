import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

        # lisätty testi
    def test_konstruktori_luo_tyhjan_varaston_positiivinen(self):
        self.pos = Varasto(7, 8) #alustetaan tilavuus < saldo
        self.assertAlmostEqual(self.pos.saldo, 7) #ei voi olla kuin maksimissaan tilavuus
        self.assertAlmostEqual(self.pos.tilavuus, 7) #ei voi olla kuin maksimissaan tilavuus

        # lisätty testi
    def test_konstruktori_luo_tyhjan_varaston_negatiivinen(self):
        self.neg = Varasto(-1, -1) #alustetaan negatiivisella tilavuudella ja saldolla
        self.assertAlmostEqual(self.neg.saldo, 0) #ei voi olla neg.
        self.assertAlmostEqual(self.neg.tilavuus, 0) #ei voi olla neg.

        # lisätty testi
    def test_ei_voi_ottaa_yli_tilavuuden(self):
        maara = self.varasto.ota_varastosta(self.varasto.saldo + 2) #koitetaan ottaa 2 yksikköä yli
        self.assertAlmostEqual(maara, self.varasto.saldo)

        # lisätty testi
    def test_negatiivinen_lisays_ei_lisaa_varastoa(self):
        alkusaldo = self.varasto.saldo #asetetaan aluksi 10
        self.varasto.lisaa_varastoon(-1) #koitetaan lisätä neg. saldo
        self.assertAlmostEqual(self.varasto.saldo, alkusaldo) 

        # lisätty testi
    def test_tilavuus_ei_mene_yli_saldon(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus + 30) #koitetaan lisätä 30 yksikkiöä yli
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

        # lisätty testi
    def test_negatiivinen_maara_ei_lisaa_varastoa(self):
        self.varasto.lisaa_varastoon(-2) #koitetaan lisätä -2 yksikkö 
        self.assertAlmostEqual(self.varasto.saldo, 0)

        # lisätty testi
    def test_negatiivinen_ottaminen_palauttaa_oikean_saldon(self):
        self.varasto.lisaa_varastoon(8) # lisäyksen jälkeen varastossa on 8
        self.varasto.ota_varastosta(-2) #otettu määrä on -2
        self.assertAlmostEqual(self.varasto.saldo, 8)

        # lisätty testi
    def test_positiivinen_ottaminen_palauttaa_oikean_saldon(self):        
        self.varasto.lisaa_varastoon(8) #lisäyksen jälkeen varastossa 8
        self.varasto.ota_varastosta(2) # otetaan 2 yksikköä pois
        self.assertAlmostEqual(self.varasto.saldo, 6)
        
        # lisätty testi
    def test_saldo_ei_ylitä_tilavuutta(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus + 30) #koitetaan lisätä yli max tilav.
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

        # lisätty testi
    def test_str(self):
        self.assertEqual(str(self.varasto), str(Varasto(10)))
