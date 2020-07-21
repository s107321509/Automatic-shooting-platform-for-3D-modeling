# 自動化三維掃描平台：平台組成與使用教學

## 序言

  
這是一個用於**Photogrammetry**的三維掃描平台，此平台以**低成本**的零組件所組成，可以用來**自動化完成三維建模所需的影像拍攝工作**。我們主要將其用於**昆蟲標本**三維掃描上，希望可以幫助國內數位標本由2D圖像展示轉為3D模型來瀏覽，讓使用者經由滑鼠旋轉3D模型來觀察整隻昆蟲。我們將平台組裝方式與使用到的原始碼在此開源，希望藉由開源可以讓各昆蟲博物館或相關單位引用此方法，來大量建置或是將我們的平台進行優化，我們非常樂意與各單位互相交流、討論，共同提升台灣數位標本3D化的程度。  
<img src="https://i.ibb.co/Qb9cCp0/lowcost3dscanner.png" alt="lowcost3dscanner" border="0">  

使用此程序之前，您必須準備以下設備：
1. Raspberry Pi    
2. 高畫素單眼相機  
3. NEMA17 步進馬達*3 (https://goods.ruten.com.tw/item/show?21405171072055&fbclid=IwAR1GomKSwFMTKWlX8ro5bkLu7ZaBOpcgn6ErBNjZy7c86bKhfIqxLVY3RmM)  
4. 步進滑台 (https://goods.ruten.com.tw/item/show?21812802023245#info)  
5. TB6600 三軸步進馬達驅動 (https://goods.ruten.com.tw/item/show?21820026614518)  
6. 印出[OpenScan]開源零件(https://www.thingiverse.com/thing:3050437)  
7. 電腦螢幕、鍵盤、滑鼠各1
8. 杜邦線數條

## 三維掃描平台架構
<img src="https://i.ibb.co/rQKBBwK/image.png" alt="image" border="0">  

## 二軸平台
二軸平台用來旋轉昆蟲標本，輔助相機拍攝標本各個角度的影像。由於國內還沒有相關應用，因此目前坊間尚無現成的二軸平台套件可以購買，而在國外有從事三維掃描相關單OpenScan，他們使用CAD軟體自行設計二軸機構，並將設計的模型檔在網路上公開下載，因此我們引用此開源機構，將零件由3D列印機印出，搭配兩顆型號為Nema17的步進馬達，將其組裝來作為我們的二軸平台。  
<img src="https://i.ibb.co/j3zgYkc/image.png" alt="image" border="0">

## 安裝

該項目使用gphoto2來控制相機拍照。使用前請確保已安裝此軟件。

```sh
$ sudo apt-get install gphoto2
```
使用前請確保安裝python2.7。

```sh
$ sudo apt-get install python2.7
```

##  用法

標本的拍攝過程大致可分為以下步驟：

1.用戶可以在中定義任意數量的傾斜角度和水平旋轉的步數tilting.py，如下所示，定義為水平轉盤每轉拍攝40個環繞圖像，並且傾斜軸每次移動300微步，從不同角度分為三個拍攝。

```sh
panning_step = [40,40,40]
tilting_step = [300,300,300]
```
2.`start.py` 用於控制堆疊平台的移動，以找到對象前後焦點的清晰範圍。使用讀取鍵盤琴鍵的方法將w定義為前進，將s定義為後退，使用a和d定義拍攝的開始和結束位置，最後按q鍵完成參數設置。

3.在水平轉盤的每個步驟之後，將調用堆疊程序。在堆疊的每個步驟之後，執行相機程序以自動控制相機拍攝樣本。

4.重複步驟（3），直到水平轉盤完成一圈。

5.將傾斜軸移至下一個角度，然後重複步驟（3）（4），直至獲得所有傾斜角。

6.拍攝完成後，三軸平台返回初始位置。
