Merhaba arkadaşlar bu yazım da şifreleme algoritmalarından bahsediceğim.Ama öncesinde anahtar(key) kavramını açıklamak istiyorum ki konuyu daha iyi anlayabilelim.

Anahtar Nedir?

Arkadaşlar anahtarlar bizim şifrelenmiş verilerimizi açmayı sağlarlar.
Kullanım amaçları da hem veri güvenliği hem de tarafların birbirine ispatı için yani bizim iki tane elemanımız var İsmail abi ile mecnun diyelim(sahneyi hatırlasınız)” İsmail abi mecnuna diyor ki ben İsmail abin kanıtımda bak elimdeki anahtarım mecnun da diyor ki ben de mecnunum abi bak bu da benim anahtarım” bu anahtarlar birbirinden farklı olsalar da matematiksel olarak bağlantılılardır.
Peki kaç tane anahtar var 2 tür anahtarımız var public ve (private) anahtar şeklinde.
Private Key:256 bit uzunluğundaki alfanümerik şifrelerdir.Özeldirler ve kimseyle paylaşılmaması gerekirler.
Public Key:  anahtar adı üstünde herkes tarafından görülebilen alfanümerik şifrelerdir..Ayrıca matematik fonksiyonları kullanılarak  private key ‘den üretilirler.
Önemli Bilgi: Bu fonksiyon tersi olmayan bir fonksiyondur. Yani private key kullanılarak public key üretilir, ama Public key kullanılarak private key üretilemez.

Şifreleme Algoritmaları:

Şimdi gelelim şifreleme algoritmalarına iki tür algoritmamız var simetrik ve asitmetrik
Bunları ayıran temel farklardan birisi simetrik şifreleme de tek anahtar kullanılır.Asitmetrik de ise iki farklı anahtar kullanılır.
Simetrik şifreleme de hem şifreleme hem de şifreyi çözme de tek gizli  anahtar kullanılıyor.

DES (Data Encrytion Standard - Veri Şifreleme Standartı):
Blok şifreleme algoritmasıdır.Şifrelemeyi uzunlukları belli olan bloklar halinde yapar.DES algoritması 64 bitlik olmasına rağmen 56 bitlik uzunluğunda simetrik şifreleme algoritmasın da kullanılır.Her kullanımda kullanıma özel anahtar üretmesi güçlğ yanıdır.Ama algoritmanın yavaş olması zayıf yönüdür.2000’li yıllların başında kırılmasıyla itibarını kaybetmiştir.

AES (Advanced Encrytion Standard - Gelişmiş Şifreleme Standartı):
Des’e göre daha güvenlidir.Des’in kırılmasından sonra çeşitli bilim insanları tarafından bulunmuştur.DES’in zayıf yönlerini geliştirirek matematikle oluşturulmuş blok şifreleme algoritmasıdır.128,192 ve 256 bitlik üç türü vardır.AES yazılımda ve donanımda hızlı olması daha uygulanabilir olması ve daha hafızaya gerek duyması güçlü yönleridir.Günümüzde kullanılan tüm akademik pratik ve brute force saldırılarına karşı dayanaklı olduğu düşünülüyor.En yaygın kulllanılan simetrik şifreleme algoritmasıdır. 

Asimetrik şifrelemede iki anahtar kullanılıyor.Şifreleme için açık anahtar kullanıyor. şifreyi çözmek için gizli anahtar kullanılıyor ki bu abiyi paylaşmak sıkıntılı çünkü üçünçü şahıslar verilerinize erişebilir ver verilerinizle istediği gibi oynayabilir.

DH (Diffie-Helman):

1976 yılında bulunmuş ilk asimetrik şifreleme algoritmasıdır.Bunu yapan abilerimiz ilk aşamada veri paylaşma değilde güvenli bir kanal vasıtasıtla ortak bir şifrede bulmayı amaçlamışlar daha sonra bu şifreyle beraber verileri yollamışlar.Simetrik şifrelemenin zayıf kaldığı çoğu yönde başarılı olmuş.

RSA (Rivest-Shamir-Adleman):

Bu da anahtar dağıtımının yanında şifreleme ve şifre çözme işlemlerini de gerçekleştirmesidir.Daha çok ticari uygulamalar da tercih edilir.Aslında algoritma basittir(bilim inşalarına göre herhalde) bunu zor kılan çok büyük asal sayı oluşturuyor olabilmesidir.1024 bitlik bir algoritmadır(300 basamak aşağı yukarı).
Önemli bilgi:RSA asimetrik şifrelemedir 1024 bitliktir ve buda yaklaşık 300 basamaklı bir sayıya tekabül eder.
Dh (Diffie-Helman) 1976 yılında bulunmuş ilk asitmetrik şifreleme algoritmasıdır.

Avanatajları  Dezavantajları

Simetrik şifreleme:

•	Hızlıdır
•	Donanımla birlikte kullanılır
•	Güvenlidir
•	Anahtar dağıtımı zordur yani bir veriyi birden fazla kişiye ilettiğinden sıkıntılar çıkarabilir
•	Kimlik doğrulama ve bütünlük ilkeleri hizmetlerini güvenli bir şekilde gerçekleştirmek zordur.

Asimetrik şifreleme:

•	Kriptografinin ana ilkeleri olarak sayılan; bütünlük, kimlik doğrulama ve gizlilik hizmeti güvenli bir şekilde sağlanabilir
•	Yavaş çalışır
•	Anahtar uzunluklarından dolayı sıkıntılar oluyormuş
•	Anahtar dağıtımı daha kolaydır
