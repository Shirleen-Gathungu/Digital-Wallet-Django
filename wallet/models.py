from datetime import datetime
import email
from email import message

from email.headerregistry import Address
from locale import currency
from pydoc import ModuleScanner
from pyexpat import model
from unittest.util import _MAX_LENGTH
from xmlrpc.client import DateTime
from django.db import models


# Create your models here.  


class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.CharField(max_length=95)
    email=models.EmailField(max_length=254)
    phone_number=models.CharField(max_length=13)
    GENDER_CHOICES = (
           ("M", "Male"),
           ("F", "Female"),
           ("NB", "Non-Binary"),
    )
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    age=models.PositiveSmallIntegerField()
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
  
class Currency(models.Model):
    COUNTRY_CHOICES = (
('AFG','Afghanistan'),
('AF','Afghanistan'),
('ZA','Afrique du Sud'),
('AL','Albanie'),
('DZ','Algérie'),
('DE','Allemagne'),
('AD','Andorre'),
('AO','Angola'),
('AI','Anguilla'),
('AQ','Antarctique'),
('AG','Antigua-et-Barbuda'),
('AN','Antilles néerlandaises'),
('SA','Arabie saoudite'),
('AR','Argentine'),
('AM','Arménie'),
('AW','Aruba'),
('AU','Australie'),
('AT','Autriche'),
('AZ','Azerbaïdjan'),
('BJ','Bénin'),
('BS','Bahamas'),
('BH','Bahreïn'),
('BD','Bangladesh'),
('BB','Barbade'),
('PW','Belau'),
('BE','Belgique'),
('BZ','Belize'),
('BM','Bermudes'),
('BT','Bhoutan'),
('BY','Biélorussie'),
('MM','Birmanie'),
('BO','Bolivie'),
('BA','Bosnie-Herzégovine'),
('BW','Botswana'),
('BR','Brésil'),
('BN','Brunei'),
('BG','Bulgarie'),
('BF','Burkina Faso'),
('CA','Canada'),
('CV','Cap-Vert'),
('CL','Chili'),
('CN','Chine'),
('CY','Chypre'),
('CO','Colombie'),
('KM','Comores'),
('CG','Congo'),
('KP','Corée du Nord'),
('KR','Corée du Sud'),
('CR','Costa Rica'),
('HR','Croatie'),
('CU','Cuba'),
('DK','Danemark'),
('DJ','Djibouti'),
('DM','Dominique'),
('EG','Égypte'),
('AE','Émirats arabes unis'),
('EC','Équateur'),
('ER','Érythrée'),
('ES','Espagne'),
('EE','Estonie'),
('US','États-Unis'),
('ET','Éthiopie'),
('FI','Finlande'),
('FR','France'),
('GE','Géorgie'),
('GA','Gabon'),
('GM','Gambie'),
('GH','Ghana'),
('GI','Gibraltar'),
('GR','Grèce'),
('GD','Grenade'),
('GL','Groenland'),
('GP','Guadeloupe'),
('GU','Guam'),
('GT','Guatemala'),
('GN','Guinée'),
('GQ','Guinée équatoriale'),
('GW','Guinée-Bissao'),
('GY','Guyana'),
('GF','Guyane française'),
('HT','Haïti'),
('HN','Honduras'),
('HK','Hong Kong'),
('HU','Hongrie'),
('BV','Ile Bouvet'),
('CX','Ile Christmas'),
('NF','Ile Norfolk'),
('KY','Iles Cayman'),
('CK','Iles Cook'),
('FO','Iles Féroé'),
('FK','Iles Falkland'),
('FJ','Iles Fidji'),
('GS','Iles Géorgie du Sud et Sandwich du Sud'),
('HM','Iles Heard et McDonald'),
('MH','Iles Marshall'),
('PN','Iles Pitcairn'),
('SB','Iles Salomon'),
('SJ','Iles Svalbard et Jan Mayen'),
('TC','Iles Turks-et-Caicos'),
('VI','Iles Vierges américaines'),
('VG','Iles Vierges britanniques'),
('CC','Iles des Cocos (Keeling),'),
('UM','Iles mineures éloignées des États-Unis'),
('IN','Inde'),
('ID','Indonésie'),
('IR','Iran'),
('IQ','Iraq'),
('IE','Irlande'),
('IS','Islande'),
('IL','Israël'),
('IT','Italie'),
('JM','Jamaïque'),
('JP','Japon'),
('JO','Jordanie'),
('KZ','Kazakhstan'),
('KE','Kenya'),
('KG','Kirghizistan'),
('KI','Kiribati'),
('KW','Koweït'),
('LA','Laos'),
('LS','Lesotho'),
('LV','Lettonie'),
('LB','Liban'),
('LR','Liberia'),
('LY','Libye'),
('LI','Liechtenstein'),
('LT','Lituanie'),
('LU','Luxembourg'),
('MO','Macao'),
('MG','Madagascar'),
('MY','Malaisie'),
('MW','Malawi'),
('MV','Maldives'),
('ML','Mali'),
('MT','Malte'),
('MP','Mariannes du Nord'),
('MA','Maroc'),
('MQ','Martinique'),
('MU','Maurice'),
('MR','Mauritanie'),
('YT','Mayotte'),
('MX','Mexique'),
('FM','Micronésie'),
('MD','Moldavie'),
('MC','Monaco'),
('MN','Mongolie'),
('MS','Montserrat'),
('MZ','Mozambique'),
('NP','Népal'),
('NA','Namibie'),
('NR','Nauru'),
('NI','Nicaragua'),
('NE','Niger'),
('NG','Nigeria'),
('NU','Nioué'),
('NO','Norvège'),
('NC','Nouvelle-Calédonie'),
('NZ','Nouvelle-Zélande'),
('OM','Oman'),
('UG','Ouganda'),
('UZ','Ouzbékistan'),
('PE','Pérou'),
('PK','Pakistan'),
('PA','Panama'),
('PG','Papouasie-Nouvelle-Guinée'),
('PY','Paraguay'),
('NL','Pays-Bas'),
('PH','Philippines'),
('PL','Pologne'),
('PF','Polynésie française'),
('PR','Porto Rico'),
('PT','Portugal'),
('QA','Qatar'),
('CF','République centrafricaine'),
('CD','République démocratique du Congo'),
('DO','République dominicaine'),
('CZ','République tchèque'),
('RE','Réunion'),
('RO','Roumanie'),
('GB','Royaume-Uni'),
('RU','Russie'),
('RW','Rwanda'),
('SN','Sénégal'),
('EH','Sahara occidental'),
('KN','Saint-Christophe-et-Niévès'),
('SM','Saint-Marin'),
('PM','Saint-Pierre-et-Miquelon'),
('VA','Saint-Siège' ),
('VC','Saint-Vincent-et-les-Grenadines'),
('SH','Sainte-Hélène'),
('LC','Sainte-Lucie'),
('SV','Salvador'),
('WS','Samoa'),
('AS','Samoa américaines'),
('ST','Sao Tomé-et-Principe'),
('SC','Seychelles'),
('SL','Sierra Leone'),
('SG','Singapour'),
('SI','Slovénie'),
('SK','Slovaquie'),
('SO','Somalie'),
('SD','Soudan'),
('LK','Sri Lanka'),
('SE','Suède'),
('CH','Suisse'),
('SR','Suriname'),
('SZ','Swaziland'),
('SY','Syrie'),
('TW','Taïwan'),
('TJ','Tadjikistan'),
('TZ','Tanzanie'),
('TD','Tchad'),
('TF','Terres australes françaises'),
('IO','Territoire britannique Océan Indien'),
('TH','Thaïlande'),
('TL','Timor Oriental'),
('TG','Togo'),
('TK','Tokélaou'),
('TO','Tonga'),
('TT','Trinité-et-Tobago'),
('TN','Tunisie'),
('TM','Turkménistan'),
('TR','Turquie'),
('TV','Tuvalu'),
('UA','Ukraine'),
('UY','Uruguay'),
('VU','Vanuatu'),
('VE','Venezuela'),
('VN','Viêt Nam'),
('WF','Wallis-et-Futuna'),
('YE','Yémen'),
('YU','Yougoslavie'),
('ZM','Zambie'),
('ZW','Zimbabwe'),
('MK','ex-République yougoslave de Macédoine'),
)
    country= models.CharField(max_length=30,choices= COUNTRY_CHOICES)
    
    symbol_name= models.CharField(max_length= 20,null=True)
    amount= models.BigIntegerField()


