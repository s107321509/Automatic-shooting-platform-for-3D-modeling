# 自動化三維掃描平台：平台組成與使用教學

## 序言

  
- 這是一個用於**Photogrammetry**的三維掃描平台，此平台以**低成本**的零組件所組成，可以用來**自動化完成三維建模所需的影像拍攝工作**。我們主要將其用於**昆蟲標本**三維掃描上，希望可以幫助國內數位標本由2D圖像展示轉為3D模型來瀏覽，讓使用者經由滑鼠旋轉3D模型來觀察整隻昆蟲。我們將平台組裝方式與使用到的原始碼在此開源，希望藉由開源可以讓各昆蟲博物館或相關單位引用此方法，來大量建置或是將我們的平台進行優化，我們非常樂意與各單位互相交流、討論，共同提升台灣數位標本3D化的程度。  
<img src="https://i.ibb.co/3vg2dZs/image.png" alt="image" border="0">

- 使用此程序之前，您必須準備以下設備：
1. Raspberry Pi    
2. 高畫素單眼相機 (Canon EOS 650D)  
3. NEMA17 步進馬達*3 (https://goods.ruten.com.tw/item/show?21405171072055&fbclid=IwAR1GomKSwFMTKWlX8ro5bkLu7ZaBOpcgn6ErBNjZy7c86bKhfIqxLVY3RmM)  
4. 步進滑台 (https://goods.ruten.com.tw/item/show?21812802023245#info)  
5. TB6600 三軸步進馬達驅動 (https://goods.ruten.com.tw/item/show?21820026614518)  
6. 印出**OpenScan**開源零件 (https://www.thingiverse.com/thing:3050437)  
7. 電腦螢幕、鍵盤、滑鼠各1
8. 杜邦線數條 (公對公、公對母)
9. 電源供應器 (24V 5A)  

## 三維掃描平台架構
<img src="https://i.ibb.co/v4wT9J2/image.png" alt="image" border="0">

## 二軸平台
- 二軸平台用來**旋轉昆蟲標本，輔助相機拍攝標本各個角度的影像**。由於國內還沒有相關應用，因此目前坊間尚無現成的二軸平台套件可以購買，而在國外有從事三維掃描相關單**OpenScan**，他們使用CAD軟體自行設計二軸機構，並將設計的模型檔在網路上公開下載，因此我們引用此開源機構，將零件由3D列印機印出，搭配兩顆型號為Nema17的步進馬達，將其組裝來作為我們的二軸平台。  
<img src="https://i.ibb.co/j8bxpjC/image.png" alt="image" border="0">

## 堆疊平台
- 由於微距攝影有較淺的景深，使用單一攝影參數拍攝一張影像無法讓整個昆蟲標本都能清晰呈現，因此對於立體有厚度的昆蟲標本，我們需要**用堆疊平台來拍攝多張不同景深的照片**，再將多張不同景深的照片透過 **Helicon focus**堆疊軟體合成出一張清晰的影像，讓標本的**每個部分都保持清晰**。此堆疊平台選擇市面上的鋁擠材料與步進馬達自行組裝而成，鋁擠材料包括軸承滑塊、螺桿導軌、導軌光軸、滾珠軸承座等，組裝容易且能透過樹莓派嵌入式平台控制單眼相機前後移動，其移動幅度可以透過程式參數來調整，以便於我們精準的找到標本前後清晰的範圍。  

<img src="https://i.ibb.co/TLvT8JP/image.png" alt="image" border="0">

## 馬達與TB6600驅動器連接方法
- 一般而言，大多數**二相四線**馬達的連接排線都由**黑、綠、紅、藍**四種顏色組成，依序表示A+、A-、B+、B-，而上述線的定義為常規但並非絕對，我們可以經由檢測來確認。由於兩相的步進馬達由兩組線圈組成，因此四條線中每兩條為一組會互相導通，我們可以先用三用電表來判斷哪兩條線為一組，將其代表為 A+、A-，而另外兩條則為 B+、B-，若通電後馬達轉向與預期相反，則將其中一組線圈兩條線交互對調即可。確認完線的順序後，就可以將三顆步進馬達使用杜邦線分別接到驅動器上1~3軸馬達接口位置。**黑色線接到 A+、綠色線接到 A-、紅色線接到 B+、藍色線接到 B-**。  

<img src="https://i.ibb.co/JrYSB5C/image.png" alt="image" border="0">

## 樹莓派與TB6600驅動器連接方法
- 接著使用杜邦線將馬達驅動1~3軸訊號控制接口分別接到樹莓派GPIO上，我們可以在程式中自行定義不同的GPIO腳位來控制馬達。訊號控制接口由左而右為PUL+、PUL-、DIR+、DIR-、ENA+、ENA-，其中ENA+和ENA-接口可不接線，**PUL是脈衝輸入**，**DIR為方向輸入**，，GPIO連接方式如下表。
<img src="https://i.ibb.co/kK9YR1V/image.png" alt="image" border="0">

<img src="https://i.ibb.co/JrhQ14R/GPIO.png" alt="GPIO" border="0">

## 完整接線方式如下圖
<img src="https://i.ibb.co/fGMJzcL/image.png" alt="image" border="0">

## 安裝相依套件

- 該項目使用gphoto2來控制相機拍照。使用前請確保已安裝此套件。

```sh
$ sudo apt-get install gphoto2
```
- 使用前請確保安裝python2.7。

```sh
$ sudo apt-get install python2.7
```

##  使用方法
- 查看當前正在運行的gphoto2程序  
```
ps -aux|grep gphoto2
```
<img src="https://i.ibb.co/5W3TmPS/03.jpg" alt="03" border="0">

- 移除舊的gphoto2程序 
```
kill -9 <代碼>
```
<img src="https://i.ibb.co/sjRtH38/04.jpg" alt="04" border="0">


- 標本的拍攝過程大致可分為以下步驟：

1.用戶可以在tilting.py中定義任意數量的傾斜角度和水平旋轉的步數，如下所示，定義為水平轉盤每轉拍攝40個環繞圖像，並且傾斜軸每次移動300微步，從不同角度分為三個拍攝。

```sh
panning_step = [40,40,40]
tilting_step = [300,300,300]
```
2.`start.py` 用於控制堆疊平台的移動，以找到對象前後焦點的清晰範圍。使用讀取鍵盤指令的方法將w定義為前進，將s定義為後退，使用a和d定義拍攝的開始和結束位置，最後按q鍵完成參數設置。

3.在水平轉盤的每個步驟之後，將調用堆疊程序。在堆疊的每個步驟之後，執行相機程序以自動控制相機拍攝樣本。

4.重複步驟（3），直到水平轉盤完成一圈。

5.將傾斜軸移至下一個角度，然後重複步驟（3）（4），直至獲得所有傾斜角。

6.拍攝完成後，三軸平台返回初始位置。
