![](Output.001.png)VERİTABANI ![](Output.002.png)![](Output.003.png)![](Output.004.png)**TEKNORİTMA YAZILIM HİZMETLERİ** STANDARTLARI

T-30 Yürürlük Tarihi/Rev.No: 01.04.2009/00

**Evaluation Only. Created with Aspose.Words. Copyright 2003-2023 Aspose Pty Ltd.**

**Veritabanı Standartları V 1.0** 

**TEKNORITMA Yazılım Birimi** 

**Veritabanı Kullanım Standartları Ve** 

**Programlama Önerileri**

**Hazırlayan Hatem Karapınar** 

**Ankara, Nisan 2009**

|Doküman Tanımı ve Tarihçesi||
| - | :- |
|**Doküman Adı** |**TEKNORITMA Veritabanı Standartları: Versiyon 1.0 (25.03.2009)**|
|||
|**Dokümanı Hazırlayan** |**Hatem KARAPINAR,** *TEKNORITMA Yazılım Uzman Yardımcısı*|
|||
|**Doküman Dağıtım** |**Çağatay IŞIKSUNGUR,** *TEKNORITMA Yazılım Direktörü*|
||**TEKNORITMA Yazılım Ekibi**|

**0  İçindekiler** 

[1  Sözlük Ve Kısaltmalar Listesi ........................................................................................................4 ](#_page3_x68.00_y128.92)[2  SQL - Structured Query Language (Ansı SQL, SQL’92) ...................................................................5 ](#_page4_x68.00_y128.92)[3  SQL Dilleri ...................................................................................................................................5 ](#_page4_x68.00_y446.92)

[3.1  PL/SQL ve T-SQL Farklılıkları .................................................................................................6 ](#_page5_x68.00_y128.92)[4  Biçimsel Yazım Kuralları .............................................................................................................10 ](#_page9_x68.00_y128.92)

1. [İsimlendirme .....................................................................................................................10 ](#_page9_x68.00_y357.92)
1. [Girinti, Boşluk ve Blok Düzenleme......................................................................................12 ](#_page11_x68.00_y128.92)

[5  Veritabanı Bileşenleri ................................................................................................................15 ](#_page14_x68.00_y128.92)

1. [Veritabanı Kullanımı ..........................................................................................................15 ](#_page14_x68.00_y203.92)
1. [Tablo Kullanımı ..................................................................................................................16 ](#_page15_x68.00_y155.92)
1. [Fonksiyon ve Prosedür Kullanımı .......................................................................................18 ](#_page17_x68.00_y182.92)
1. [Tetikleyici Kullanımı ...........................................................................................................19 ](#_page18_x68.00_y195.92)
1. [İndeks Kullanımı ................................................................................................................19 ](#_page18_x68.00_y430.92)
1. [View Kullanımı ...................................................................................................................20 ](#_page19_x68.00_y209.92)
1. [Şema Kullanımı ..................................................................................................................20 ](#_page19_x68.00_y376.92)

[6  Normalizasyon ..........................................................................................................................21 ](#_page20_x68.00_y222.92)[7  Veritabanı Programlama ve Kullanımı Önerileri .........................................................................22 ](#_page21_x68.00_y209.92)[8  Veritabanı Peformans Yönetimi .................................................................................................25 ](#_page24_x101.00_y235.92)[9  Veritabanı Kullanım ve Performans Yönetimi Araçları ................................................................28 ](#_page27_x101.00_y276.92)

1. [Query Analyzer Kullanımı ...................................................................................................28 ](#_page27_x112.00_y364.92)
1. [SQL Profiler Kullanımı ........................................................................................................31 ](#_page30_x68.00_y689.92)

[10  SQL Injection Saldırıları ..........................................................................................................37 ](#_page36_x106.00_y128.92)

1. [Örnek Saldırılar ..............................................................................................................37 ](#_page36_x68.00_y418.92)
1. [İzinsiz Giriş Sağlama .......................................................................................................38 ](#_page37_x68.00_y128.92)
1. [Uzaktan Prosedür Çalıştırma ..........................................................................................39 ](#_page38_x68.00_y128.92)
1. [SQL Server Saldırıları ......................................................................................................39 ](#_page38_x68.00_y433.92)
1. [ODBC Hata Mesajları ile Yapılan Saldırılar ......................................................................40 ](#_page39_x68.00_y128.92)
1. [Veritabanında Veri Düzenleme ......................................................................................41 ](#_page40_x68.00_y544.92)
2. [SQL Injection dan Korunma Yolları .................................................................................42 ](#_page41_x68.00_y156.92)
1. [Kullanıcı Haklarının Sınırlandırılması ...............................................................................42 ](#_page41_x68.00_y228.92)
1. [Girdilerde  Tek Tırnak (’) İmlecinin Kontrol Edilmesi .......................................................42 ](#_page41_x68.00_y421.92)
1. [Arayüz Girdilerinden Gereksiz Karakterlerin Elenmesi ....................................................43 ](#_page42_x68.00_y169.92)
1. [Girdi Uzunluğunun Sınırlandırılması ...............................................................................44 ](#_page43_x68.00_y169.92)
1. [Girdi Cinsinin Kontrol Edilmesi .......................................................................................44 ](#_page43_x68.00_y268.92)
1. [GET Metodu yerine POST Kullanılması ...........................................................................44 ](#_page43_x68.00_y366.92)

[11  Öne Çıkanlar..........................................................................................................................45 ](#_page44_x106.00_y183.92)[12  Referanslar ............................................................................................................................46 ](#_page45_x68.00_y195.92)[EK 1 : Tam Metin Arama (Full Text Indexing) .....................................................................................47 ](#_page46_x68.00_y184.92)

<a name="_page3_x68.00_y128.92"></a>**1  Sözlük Ve Kısaltmalar Listesi** 



|ANSI |American National Standarts Institute |Amerikan Ulusal Standartlar Enstitüsü |
| - | - | - |
|SQL |Structured Query Language |Çeşitli veri düzenleme ve sorgulama işlemlerinin gerçekleştirilmesine olanak sağlayan evrensel sorgulama dili  |
|SEQUEL |Structured English Query Language |SQUARE dilinin geliştirilmiş hali |

<a name="_page4_x68.00_y128.92"></a>**2  SQL - Structured Query Language (Ansı SQL, SQL’92)** 

**SQL**, Türkçe karşılığı olarak yapılandırılmış sorgulama dili, bir veritabanı üzerinde çeşitli veri düzenleme ve sorgulama işlemlerinin gerçekleştirilmesine olanak sağlayan belirli mantıksal ve sözdizimsel kurallar ile yapılandırılmış sorgulama dilidir. 

Veritabanı yaklaşımının ortaya çıkmasıyla veri sorgulama ve düzenlemeler için bir veri sorgulama diline ihtiyaç duyulmuştur. Bu yaklaşımıın ilk yıllarında daha çok matematiksel bir sözdizime sahip **SQUARE** adında bir dil geliştirilmiştir. **SQUARE** dilinin matematiksel sözdiziminin zorluğu sebebiyle, 1970’li yılların ortalarında İngilizceye benzer ve daha kolay sözdimine sahip **SEQUEL** (Structured English Query Language) dili geliştirilmiştir. Daha sonra **SEQUEL**, **ANSI** tarafından standartlaştırılarak 1992 yılında **Structured Query Language** adını almıştır ve İngilizce söylenişine paralel olarak **SQL** olarak kısaltılmıştır. 

**SQL** dili zamanla ilişkisel veritabanı yönetim sistemlerinde (MS SQL Server, Oracle, DB2, PostgreSQL, MySQL, ..) standart dil haline gelmiştir. Bu sistemler **SQL** i bir alt dil şeklinde kullanarak kendi sistemlerine özgü diller geliştirmiştir. 

<a name="_page4_x68.00_y446.92"></a>**3  SQL Dilleri** 

Veritabanı yönetim sistemleri tarafından geliştirilen SQL dilleri ile, yazılımlarımızın içerisinden veya veritabanı sistemlerine bağlantı kurularak anlık çalıştırıdığımız sorguları, prosedür haline getirerek veritabanında tanımlayabiliriz. Böylece çalıştırdığımız sorgular veritabanında saklanır. Bu bir çok yönüyle performans ve maliyet kazancı sağlar. 

**T-SQL (Transact SQL)** ve **PL/SQL (Procedural Language / SQL)** en çok bilinen SQL dilleridir. Bu diller sözdizimsel ve mantıksal olarak SQL i temel alsalar da aralarında bazı farklılıklar mevcuttur. 

**PL/SQL**, Oracle tarafından geliştirilmiş, Oracle veritabanı sistemlerine özel bir dildir. SQL in kullanım kolaylığı ve esnekliği yapısal programlama dillerinin prosedürel özelliği ile birleştirilmiştir. PL/SQL, Ada dili örnek alınarak tasarlanmıştır. 

**T-SQL** ise SyBase ve Microsoft tarafından SyBase in ilk veritabanı sistemi DataServer için geliştirilmiştir. Daha sonra Ashton-Tate şirketinin de katkısıyla Microsoft ve SyBase, SQL Server ürününü geliştirmiş ve T-SQL son halini almıştır. T-SQL de, SQL e yapısal programlama teknikleri kazandırarak geliştirilmiştir. Bu yönüyle PL/SQL e benzer. 

<a name="_page5_x68.00_y128.92"></a>***3.1  PL/SQL ve T-SQL Farklılıkları*** 



||**PL/SQL** |**T-SQL** |
| :- | - | - |
|Veritabanı |**Oracle** |**SQL Server, SyBase** |
|Yeni bir veri türü Yaratmak  |<p>%TYPE, %ROWTYPE sözcüğü kullanılır. </p><p>Örnek: </p><p>*tl\_telefon   deneme.telefon%TYPE; deneme\_row   deneme%ROWTYPE;* </p>|<p>Sp\_addtype prosedürü kullanılır. </p><p>Örnek:  </p><p>*EXEC sp\_addtype 'MyType', 'smallint', NULL* </p>|
|Insert, update ve delete işlemlerinin öncesini ele almak |<p>BEFORE tetikleyicisi kullanılır. Örnek: </p><p>*CREATE TRIGGER TRIGGER\_A BEFORE INSERT*  </p><p>*ON TABLE\_A ..* </p>|<p>INSTEAD OF tetikleyicisi kullanılır. Örnek: </p><p>*CREATE TRIGGER TRIGGER\_B ON TABLE\_B* </p><p>*INSTEAD OF BEFORE AS ..* </p>|
|Veritabanı bileşen bilgileri |<p>DESCRIBE() fonksiyonu kullanılır. </p><p>Örnek: </p><p>*DESCRIBE Receptions*; </p>|<p>Sp\_help, sp\_columns gibi system prosedürleri kullanılır. </p><p>Örnek: </p><p>*EXEC SP\_COLUMNS 'Receptions';* </p>|
|Tablosuz select sorguları |<p>DUAL tablosu sorguya eklenmelidir. </p><p>*Örnek:* </p><p>SELECT ‘Hello World!’ FROM DUAL; </p>|<p>DUAL gibi bir tabloya ihtiyaç duymaz. </p><p>*Örnek:* </p><p>SELECT ‘Hello World!’ </p>|

<table><tr><th colspan="1" rowspan="2" valign="top">İçiçe tablolar </th><th colspan="1" valign="top">SQL Server da bu özellik yoktur. </th></tr>
<tr><td colspan="2" valign="top"><p><i>AS OBJECT (</i> </p><p><i>street VARCHAR2(15), city   VARCHAR2(15), state  CHAR(2),</i> </p><p><i>zip    VARCHAR2(5));</i>  </p><p><i>CREATE OR REPLACE TYPE AdressesTable     AS TABLE OF AddressType;</i> </p></td><td colspan="1" valign="top"></td></tr>
<tr><td colspan="1">Satır bazlı güvenlik kısıtları </td><td colspan="2">Oracle sistemi içerisinde desteklenmiştir. Tablo içerisindeki veriler user veya role ler ile ilişkilendirilir. </td><td colspan="1" valign="top">View ler ve sistem fonksiyonları ile manuel gerçekleştirilebilir. </td></tr>
<tr><td colspan="1" valign="top">Rownum, rowid  </td><td colspan="2"><p>Oracle de mevcuttur. Örnek: </p><p><i>SELECT ROWNUM,Name,Surname,Sal  FROM</i> </p><p>`    `<i>(SELECT * FROM Emp</i>  </p><p>`     `<i>ORDER BY Sal DESC)</i>  </p><p><i>WHERE ROWNUM<=10;</i></b>   </p></td><td colspan="1"><p>RANK() fonksiyonu kullanılabilir. </p><p>Örnek: </p><p><i>SELECT</i> </p><p><i>RANK() OVER(ORDER BY Sal) as ROWNUM,</i>  </p><p><i>Name, Surname, Sal</i> </p><p><i>FROM Emp</i> </p><p><i>ORDER BY Sal;</i> </p></td></tr>
<tr><td colspan="1" valign="top">Kayıt kilitleme </td><td colspan="2"><p>SELECT...FOR UPDATE ile yapılır Örnek: </p><p><i>SELECT CourseNumber, Instructor FROM Courses</i>  </p><p><i>FOR UPDATE OF Instructor</i> </p></td><td colspan="1" valign="top"><p>UPDLOCK sözcüğü ile gerçekleştirilir. </p><p>Örnek: </p><p><i>SELECT CourseNumber, Instructor FROM Courses</i>  </p><p><i>WITH (UPDLOCK)</i> </p></td></tr>
<tr><td colspan="1">Sorgu çalıştırma </td><td colspan="2" valign="top">SQL *Plus kullanılabilir. </td><td colspan="1" valign="top">Query Analyzer kullanılabilir. </td></tr>
<tr><td colspan="1" rowspan="2" valign="top">Hiyerarşik sorgulama tekniği </td><td colspan="1" valign="top">Desteklenmez. </td></tr>
<tr><td colspan="2" valign="top"><p><i>4  SELECT LEVEL,</i> </p><p><i>LPAD(' .', 2 * LEVEL 1) || FirstName || ' ' | |</i> </p><p><i>LastName AS Employee</i> </p><p><i>FROM Employee</i> </p><p><i>START WITH EmployeeId = (</i> </p><p><i>SELECT EmployeeId</i> </p><p><i>FROM Employee</i> </p><p><i>WHERE FirstName = 'Kevin'</i> </p><p><i>AND LastName = 'Black')</i> </p><p><i>CONNECT BY PRIOR EmployeeId = Manag erId;</i> </p><p>5      LEVEL EMPLOYEE </p><p>---------- -------------------------          1  Kevin Black </p><p>`         `2  ..Keith Long </p><p>`         `2  ..Frank Howard </p></td><td colspan="1" valign="top"></td></tr>
<tr><td colspan="1" valign="top">Sıradan Id Verme </td><td colspan="2"><p>SEQUENCE ler kullanılarak yapılır. </p><p>Önce yeni bir sequence tanımlanır ve başlangıç değerleri verilir. Daha sonra tabloya insert trigger ı tanımlanır. Trigger içerisinde her yeni kayıtta </p><p>Sequence.NextVal ile ilgili alanı set ederiz. </p><p>Örnek: </p><p><i>CREATE SEQUENCE ID_SEQ</i>  </p><p><i>START WITH 100 INCREMENT BY 1; SELECT ID_SEQ.NextVal;</i> </p></td><td colspan="1" valign="top"><p>Identity kullanılır. </p><p>Sıralı bir değer alacak olan alananın Identity özelliği aktifleştirilir, sıralı değerin başlangıç değeri ve değişim değeri belirtilir. </p></td></tr>
<tr><td colspan="1" valign="top">Select sözcüğü ile belirli sayıda veri çekmek </td><td colspan="1"><p>Rownum kullanılarak yapılabilir. Örnek: </p><p><i>SELECT Name,Surname,Sal  FROM</i> </p><p>`    `<i>(SELECT * FROM Emp</i>  </p><p>`     `<i>ORDER BY Sal DESC)  WHERE ROWNUM<=10;</i></b>   </p></td><td colspan="1" valign="top"><p>Top sözcüğü ile gerçekleştirilir. Örnek: </p><p><i>SELECT TOP 10 Name,Surname,Sal  FROM Emp</i>  </p><p><i>ORDER BY Sal DESC;</i>   </p></td></tr>
<tr><td colspan="1">Prosedür Kullanımı </td><td colspan="1" valign="top">Parametrelerin sadece sırası önemlidir. </td><td colspan="1">Parametre sırası ve isimleri birebir aynı olmak zorundadır. </td></tr>
<tr><td colspan="1">Trigger  FOR EACH ROW </td><td colspan="1"><p>Çalıştığımız satır sayısı ne olursa olsun  </p><p>ile trigger ın her satır için tekrar tekrar çalışarak bu satırları ele alması saplanır. </p></td><td colspan="1">Bu özellik yoktur. Bunun için trigger içinde cursor açarak üzerinde çalıştığımız satırları ele alabiliriz. </td></tr>
</table>

<a name="_page9_x68.00_y128.92"></a>**4  Biçimsel Yazım Kuralları** 

Türkçe karşılığı olarak yapılandırılmış sorgulama dili, bir veritabanı üzerinde çeşitli veri düzenleme ve sorgulama işlemlerinin gerçekleştirilmesine olanak sağlayan belirli mantıksal ve sözdizimsel kurallar ile yapılandırılmış sorgulama dilidir. 

T-SQL veya PL/SQL ile, daha önceki bölümlerde bahsettiğimiz gibi bu dillerin SQL e yapısal programlama işlevleri kazandırmasıyla, istediğimiz SQL cümleciklerini bloklar halinde yazabilir, fonksiyonlar ve prosedürler oluşturabiliriz. Bu aşamada dikkat etmemiz gereken bazı biçimsel kurallar vardır. 

Biçimsel kurallar, yazdığımız SQL cümleciklerinin okunabilirliğini artırır, bakımını kolaylaştırır ve geliştirme aşamasında eksiklerimizi ve yanlışlarımızı görmemizde kolaylık sağlar. 

1. ***İsimlendirme<a name="_page9_x68.00_y357.92"></a>*** 

TEKNORITMA projelerinde veritabanı programlama yaparken genel olarak İngilizce isimlendirme yapmalıyız. İngilizce karşılığı olmayan sözcükler için Türkçe isimlendirme yapabiliriz. Tanımlayacağımız veritabanı nesnelerinin işlevselliğine paralel isimler vermeliyiz. Böylece ilgili nesnelerin ne işe yaradıkları kolayca anlaşılabilir. 



<table><tr><th colspan="3"></th></tr>
<tr><td colspan="1" rowspan="3"></td><td colspan="1" valign="top">Not  :  </td><td colspan="1" rowspan="2"></td></tr>
<tr><td colspan="1" valign="top">Pascal Casing ve Camel Casing  tanımları bu doküman boyunca kullanılacaktır.  </td></tr>
<tr></tr>
</table>
**This document was truncated here because it was created in the Evaluation Mode.**
**Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/**

**HAZIRLAYAN ONAYLAYAN** Sayfa No ![](Output.005.png)![](Output.006.png)Yazılım Uzman Yardımcısı Teknik Müdür 12/36