class Wallet(models.Model):
    balance = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='wallet_customer')
    date_created = models.DateTimeField()
    status = models.CharField(max_length=15)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE,related_name='wallet_currency')
    history = models.DateTimeField()
    pin = models.IntegerField()


class Account(models.Model):
    account_name = models.CharField(max_length=20)
    account_number = models.IntegerField()
    ACCOUNT_CHOICES=(
        ("P", "Personal Account"),
        ("B", "Business Account"),
    )
    account_type = models.CharField(max_length=20,choices=ACCOUNT_CHOICES)
    account_balance = models.IntegerField()
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='account_wallet')

class Transaction(models.Model):
    message = models.CharField(max_length=100)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='transaction_wallet')
    transaction_amount = models.BigIntegerField()
    transaction_charge = models.IntegerField()
    transaction_type = models.CharField(max_length=16)
    origin_account = models.ForeignKey(Wallet, on_delete=models.CASCADE,related_name='transaction_origin')
    destination_account = models.ForeignKey(Wallet, on_delete=models.CASCADE,related_name='transaction_destination')



class Card(models.Model):
    card_number= models.IntegerField()
     
    CARD_CHOICES=(
        ("P", "Debit Card"),
        ("B", "Credit Card"),
    )
    card_type= models.CharField(max_length=20,choices=CARD_CHOICES)
    expiry_date = models.DateField()
    security_code = models.IntegerField()
    date_of_issue = models.DateTimeField()
    wallet= models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='card_wallet')
    account= models.ForeignKey(Account,on_delete=models.CASCADE,related_name='card_account')
    issuer= models.CharField(max_length=10)



class ThirdParty(models.Model):
    account= models.ForeignKey(Account,on_delete=models.CASCADE,related_name='thirdparty_account')
    transaction_amount= models.BigIntegerField()
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE,related_name='thirdparty_currency')
    date_of_issue = models.DateTimeField()
    wallet= models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='thirdparty_wallet')
    issuer= models.CharField(max_length=20)



class Notification(models.Model):
    message= models.CharField(max_length=100)
    date = models.DateTimeField()
    recipient= models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='thirdparty_recipient')
    title = models.CharField(max_length=20)



class Receipt(models.Model):
    receipt_type= models.CharField(max_length = 20)
    date = models.DateTimeField()
    receipt_number= models.IntegerField()
    amount= models.IntegerField()
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='thirdparty_transaction')
    receipt_file = models.FileField()



class Loan(models.Model):
    loan_id = models.IntegerField()
    loan_type = models.CharField(max_length=15)
    loan_balance = models.IntegerField()
    amount = models.IntegerField()
    guaranter = models.CharField(max_length=20)
    issuer = models.CharField(max_length=20)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='loan_wallet')


  


class Reward(models.Model):
    transaction= models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='reward_transaction')
    recipient = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='reward_recipient')
    date_of_reward = models.DateTimeField()
    points = models.IntegerField()
    

